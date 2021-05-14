import json, os
from time import time, ctime
from datetime import timedelta, date

script_dir = os.path.dirname(__file__) #<-- absolute

# Returns a list -> str -> timestamp -> hours:minutes:seconds.milliseconds
json_files = [pos_json for pos_json in os.listdir(f"{script_dir}/reports/") if pos_json.endswith('.json')]

def convert_timestamp(activity=None, d_data=None):
    # activity -> ['Undecided', '0:06:21.742420', '20452264']
    # d_data -> str -> 3:37:37
    # Returns -> type timedelta -> 3:19:59

    # Converts a timestamp from already added data set and returns the delta
    if activity == None:
        new_set = d_data.replace(".", ":").split(":")
        new_values = [int(x) for x in new_set]

        delta = timedelta(hours=new_values[0], minutes=new_values[1], seconds=new_values[2])
        return delta
    else:
        # Else it converts new timestamp and returns the delta
        print("@@@@@@@@@@@@@@@@ DEBUG DATA BELOW @@@@@@@@@@@@@@@@")
        print("ACTIVITY PRINT --------")
        print(activity)
        print("ACTIVITY PRINT -----")
        clean_data = activity[1].replace(".", ":").split(":")
        print("CLEAN DATA -------------")
        print(clean_data)
        print(type(clean_data))
        print("CLEAN DATA -------------")
        print("@@@@@@@@@@@@@ DEBUG DATA END @@@@@@@@@@@@@@@@@")

        try:
            clean_data_int = [int(x) for x in clean_data]
        except ValueError:
            clean_data_int = [0, 1, 2, 3]
        
        delta = timedelta(hours=clean_data_int[0], minutes=clean_data_int[1], seconds=clean_data_int[2])
        return delta
            


def read_report(json_data_file):
    # json_data_file -> .json -> {"Undecided+0:03:08.625016+72752169": "0:03:08.625016", ... }
    # Retruns a single set of activities -> {'Undecided': '0:35:05', 'Chess': '0:10:10.256330', ... }
    d_set = {}

    with open(f"{json_data_file}") as json_file:
        data = json.load(json_file)
        clean_data = [activities.split("+") for activities in data]
        print("@@@@@@@@@@@@@@@@ DEBUG DATA BELOW @@@@@@@@@@@@@@@@")
        print("read_report clean_data ~~~~~~~~~~~~~")
        print(clean_data)
        print("read_report clean_data ~~~~~~~~~~~~~")
    
        for activity in clean_data:
            print("read_report activity -----------------")
            print(activity)
            print("read_report activity -----------------")
            print("@@@@@@@@@@@@@ DEBUG DATA END @@@@@@@@@@@@@@@@@")
            if activity[0] in d_set:
                # If aleady in d, then add the two timestamps together and replace the value in d
                
                old_timestamp_delta = convert_timestamp(d_data=d_set[activity[0]])
                new_timestamp_delta = convert_timestamp(activity)

                total_timestamp = old_timestamp_delta + new_timestamp_delta
                d_set[activity[0]] = str(total_timestamp)

            else:
                # Simply add to d
                d_set[activity[0]] = activity[1]
    return d_set
    
def pretty_print(data_set):
    if isinstance(data_set, dict):
        for key, value in data_set.items():
            print(f"""
                ------------------------
                Activity name: {key}
                Time spent: {value}
                ------------------------
            """)
    elif isinstance(data_set, list):
        print(data_set)

def weekly_print(start_date):
    # Returns a weekly set of activities -> {'2021-05-01.json': {'Undecided': '0:35:05', 'Chess': '0:10:10.256330', ... }, '2021-05-02.json': {'Other': ... }}
    weekly_set = {}
    stop = 7

    def combine_sets(weekly_activities_set):
        # Combines the weekly activities set and returns singular data output -> {'Other': '1:35:21', ... }
        combined_set = {}

        for key, value in weekly_activities_set.items(): # -> 2021-05-01.json - {'Undecided': '0:35:05' ... }
            for activity, time_length in value.items(): # -> Undecided - 0:35:05
                if activity in combined_set.keys():
                    # If aleady in combined_set, then add the two timestamps together and replace the value in combined_set
                    
                    old_timestamp_delta = convert_timestamp(d_data=combined_set[activity])
                    new_timestamp_delta = convert_timestamp(activity)

                    total_timestamp = old_timestamp_delta + new_timestamp_delta
                    combined_set[activity] = str(total_timestamp)

                else:
                    combined_set[activity] = time_length
        
        pretty_print(combined_set)


    for report, value in enumerate(json_files):
        if value == f"{start_date}.json":
            new_list = json_files[report:report+stop] # List of str -> json file names
         
    try:
        for i in new_list:
            weekly_set[i] = read_report(f"reports/{i}")
    except UnboundLocalError:
        pass
        combine_sets(weekly_set)  
    combine_sets(weekly_set)


    


