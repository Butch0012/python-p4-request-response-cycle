import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

# This function is a Flask before_request hook.
# It runs before every request and sets the 'path' attribute in the global 'g' object.
@app.before_request
def app_path():
    # Get the absolute path of the current working directory and store it in 'g.path'
    g.path = os.path.abspath(os.getcwd())

# This route handles requests to the root URL ('/')
@app.route('/')
def index():
    # Get the 'Host' header from the HTTP request
    host = request.headers.get('Host')
    
    # Get the name of the current Flask application
    appname = current_app.name
    
    # Construct the HTML response body
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    # Set the HTTP status code to 200 (OK)
    status_code = 200
    
    # Define an empty dictionary for headers (not used in this example)
    headers = {}

    # Create a Flask response object using make_response
    response = make_response(response_body, status_code, headers)

    # Return the response object
    return response

# Run the Flask app if this script is the main module
if __name__ == '__main__':
    app.run(port=5555)
