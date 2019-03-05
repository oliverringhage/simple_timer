import time
import re
import sys

total_time = str(sys.argv[1])
if(re.search("^[\d]{1,5}m[0-5]?[0-9]s$", total_time)):
    mins = int(total_time[:total_time.find('m')])
    secs = int(total_time[total_time.find('m') + 1 :total_time.find('s')])
    while(mins > 0 or secs > 0):
        print("%2d minutes and %2d seconds" % (mins, secs))
        time.sleep(1)
        secs = (secs - 1) % 60
        if(secs == 59):
            mins = mins - 1
    print("\n\n\n\n\nTime is up")
else:
    print("Input in the wrong form, should be: xxmxxs, or minutes > 59")
