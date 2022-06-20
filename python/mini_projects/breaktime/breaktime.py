# ========================================
# Created     : Mon Jun 20 2022
# Author      : s7marsh
# Description : Take a break reminder
# ========================================

from copy import copy
import time
import datetime
import webbrowser

# Some parameters
eod_time = (input("When does your day end? <HH:MM> ") or "17:00") # default is 5PM
work_duration_minute = (input("Break reminder every? <minute> ") or 20) # default is 20 minutes

# Helper Functions
def is_before_eod_time(eod_time):
    """
    returns True if currently before eod_time.
    eod_time is a string, formatted as `%H:%M`
    """
    eod_hh = int(eod_time.split(':')[0])
    eod_mm = int(eod_time.split(':')[1])
    now = datetime.datetime.now()
    eod = copy(now)
    eod = eod.replace(hour=eod_hh,minute=eod_mm,second=0,microsecond=0)
    return now < eod

# Main
print("Start at "+ time.ctime() + "\nEnd at "+eod_time)
while is_before_eod_time(eod_time):
    # Every after 20 mins
    time.sleep(60*work_duration_minute)
    # Play a this youtube video
    webbrowser.open("https://www.youtube.com/watch?v=aynkFJdXF_M")
print("Good job! it's the end of the day.")


