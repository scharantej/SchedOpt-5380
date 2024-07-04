---
## Optimized Prompt

### Create a Flask application that generates a personalized daily planner based on user input. The planner should take into account the user's available time slots and tasks.

## Flask Application Design

### HTML Files

**index.html**

* The main page where the user inputs their tasks and available time slots.
* Fields for entering tasks, start times, end times, and a submit button.
* Contains JavaScript code for manipulating the form submission.

**planner.html**

* The page that displays the generated daily planner.
* Structure to display the user's tasks and available time slots in a table format.

### Routes

**home()**

* The route handler for the index page.
* Renders the 'index.html' template.

**generate_planner()**

* The route handler that processes the user's input.
* Receives the user's tasks and time slots as form data.
* Generates the daily planner based on the user's input.
* Renders the 'planner.html' template with the generated planner.

### Implementation

1. Create a new Flask project and add the necessary HTML files and routes.
2. Design the form in 'index.html' to capture the user's input.
3. Implement the 'generate_planner()' route to process the form submission and generate the planner.
4. Use Flask's rendering functions to display the 'index.html' and 'planner.html' templates.