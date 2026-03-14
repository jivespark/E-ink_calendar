from display_driver import get_display
from img_render import draw_bg, refresh_todo, load_tasks
from todo_buttons import check_todo
from DaM import month, day
from ble_get import ble_receive
import rtc
import time
import json
from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService

#This initiates BLE so that someone can connect from any device with a BLE terminal
ble=BLERadio()
uart=UARTService()
ble.start_advertising(uart)

r = rtc.RTC()

#This is just a placeholder date, to set the date and time, you need to send /tmst mmddhhmm
r.datetime = time.struct_time((
    2026, 3, 5,     # year, month, day
    14, 30, 0,      # hour, minute, second
    3, -1, -1       # weekday, yearday, DST
))
c_day=day()
c_month=month()
display=get_display()
l=[True, True, True, True, True]
labels=draw_bg(display)
while True:
    #------------BLE------------#
    if not ble.connected:
        ble.start_advertising(uart)
    tmst, msg=ble_receive(ble, uart)
    if msg:
        if tmst:#Set time through ble
            m=msg[6:8]
            d=msg[8:10]
            h=msg[10:12]
            mi=msg[12:14]
            r.datetime = time.struct_time((
                2026, int(m), int(d),  # year, month, day
                int(h), int(mi), 0,    # hour, minute, second
                3, -1, -1              # weekday, yearday, DST
            ))
        else:
            with open("todo.json", "r") as f:
                data = json.load(f)
            tasks = data["tasks"]
            changed=False
            for i in range(5):
                if tasks[i]=="":
                    tasks[i]=msg
                    changed=True
                    break
            if changed:
                data["tasks"]=tasks
                with open("todo.json", "w") as f:
                    json.dump(data, f)
    
    #------------Date------------#
    if c_month!=month():
        c_month=month()
        labels=draw_bg(display)
    if c_day!=day():
        c_day=day()
        labels=draw_bg(display)

    #------------ToDo------------#
    change, l=check_todo(l)
    if change:
        refresh_todo(display, labels)
    time.sleep(0.1)