# keep-system-active
Script to keep your computer awake

## Purpose: 
This is a simple Python script that demonstrates how to use argparse,os,pyautogui and time modules in just few lines of codes.This script can be used to keep your system awake.
It takes two arguments i.e number of minutes system is to be awakened and action to be taken after  that no of minutes.
 
## Sources
For step by step guide please visit my blog [@shaikhu](https://shaikhu.com/how-to-keep-your-computer-awake-using-python)

## Usage: app.py -t count -a s|r
- count is no of minutes to keep system awake
- s|r : s to shutdown, r to restart computer after count no of minutes
## examples
1. to keep a system active for 300 minutes: 
```
c:\Users\jaqsp\> app.py -t 300
```
2. keep a system active for 1 hour and then turn off the PC
```
c:\Users\jaqsp\> app.py -t 60 -a s
```
3. keep a system  active for 2 hours and then restart it
```
c:\Users\jaqsp\> app.py -t 120 -a r
```
