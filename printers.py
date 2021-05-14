def commands():
    print("""
        start - Start a new activity
        show - Show current session activities
        export - Exports current session activities to JSON
        commands - Shows available commands
        activities - Shows avaialble activities
        add - Add new activity
        report - Print a report
        alarm - Set an alarm
""")

init_message = """
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
"""

date_selection = """
            today - Print a report for today
            weekly - Print a weekly report
            monthly - Print a monthly report
            day - Print a specific day report
"""

specific_date = """  
            Enter date in format YYYY-MM-DD, for example:

            2021-05-01                       
"""

weekly_start_date = """
            Enter start date in format YYYY-MM-DD, for example:

            2021-05-01
"""

