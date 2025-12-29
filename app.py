from flask import Flask, render_template, redirect
from db_session import global_init, create_session
from forms.user import RegisterForm
from forms.jobs import JobForm
from forms.department import DepartmentForm
from models.user import User
from models.jobs import Jobs
from models.department import Department
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mars_secret_key'

global_init("mars_explorer.db")


@app.route("/")
def index():
    session = create_session()
    jobs = session.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session = create_session()
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,
            hashed_password=generate_password_hash(form.password.data)
        )
        session.add(user)
        session.commit()
        return redirect("/")
    return render_template("register.html", form=form)


@app.route("/add_job", methods=["GET", "POST"])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        session = create_session()
        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        session.add(job)
        session.commit()
        return redirect("/")
    return render_template("add_job.html", form=form)


@app.route("/add_department", methods=["GET", "POST"])
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        session = create_session()
        dep = Department(
            title=form.title.data,
            chief=form.chief.data,
            members=form.members.data,
            email=form.email.data
        )
        session.add(dep)
        session.commit()
        return redirect("/")
    return render_template("add_department.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
