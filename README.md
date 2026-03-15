# E-ink_calendar
This is my project I made for the HackClub Blueprint YSWS. It is a calendar/ToDo tracker using an E-ink display, which can sit on your desk, and show you a calendar, and up to 5 tasks which you can mark as completed using 5 mechanical buttons next to the display.

To add tasks to the todo system you can send a message using a BLE terminal from any device.The first time you use it the time will probably be set incorrectly, and to set it you have to send `/tmst mmddhhmm` where the first mm means current month(like 03), dd is the current day(example: 09), hh is the current hour(for example 13), and the second mm is the minute(like 46). So if the time would be 2026, march 9th, 1:46 PM, you would send `/tmst 03091346`. Note that if the current year is not 2026 you will have to update the code.py file, and the 1.bin, 2.bin, ..., 12.bin files, but I will post the new versions in a new commit.

I mainly made this project to make use of the Blueprint YSWS, since it ends in a few weeks, and I wanted something cool. When thinking about project ideas I sudennly remembered someone building a little desktop habit tracker/To-do list, and thats where I started out of. I would like to give credit to the person who did the original device that gave me this idea, but i couldn't remember where I saw it. I also sometimes struggle with forgetting things that I should do, so i thought a device like this would help me, and potentially others with the same problem.

**Full assembly:**

![image](https://github.com/jivespark/E-ink_calendar/blob/main/Docks/FullAssembly.png)

You will need to use jumper wires to connect the display with the pcb. See this wiring diagram for more info(the yellow lines show what to connect with what):

![image](https://github.com/jivespark/E-ink_calendar/blob/main/Docks/Wiring.png)

**Schematic:**

![image](https://github.com/jivespark/E-ink_calendar/blob/main/Docks/Schematic.png)

**PCB:**

![image](https://github.com/jivespark/E-ink_calendar/blob/main/Docks/PCB.png)

BOM:

|Item                                         |Description    |Quantity|Unit price($)(Including tax)|Total price($)(Including tax)|URL:                                                     |Running total:|
|---------------------------------------------|---------------|--------|----------------------------|-----------------------------|---------------------------------------------------------|--------------|
|XIAO nRF52840                                |Microcontroller|1       |13.72                       |13.72                        |https://www.aliexpress.com/item/1005008326858009.html    |13.72         |
|waveshare 800×480, 7.5inch E-Ink display     |Display        |1       |56.99                       |56.99                        |https://www.waveshare.com/product/7.5inch-e-paper-hat.htm|70.71         |
|10pcs XDA2 Keycaps                           |Keycaps        |10      |0.34                        |3.43                         |https://www.aliexpress.com/item/1005006910173774.html    |74,14         |
|Mechanical Keyboard Replacement Blue Switches|Keyswitches    |16      |0.19                        |3.14                         |https://www.aliexpress.com/item/1005011789237834.html    |77,28         |

