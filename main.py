
# Import necessary modules
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the generate_planner route
@app.route('/generate_planner', methods=['POST'])
def generate_planner():
    # Get the user's input
    tasks = request.form.getlist('task')
    start_times = request.form.getlist('start_time')
    end_times = request.form.getlist('end_time')

    # Create a list of dictionaries to store the user's input
    tasks_and_times = []
    for task, start_time, end_time in zip(tasks, start_times, end_times):
        tasks_and_times.append({
            'task': task,
            'start_time': start_time,
            'end_time': end_time
        })

    # Sort the tasks by start time
    tasks_and_times.sort(key=lambda task: task['start_time'])

    # Create a list of available time slots
    available_time_slots = []
    start_time = '9:00 AM'
    end_time = '5:00 PM'
    while start_time <= end_time:
        available_time_slots.append({
            'start_time': start_time,
            'end_time': start_time
        })
        start_time = add_time(start_time, 30)

    # Generate the daily planner
    daily_planner = []
    for task in tasks_and_times:
        # Find the first available time slot that can accommodate the task
        available_time_slot = next((time_slot for time_slot in available_time_slots if time_slot['start_time'] <= task['start_time'] and time_slot['end_time'] >= task['end_time']), None)

        # If no available time slot is found, skip the task
        if not available_time_slot:
            continue

        # Add the task to the daily planner
        daily_planner.append({
            'task': task['task'],
            'start_time': task['start_time'],
            'end_time': task['end_time']
        })

        # Remove the used time slot from the list of available time slots
        available_time_slots.remove(available_time_slot)

    # Render the planner.html template with the generated daily planner
    return render_template('planner.html', daily_planner=daily_planner)

# Define a function to add time
def add_time(time, minutes):
    # Convert the time to a datetime object
    time = datetime.strptime(time, '%I:%M %p')

    # Add the minutes to the datetime object
    time = time + timedelta(minutes=minutes)

    # Convert the datetime object back to a string
    time = time.strftime('%I:%M %p')

    # Return the new time
    return time

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
