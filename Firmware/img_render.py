import board
import busio
import displayio
import json
from adafruit_display_text import label
from DaM import month, day
import terminalio
import adafruit_uc8179

def load_tasks():
    with open("/todo.json", "r") as f:
        data = json.load(f)
    return data["tasks"]

def load_old():
    with open("/todo.json", "r") as f:
        data = json.load(f)
    return data["out"]

def draw_bg(display):

    bitmap = displayio.Bitmap(800, 480, 2)

    palette = displayio.Palette(2)
    palette[0] = 0xFFFFFF  # white
    palette[1] = 0x000000  # black

    cmonth=month()
    cday=day()
    with open(str(cmonth)+'.bin', "rb") as f:
        raw = f.read()

    byte_index = 0

    for y in range(480):
        for x_byte in range(800 // 8):
            byte = raw[byte_index]
            byte_index += 1

            for bit in range(8):
                pixel=(byte>>(7-bit))&1
                bitmap[x_byte*8+bit, y]=pixel

    tile = displayio.TileGrid(bitmap, pixel_shader=palette)

    main_group = displayio.Group()
    main_group.append(tile)

    display.root_group = main_group
    #------------date------------#
    s_month=''
    s_day=str(cday)+'th'
    if cday==1:
        s_day='1st'
    elif cday==2:
        s_day='2nd'
    elif cday==3:
        s_day='3rd'
    if cmonth==1:
        s_month='January '
    elif cmonth==2:
        s_month='Febuary '
    elif cmonth==3:
        s_month='March '
    elif cmonth==4:
        s_month='April '
    elif cmonth==5:
        s_month='May '
    elif cmonth==6:
        s_month='June '
    elif cmonth==7:
        s_month='July '
    elif cmonth==8:
        s_month='August '
    elif cmonth==9:
        s_month='September '
    elif cmonth==10:
        s_month='October '
    elif cmonth==11:
        s_month='November '
    elif cmonth==12:
        s_month='December '
    date_label=label.Label(
        terminalio.FONT,
        text=s_month+s_day,
        color=0x000000
    )
    date_label.scale=2
    date_label.anchor_point=(0, 1)
    date_label.anchored_position=(10, 470)
    main_group.append(date_label)
    #------------todo------------#
    tasks = load_tasks()
    labels = []

    left_margin=450
    top_margin=80
    line_spacing=70

    for i in range(5):
        task_text = tasks[i]

        task_label = label.Label(
            terminalio.FONT,
            text=f"{'-'}. {task_text}",
            color=0x000000
        )

        task_label.scale=2
        task_label.anchor_point=(0, 0)
        task_label.anchored_position=(
            left_margin,
            top_margin+i*line_spacing
        )
        main_group.append(task_label)
        labels.append(task_label)

    display.refresh()
    return labels

def refresh_todo(display, labels):
    tasks=load_tasks()
    old=load_old()
    if tasks!=old:
        for i in range(5):
            labels[i].text=f"- {tasks[i]}"
        with open("/todo.json", "r") as f:
            data = json.load(f)
        data["out"]=tasks
        with open("/todo.json", "w") as f:
            json.dump(data, f, indent=4)
        display.refresh()
    else:
        return