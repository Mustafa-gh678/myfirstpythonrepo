
import time
from datetime import datetime
import winsound

alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")

print("Alarm set for", alarm_time)
print("Waiting for alarm...")

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == alarm_time:
        print("Wake up! Your alarm is ringing!")

        while True:
            winsound.Beep(1000, 1000)
            stop = input("Type 'stop' to turn off the alarm: ")

            if stop.lower() == "stop":
                print("Alarm stopped!")
                break

        break

    time.sleep(1)
