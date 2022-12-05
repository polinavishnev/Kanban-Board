from app import db, app
from flask import Flask, render_template, request, redirect, url_for, abort
from .kanban_db import Task
from datetime import datetime


@app.route('/')
def index():
    print('index')
    tasks = db.session.query(Task)
    to_do, doing, done = [],[],[]
    for task in tasks:
        if task.status == 'to_do':
            to_do.append(task)
        elif task.status == 'doing':
            doing.append(task)
        elif task.status == 'done':
            done.append(task)

    to_do.sort(key=lambda t: t.date)
    doing.sort(key=lambda t: t.date)
    done.sort(key=lambda t: t.date)

    return render_template('index.html', to_do=to_do, doing=doing, done=done)


def valid_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

    if date.strftime('%Y-%m-%d') != date:
        return False

    if datetime.strptime(date, '%Y-%m-%d') < datetime.now():
        return False

    if int(datetime.date[0:2]) > 20:
        return False

    # check if date is in correct format
    if date.strftime('%Y-%m-%d') != date:
        return False



    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        return False


@app.route('/add', methods=['POST'])
def add():
    requested_date = request.form['date']
    if valid_date(requested_date):
        to_do = Task(
            task=request.form['task'],
            status='to_do',
            date=datetime.strptime(requested_date, '%Y-%m-%d')
        )
        db.session.add(to_do)
        db.session.commit()
    else:
        return 'Invalid input. Please try again.'
    return redirect(url_for('index'))


@app.route('/task/<id>/<status>')
def change_status(id,status):
    task = db.session.query(Task).filter(Task.id==int(id)).first()
    if not task:
        abort(404)
    task.status = status
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/task/<id>', methods=['GET', 'POST', 'DELETE'])
def delete(id):
    task = db.session.query(Task).filter(Task.id==int(id)).first()
    if not task:
        abort(404)

    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

#
if __name__ == '__main__':
    app.run(debug=True)