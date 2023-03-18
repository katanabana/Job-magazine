from flask import Flask, render_template
from data.jobs import Jobs
from data.users import User
from data.db_session import global_init, create_session

app = Flask(__name__)


@app.route('/')
def f():
    global_init('db/database.db')
    session = create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User.id, User.name, User.surname).all()
    names = {}
    for id, name, surname in users:
        names[id] = (name, surname)
    return render_template('index.html', jobs=jobs, names=names)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
