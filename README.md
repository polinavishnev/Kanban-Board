# Flask Kanban Board
A simple Kanban board for keeping track of task status (to do, doing, or done) and date.

## Features

- Add new tasks, with due dates.
- Change task statuses between to-do, doing and done.
- Delete tasks.

## Installation

Set up a virtual environment.

### Windows

    $ python3 -m venv venv venv\Scripts\activate.bat

### Mac/Linux
    
    $ python3 -m venv venv
    $ source venv/bin/activate

Install the necessary dependencies.

    $ pip3 install -r requirements.txt

Run the app.

    $ python3 app.py

The Kanban board will be run on http://127.0.0.1:5000/

## Testing

Run the following command to run the tests.

    $ python3 -m unittest discover test

## Directory pathways

Root directory:
`app.py` - The main file that runs the app.
`README.md` - The file describing the app.
`requirements.txt` - The dependencies for the app.
`test` - The directory that contains the tests.

`app` - The directory that contains the app.
`app/__init__.py` - The file that initializes the app.
`app/kanban_db.py` - The file that contains the database setup for the app.
`app/kanban_routing.py` - The file that contains the routes for the app.

`app/templates` - The directory that contains the HTML for the app.

`app/templates/index.html` - The HTML for the Kanban board.