# keep-system-active
Script to keep your computer awake

Purpose: Script to keep your system alive. It takes two arguments i.e number of minutes system is to be awakened 
         and action to be taken after  that no of minutes.
Usage: app.py -t COUNT -a s|r
example to keep a system active for 30 minutes: keep_your_system_alive.py -t 30
example to keep a system active for 1 hour and then turn off the PC: keep_your_system_alive.py -t 60 -a s
example to keep a system  active for 2 hours and then restart it: keep_your_system_alive.py -t 120 -a r
