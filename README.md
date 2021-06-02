# TimeKeeperCLI

Extremely simple and lightweight activity time tracker accessible as a command line interface tool. 

TimeKeeper Front-End -> https://github.com/Arivald8/TimeKeeper-Front-End
TimeKeeper Back-End -> https://github.com/Arivald8/TimeKeeper-Back-End
(CLI will get integrated with the Django backend in the future)

## Overview

TimeKeeper works by measuring the time between the start time and the finish time of any given activity.
It provides an option to check current session activities as well as their duration. Any amount of activities can be added, 
but only one activity can be activated at any given time. Besides showing active session activities, TimeKeeper allows you to 
export an active session into JSON. Exporting activities to JSON allows for daily, weekly and monthly report summarries.

For example, you can track all of your activities for a week and then produce a weekly report. The report will let you know how much time you
spent on each activity in that week, allowing you to understand and improve your time management. 

TimeKeeper allows you to set sound alarms before you begin an activity. For example, you can set an alarm for 15 minutes and then start 
an activity. After 15 minutes, a beeping alarm will be heard.

Before TimeKeeper can track your activities, they have to be added to the tool. Activities should be added separately in order to limit report issues.
For example, if you would like to see how much time you spent on reading the previous week, you might run into a problem if there is an activity called "Read"
and an activity called "Reading". All added activities can be found in a JSON file "activities_settings.json".

## Interface

### Welcome Screen

```

          |----------|
          |TimeKeeper|
          |----------|
    |-----------------------|
    |- Track your activities|
    |- Export into JSON     |
    |- Create Reports       |
    |-----------------------|
                  by A.Dorsz


Type "commands" to see available commands


>
```

### Available Commands:

```
> commands


        start - Start a new activity
        show - Show current session activities
        export - Exports current session activities to JSON
        commands - Shows available commands
        activities - Shows avaialble activities
        add - Add new activity
        report - Print a report
        alarm - Set an alarm


>
```
### add
```
> add

New activity name: Tester
------------------
Activities Updated

>
```

### start
```
> start


Enter activity name > Reading

Activity "Reading" started.
-----------------------------------
Waiting to stop the activity...
Type any key to stop.

Activity "Reading" stopped.
 Total time elapsed: 0:11:12.217614

>
```

### show
```
> show

--------------------------------
Activity: 'Reading+0:11:12.217614+18011864' & Time Elapsed: 0:00:12.217614
--------------------------------
--------------------------------
Activity: 'Learning+0:25:01.382924+68509090' & Time Elapsed: 0:00:01.382924
--------------------------------

>
```

### activities
```
> activities

------------------
QA
Work
Undecided
Chores
Learning
Fun
Cooking
Waste
Test
Other
Chess
Resting
Eating
Walk
Reading
Tester
------------------

>

```

### alarm
```
> alarm

Alarm to play in hh:mm:ss
> 00:00:10
Alarm set for 00:00:10

>
```

### report
If a report for an active session has not been exported, option to print a report for today will return "No such file exists..."
```
> report


            today - Print a report for today
            weekly - Print a weekly report
            monthly - Print a monthly report
            day - Print a specific day report

> today
No such file exists...

>
```
If a report exists, it will be printed to the screen.
```
> report


            today - Print a report for today
            weekly - Print a weekly report
            monthly - Print a monthly report
            day - Print a specific day report

> day

            Enter date in format YYYY-MM-DD, for example:

            2021-05-01

> 2021-05-01

                ------------------------
                Activity name: Undecided
                Time spent: 0:35:05
                ------------------------


                ------------------------
                Activity name: Chess
                Time spent: 0:10:10.256330
                ------------------------


                ------------------------
                Activity name: Chores
                Time spent: 4:58:29
                ------------------------


                ------------------------
                Activity name: Cooking
                Time spent: 0:41:44.173526
                ------------------------


                ------------------------
                Activity name: Resting
                Time spent: 0:33:39.922232
                ------------------------


                ------------------------
                Activity name: Eating
                Time spent: 0:16:48.928308
                ------------------------


                ------------------------
                Activity name: Fun
                Time spent: 3:38:24
                ------------------------


                ------------------------
                Activity name: Walk
                Time spent: 3:17:08.473622
                ------------------------


                ------------------------
                Activity name: Learning
                Time spent: 0:05:20.619188
                ------------------------
```
Weekly report example:
```
> report


            today - Print a report for today
            weekly - Print a weekly report
            monthly - Print a monthly report
            day - Print a specific day report

> weekly

            Enter start date in format YYYY-MM-DD, for example:

            2021-05-01

> 2021-05-01

                ------------------------
                Activity name: Undecided
                Time spent: 4:50:08
                ------------------------


                ------------------------
                Activity name: Chess
                Time spent: 7:29:13
                ------------------------


                ------------------------
                Activity name: Chores
                Time spent: 9:14:09
                ------------------------


                ------------------------
                Activity name: Cooking
                Time spent: 10:27:09
                ------------------------


                ------------------------
                Activity name: Resting
                Time spent: 0:43:25
                ------------------------


                ------------------------
                Activity name: Eating
                Time spent: 0:16:48.928308
                ------------------------


                ------------------------
                Activity name: Fun
                Time spent: 15:08:03
                ------------------------


                ------------------------
                Activity name: Walk
                Time spent: 9:47:33
                ------------------------


                ------------------------
                Activity name: Learning
                Time spent: 12:57:53
                ------------------------


                ------------------------
                Activity name: Other
                Time spent: 8:09:13
                ------------------------


                ------------------------
                Activity name: Waste
                Time spent: 7:10:01
                ------------------------


                ------------------------
                Activity name: Reading
                Time spent: 4:34:45
                ------------------------


                ------------------------
                Activity name: QA
                Time spent: 9:26:07
                ------------------------


>
```

### export
```
> export


Activities successfully exported.

>
```

### How to run TimeKeeper

Clone the repository and execute `python timekeeper.py`






