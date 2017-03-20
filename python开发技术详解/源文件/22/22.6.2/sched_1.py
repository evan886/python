#!/usr/bin/python
#encoding=utf-8

import time, os
import sched

schedule = sched.scheduler(time.time, time.sleep)

def execute_command(cmd, inc):
    os.system(cmd)
    schedule.enter(inc, 0, execute_command, (cmd, inc))
    
def main(cmd, inc=60):
    schedule.enter(0, 0, execute_command, (cmd, inc))
    schedule.run( )

main("netstat -an", 60)
