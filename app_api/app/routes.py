from app import app_api

@app_api.route('/')
def index():
    return '''
    <html>
        <head>
            <title>Home Page - UG48 API</title>
        </head>
        <body>
            <h1>Welcome to our UG48 API</h1>
            <a href="http://localhost:5000/get-users">List users</a><br>
            <a href="http://localhost:5000/add">Add user</a><br>
            <a href="http://localhost:5000/delete">Delete User</a>
        </body>
    </html>'''

@app_api.route('/add')
def add():
    return "Here: We will add a user to a list object"

@app_api.route('/get-users')
def get_users():
    return "Here: We will get all users in our list object"

@app_api.route('/delete')
def delete():
    return "Here: We will delete a specific user from our list object"