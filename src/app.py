from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models.task import Task

app = Flask(__name__)

TASKS = []


@app.route('/')
def index():

    return render_template(
        'index.html',
        tasks=TASKS
    )


@app.route('/create', methods=['GET','POST'])
def create_task():

    if request.method == 'POST':

        title = request.form['title']

        description = request.form['description']

        priority = request.form['priority']

        task = Task(
            title,
            description,
            priority
        )

        TASKS.append(task)

        return redirect(
            url_for('index')
        )

    return render_template(
        'create.html'
    )


@app.route('/delete/<int:index>')
def delete_task(index):

    if 0 <= index < len(TASKS):

        TASKS.pop(index)

    return redirect(
        url_for('index')
    )


@app.route('/edit/<int:index>', methods=['GET','POST'])
def edit_task(index):

    task = TASKS[index]

    if request.method == 'POST':

        task.title = request.form['title']

        task.description = request.form['description']

        task.priority = request.form['priority']

        task.status = request.form['status']

        return redirect(
            url_for('index')
        )

    return render_template(
        'edit.html',
        task=task
    )


if __name__ == '__main__':

    app.run(
        debug=True
    )