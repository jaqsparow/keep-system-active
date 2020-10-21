"""
Author: Javed Shaikh
Purpose: Script to keep your system alive. It takes one argument i.e number of minutes system is to be awakened 
         and action to be taken after  that no of minutes.
Usage: app.py -t COUNT -a s|r
example to keep a system active for 30 minutes: keep_your_system_alive.py -t 30
example to keep a system active for 1 hour and then turn off the PC: keep_your_system_alive.py -t 60 -a s
example to keep a system  active for 2 hours and then restart it: keep_your_system_alive.py -t 120 -a r
"""
import argparse
import pyautogui
import time
import os

def timer(stop_time, action):
    counter = 0
    while stop_time > counter:
        #Lets sleep for 60 seconds only
        time.sleep(60)
        pyautogui.click(button='right')
        counter = counter + 1
    #Save current date and time
    timestamp = time.strftime('%d-%b-%Y_%H-%M-%S', time.localtime())
    #Create a text log when system shutsdown
    f = open('C:\\Users\\jaqsp\\Snapshot\\shutdown_logs.txt','a+')
    f.write('Shutting down at {}'.format(timestamp))
    f.close()
    #Take screenshot
    image_location = 'C:\\Users\\jaqsp\\Snapshot\\image_' + timestamp + '.jpeg'
    pyautogui.screenshot(image_location)

    #Shutdown system or Restart
    if action in ['s', 'S']:
        os.system("shutdown -s -f -t 0")
    if action in ['r', 'R']:
        os.system("Shutdown -r -f -t 0")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="Enter time in minutes")
    parser.add_argument("-a", "--action", help="want to shutdown?")

    args = parser.parse_args()
    if args.time:
        timer(int(args.time), args.action)

