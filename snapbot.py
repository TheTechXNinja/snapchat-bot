import pyautogui
import keyboard
import time
import sys

exitProgram = False

# prepare to exit the program
def quit():
    global exitProgram
    exitProgram=True
    
# set hotkey    
keyboard.add_hotkey('q', lambda: quit())

pose = []
letters = ["camera", "send to", "person you want to send to", "send"]
num = 0
while num < 4:
    print(f"Press enter when Over {letters[num]} Button")
    if keyboard.read_key() == "enter":
        position = pyautogui.position()
        pose.append(position)
        time.sleep(.4)
    num += 1

# main loop to do things
score = 0
snaps_sent = int(input("enter now many snaps you want to send: "))
speed = float(input("Now how fast do you want to send the snaps ie.(.1, .2, .3, .4 etc.): "))
time.sleep(2)
while not exitProgram and score < snaps_sent:
    score += 1
    time.sleep(speed)
    pyautogui.leftClick(pose[0])
    time.sleep(speed)
    pyautogui.leftClick(pose[1])
    time.sleep(speed)
    pyautogui.typewrite("ww")
    time.sleep(speed)
    pyautogui.leftClick(pose[2])
    time.sleep(speed)
    pyautogui.leftClick(pose[3])
    print(f"snap ({score}) sent!")

    
print("the program has quit successfully")
sys.exit()
