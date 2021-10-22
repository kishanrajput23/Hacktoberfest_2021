
"""
Created on Tue Aug  3 18:03:02 2021

@author: Kaushal Barhate

This is a python script to notify daily college/school timetable on windows 10.
The program creates a timetable.db file and saves the timetable in it.
At the start of the every class the user would get notification on their windows 10 laptop stating which class has started and at what time will it end.
"""

import sqlite3
import schedule
from plyer import notification
import time 

conn = sqlite3.connect('timetable.db')
c=conn.cursor()
try:
    c.execute("CREATE TABLE timetable1(class text, start_time text, end_time text, day text)")
except:
    pass    

while(True):
    a=int(input("Select option: \n 1.Add class \n 2.View TimeTable \n 3.Delete a class \n 4.stop \n"))
    if(a==1):
        name=input("Enter class name= ")
        start_time=input("Enter start time= ")
        end_time=input("Enter end time= ")
        day=input("day= ")
        c.execute("INSERT INTO timetable1 VALUES ('%s','%s','%s','%s')"%(name,start_time,end_time,day))
        conn.commit()
    elif(a==2):
        for row in c.execute('SELECT * FROM timetable1'):
            print(row)
            
    elif(a==3):
        name=input("Enter name= ")
        c.execute("DELETE FROM timetable1 where class='%s'"%(name))
        conn.commit()
        
    elif(a==4):
        break
        
def notify_win(name,day,start_time,end_time):
    notification.notify(title="%s Class started at %s"%(name,start_time),  
                        message="Class ends at %s\n "%(end_time))
    
def sched():
    for row in c.execute('SELECT * from timetable1'):
        name=row[0]
        start_time=row[1]
        end_time=row[2]
        day=row[3]
        if(day.lower()=="monday"):
            schedule.every().monday.at(start_time).do(notify_win,name,day,start_time,end_time)
            print("Scheduled class '%s' on %s at %s"%(name,day,start_time))
        if(day.lower()=="tuesday"):
            schedule.every().tuesday.at(start_time).do(notify_win,name,day,start_time,end_time)
            print("Scheduled class '%s' on %s at %s"%(name,day,start_time))
        if(day.lower()=="wednesday"):
            schedule.every().wednesday.at(start_time).do(notify_win,name,day,start_time,end_time)
            print("Scheduled class '%s' on %s at %s"%(name,day,start_time))   
        if(day.lower()=="thursday"):
            schedule.every().thursday.at(start_time).do(notify_win,name,day,start_time,end_time)
            print("Scheduled class '%s' on %s at %s"%(name,day,start_time))
        if(day.lower()=="friday"):
            schedule.every().friday.at(start_time).do(notify_win,name,day,start_time,end_time)
            print("Scheduled class '%s' on %s at %s"%(name,day,start_time))
        if(day.lower()=="saturday"):
            schedule.every().saturday.at(start_time).do(notify_win,name,day,start_time,end_time)
            print("Scheduled class '%s' on %s at %s"%(name,day,start_time))    
        if(day.lower()=="sunday"):
            schedule.every().sunday.at(start_time).do(notify_win,name,day,start_time,end_time)
            print("Scheduled class '%s' on %s at %s"%(name,day,start_time))    
    while True:
        schedule.run_pending()
        time.sleep(1)  
        
sched()
