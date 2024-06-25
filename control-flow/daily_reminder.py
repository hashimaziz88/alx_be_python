# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate inputs
if priority not in ['high', 'medium', 'low']:
    print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
else:
    if time_bound not in ['yes', 'no']:
        print("Invalid response for time-bound. Please enter 'yes' or 'no'.")
    else:
        # Process the task based on priority and time sensitivity
        reminder = f"Reminder: '{task}' is a {priority} priority task"
        
        match priority:
            case 'high':
                reminder += " that requires immediate attention!"
            case 'medium':
                reminder += ". Try to complete it soon."
            case 'low':
                reminder += ". Consider completing it when you have free time."
        
        # Modify the reminder if the task is time-bound
        if time_bound == 'yes':
            reminder += " Don't forget, it needs to be done today!"
        
        # Print the customized reminder
        print(reminder)
