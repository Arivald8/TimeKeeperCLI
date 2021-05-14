import reports, alerts, printers
import json, random
from datetime import timedelta, date
from time import time


activity_storage = {}

class Activity:
    def __init__(self, name, start_time):
        self.name = name
        self.start_time = start_time

    def activity_time(self):
        return timedelta(seconds=time() - self.start_time)

    def store_activity(self):
        activity_storage[f"{self.name}+{str(self.activity_time())}+{random.randint(999999, 99999999)}"] = str(self.activity_time())

def start_activity():
    print("")
    activity_name = input("Enter activity name > ")
    print("")
    if activity_name not in available_activities():
        print("Activity not added!")
    else:
        activity = Activity(name=activity_name, start_time=time())
        print(f'Activity "{activity.name}" started.')
        print("-----------------------------------")
        print(f"Waiting to stop the activity...")
        activity_stop = input("Type any key to stop.")
        print("-----------------------------------")
        print(f'Activity "{activity.name}" stopped.\n Total time elapsed: {activity.activity_time()}')
        activity.store_activity()

def show_activities():
    for key, value in activity_storage.items():
        print("--------------------------------")
        print(f"Activity: '{key}' & Time Elapsed: {value}")
        print("--------------------------------")

def dump_activities():
    json_name = date.today()
    with open(f"reports/{str(json_name)}.json", 'w') as f:
        json.dump(activity_storage, f)

    print("")
    print("Activities successfully exported.")

def available_activities():
    AVAILABLE_ACTIVITIES = []

    with open('activities_settings.json') as json_file:
        data = json.load(json_file)
        for i in data['Activities']:
            AVAILABLE_ACTIVITIES.append(i)
    return AVAILABLE_ACTIVITIES

def show_available_activities():
    AVAILABLE_ACTIVITIES = []

    with open('activities_settings.json') as json_file:
        data = json.load(json_file)
        for i in data['Activities']:
            AVAILABLE_ACTIVITIES.append(i)

    print("------------------")
    for i in AVAILABLE_ACTIVITIES:
        print(i)
    print("------------------")
  

def add_activity():
    data = input("New activity name: ")
    with open('activities_settings.json') as f:
        json_data = json.load(f)
        print("------------------")
        json_data['Activities'].append(data)
        
    with open('activities_settings.json', 'w') as f:
        json.dump(json_data, f)

    print("Activities Updated")


available_commands = {
    "start": start_activity,
    "show": show_activities,
    "export": dump_activities,
    "commands": printers.commands,
    "activities": show_available_activities,
    "add": add_activity,
    "report": reports.pretty_print,
    "alarm": alerts.activity_alarm
    }