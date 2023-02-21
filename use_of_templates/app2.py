# Import the necessary modules from Flask library
from flask import Flask, request, render_template

# Initialize the Flask application
app = Flask(__name__)


# Define a route for the index page
@app.route('/')
def index():
    # Render the form template
    return render_template('POST.html')


# Define a route for submitting the form
@app.route('/submit', methods=['POST'])
def submit():
    # Get the user's feedback from the form
    feedback = request.form['feedback']

    # Render the template that displays the feedback
    return render_template('GET.html', feedback=feedback)


# Run the application if this file is executed as the main program
if __name__ == '__main__':
    app.run()
