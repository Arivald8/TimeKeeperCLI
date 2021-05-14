import winsound
import datetime
from threading import Timer

def activity_alarm():

    def alarm():
            for _ in range(4):
                duration = 200  # milliseconds
                freq = 440  # Hz
                winsound.Beep(freq, duration)
    
    print("Alarm to play in hh:mm:ss")

    alarm_time = input("> ")
    time_list = alarm_time.split(":")
    delta = datetime.timedelta(hours=int(time_list[0]), minutes=int(time_list[1]), seconds=int(time_list[2]))
    time_seconds = delta.total_seconds()

    t = Timer(time_seconds, alarm)
    print(f"Alarm set for {alarm_time}")
    t.start()
