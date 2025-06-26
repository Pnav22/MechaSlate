---
title: "Mecha Slate"
author: "Pranav Mukkara"
description: "Custom Built Keyboard"
created_at: "2025-06-20"
---

**Total Time Spent: 810 minutes (13.5 hours)**

---

## June 20: Research, Learning, and Starting

So this is my first time making a keyboard. I had zero experience. I first learned how to make some basic PCBs on KiCad following Joe Scotto's tutorial. Very nice guy!  
Link here: https://www.youtube.com/watch?v=8WXpGTIbxlQ&ab_channel=JoeScotto  
Here is some sample circuits I made from his tutorial.

**Total Time Spent: 60 mins**

### created practice PCBs  
| PCB | Schematic |
|:-------------------------:|:-------------------------:|
| ![PCB Front](https://github.com/user-attachments/assets/fe14e158-7bf4-4130-a9e4-d2c2ffe600b3) | ![PCB Back](https://github.com/user-attachments/assets/0920f8ec-823d-4420-902b-3d1fbaa8548c) |

**Total Time Spent: 90 mins**

---

## June 21: Initial Design

This was kinda scary because I was so afraid of messing something up. I knew I wanted a keyboard with  no number pad. Here is a reference:

![image](https://github.com/user-attachments/assets/5022cb00-1b8f-4f8d-9eed-496a488ff698)

I made an initial sketch for the matrix. I decided to use the Arduino Pro Micro for my MCU.

![image](https://github.com/user-attachments/assets/eb706fce-0594-4e8b-9120-f8f950bf33c4)

Decide to base my project off this keyboard: 
![image](https://github.com/user-attachments/assets/375b4509-4335-4047-8f0a-fa6b8db1fd74)


_Edit: I'm not doing the top row – the ESC row._  

I dont know how mechanical keyboards work so I did a little research on this stuff. Apparently it doesnt seem so hard to make? I think I could make this easily. 
_Edit: This was so hard. It is so so hard to engineer stuff :( But I kinda like the struggle _
![image](https://github.com/user-attachments/assets/49211bdb-7b2f-44fb-89b5-5081d8bbe36e)


**Total Time Spent: 60 mins**

---

## June 21: Making the Schematics
_Edit: I decided to do the esc row again _

So I made this schematic. I used a json file and free tool online to make it. It was convient and it gave me this. 
![Screenshot 2025-06-25 142915](https://github.com/user-attachments/assets/34225385-e449-4b23-acfc-49091696b969)
So far so good lets move on.
**Total Time Spent: 30 mins**

## June 21: Making the pcb
Disaster struck. For some reason the schematic was so buns I could barely make the pcb. The schematic was missing things and their were just a whole bunch of errors. 
![Screenshot 2025-06-25 155947](https://github.com/user-attachments/assets/67dccc9c-11da-4330-948e-d6331cfed35f)

I spent like a hour trying to troubleshoot. I installed, reinstalled, i did all the librarys again and i searched online. Massive waste of time.

**Total Time Spent: 90 mins**


## June 22: Restarting
So I made so many mistakes and everything that i thought it would be easier to just restart from scratch. 
So i delted everything - very painfull 
and redid the schematic. 




![image](https://github.com/user-attachments/assets/bdc40540-bcfa-4218-b22b-1539af9df3dd)

Was very painful to do this again. BUT LOOK. SO PRETTY

Something I learned is that you should keep everything bevel and straight. When I duplicated the switches they would shift down slightly or up. this made wiring so hard I decided to wipe and create a schematic where everything was on the same level so i could wire with straight lines. - something to learn for the future. 

**Total Time Spent: 60 mins**


---

## June 21: Remaking the PCB

I didn’t want to manually move each square, so I’m trying to find a better solution—probably a plugin.  
Found a plugin to use. It was an absolute pain to use.  
Used a JSON file.  
This is hopefully what it should look like perfect:


This is the most painful thing I have done so far. The wiring was an absolute pain in the butt.

![image](https://github.com/user-attachments/assets/746c39b6-2719-4e80-a50a-436dbb346b28)

So much better than the last PCB
but look its so pretty. I added a angry face to it aswl. I really like how it turned out. 

Most of this time was spent on trying to use the plugin. 
**Time Spent: 180 mins**
---

## June 25: Making the CAD

This should be the easiest part.

**Back done**  
![image](https://github.com/user-attachments/assets/a3622311-2f57-4e30-843a-bcb4fbbe01a6)

**Front done**  
![image](https://github.com/user-attachments/assets/c723ca9a-8d94-49c9-b8a2-eebfd8053d2d)

Now just assembly.  

Finally finished the whole project. Manually putting the keycaps in took very long.

![image](https://github.com/user-attachments/assets/c05ccc66-1ff3-4efa-8257-af330fe5bb88)

It took so long because I manually inserted and moved every switch and key. Not a good idea for the future. 
**Time Spent: 240 mins**
