import digitalio
import board
import json

sw1=digitalio.DigitalInOut(board.D0)
sw1.direction=digitalio.Direction.INPUT
sw1.pull=digitalio.Pull.UP

sw2=digitalio.DigitalInOut(board.D1)
sw2.direction=digitalio.Direction.INPUT
sw2.pull=digitalio.Pull.UP

sw3=digitalio.DigitalInOut(board.D2)
sw3.direction=digitalio.Direction.INPUT
sw3.pull=digitalio.Pull.UP

sw4=digitalio.DigitalInOut(board.D3)
sw4.direction=digitalio.Direction.INPUT
sw4.pull=digitalio.Pull.UP

sw5=digitalio.DigitalInOut(board.D4)
sw5.direction=digitalio.Direction.INPUT
sw5.pull=digitalio.Pull.UP


def check_todo(l: list):
    c = [sw1.value, sw2.value, sw3.value, sw4.value, sw5.value]
    with open("todo.json", "r") as f:
        data = json.load(f)
    tasks = data["tasks"]
    changed=False

    for i in range(5):
        if l[i] and not c[i]:
            for j in range(i, 4):
                tasks[j] = tasks[j+1]
            tasks[4] = ""
            changed=True
            break

    if changed:
        data["tasks"]=tasks
        with open("todo.json", "w") as f:
            json.dump(data, f)
    return changed, c
        
