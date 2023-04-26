from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "dwffniwnn253632niwn2SkoC"

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


with app.app_context():
    class Users(UserMixin, db.Model):
        __tablename__ = "users"
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String, nullable=False)
        password = db.Column(db.String, nullable=False)

        tasks_active = relationship("ActiveTasks", back_populates="active")
        tasks_completed = relationship("CompletedTasks", back_populates="completed")


    db.create_all()


    class ActiveTasks(db.Model):
        __tablename__ = "active_tasks"
        id = db.Column(db.Integer, primary_key=True)
        deadline = db.Column(db.String, nullable=False)
        title = db.Column(db.String, nullable=False)
        description = db.Column(db.String, nullable=False)
        priority = db.Column(db.String, nullable=False)

        user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
        active = relationship("Users", back_populates="tasks_active")


    db.create_all()


    class CompletedTasks(db.Model):
        __tablename__ = "completed_tasks"
        id = db.Column(db.Integer, primary_key=True)
        deadline = db.Column(db.String, nullable=False)
        title = db.Column(db.String, nullable=False)
        description = db.Column(db.String, nullable=False)
        priority = db.Column(db.String, nullable=False)

        user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
        completed = relationship("Users", back_populates="tasks_completed")


    db.create_all()


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("active_tasks"))
    else:
        form = LoginForm()
        if request.method == "POST":
            email = request.form.get("email")
            user = Users.query.filter_by(email=email).first()
            if user:
                password = request.form.get("password")
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for("active_tasks"))
                else:
                    flash("Incorrect password, please try again")
            else:
                flash("We don't have a user associated with this email, please register.")
                return redirect(url_for("login"))
        return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        email = request.form.get("email")
        user = Users.query.filter_by(email=email).first()
        if user:
            flash("You've already registered with this email address, Please login.")
            return redirect(url_for('login'))
        else:
            hashed_and_salted_pw = generate_password_hash(
                password=request.form.get("password"),
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = Users(
                email=request.form.get("email"),
                password=hashed_and_salted_pw
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('active_tasks'))
    return render_template("register.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=["GET", "POST"])
def add_task():
    if current_user.is_authenticated:
        if request.method == "POST":
            deadline = request.form.get('deadline')
            title = request.form.get('title')
            description = request.form.get('description')
            priority = request.form.get('priority')
            new_task_active = ActiveTasks(
                deadline=deadline,
                title=title,
                description=description,
                priority=priority,
                user_id=current_user.id
            )
            db.session.add(new_task_active)
            db.session.commit()
            return redirect(url_for('active_tasks'))
        return render_template('add-task.html')
    else:
        return redirect(url_for('login'))


@app.route("/active_tasks", methods=["GET", "POST"])
def active_tasks():
    if current_user.is_authenticated:
        all_tasks = ActiveTasks.query.filter_by(user_id=current_user.id).all()
        status = 'active'
        return render_template("active.html", active_tasks=all_tasks, task_status=status)
    else:
        return redirect(url_for('login'))


@app.route("/completed_tasks", methods=["GET", "POST"])
def completed_tasks():
    all_tasks = CompletedTasks.query.filter_by(user_id=current_user.id).all()
    status = "completed"
    return render_template("complete.html", completed_tasks=all_tasks, task_status=status)


@app.route('/delete/<id>/<status>', methods=["GET", "POST"])
def delete_task(id, status):
    if status == "active":
        ActiveTasks.query.filter_by(id=id, user_id=current_user.id).delete()
        db.session.commit()
        return redirect(url_for("active_tasks"))
    elif status == "completed":
        CompletedTasks.query.filter_by(id=id, user_id=current_user.id).delete()
        db.session.commit()
        return redirect(url_for("completed_tasks"))
    else:
        pass


@app.route("/<id>/", methods=["GET", "POST"])
def set_active(id):
    task_to_send = CompletedTasks.query.filter_by(id=id, user_id=current_user.id).first()
    new_active_task = ActiveTasks(
        deadline=task_to_send.deadline,
        title=task_to_send.title,
        description=task_to_send.description,
        priority=task_to_send.priority,
        user_id=current_user.id
    )
    db.session.add(new_active_task)
    db.session.commit()

    CompletedTasks.query.filter_by(id=id, user_id=current_user.id).delete()
    db.session.commit()
    return redirect(url_for('active_tasks'))


@app.route("/<id>", methods=["GET", "POST"])
def complete_task(id):
    current_task = ActiveTasks.query.filter_by(id=id).first()
    if current_task:
        new_completed = CompletedTasks(
            deadline=current_task.deadline,
            title=current_task.title,
            description=current_task.description,
            priority=current_task.priority,
            user_id=current_user.id
        )
        db.session.add(new_completed)
        ActiveTasks.query.filter_by(id=id, user_id=current_user.id).delete()
        db.session.commit()
        return redirect(url_for('active_tasks'))
    return redirect(url_for('active_tasks'))


def check_user(id, status):
    if status == 'active':
        task_to_change = ActiveTasks.query.filter_by(id=id).first()
        if task_to_change.user_id != current_user.id:
            print("Unauthorised attempt by User")
            abort(403)
    if status == 'completed':
        task_to_change = CompletedTasks.query.filter_by(id=id).first()
        if task_to_change.user_id != current_user.id:
            print("Unauthorised attempt by User")
            abort(403)


@app.route("/edit_task/<id>/<status>", methods=["GET", "POST"])
def edit_task_page(id, status):
    check_user(id, status)
    if status == 'active':
        send_status = 'active'
        current_active_task = ActiveTasks.query.filter_by(id=id, user_id=current_user.id).first()
        return render_template('edit_page.html', id=id, status=send_status, task=current_active_task)
    elif status == 'completed':
        send_status = 'completed'
        current_completed_task = CompletedTasks.query.filter_by(id=id, user_id=current_user.id).first()
        return render_template('edit_page.html', id=id, status=send_status, task=current_completed_task)


@app.route("/edit_current_task/<id>/<status>", methods=["GET", "POST"])
def edit_current_task(id, status):
    if request.method == "POST":
        if status == 'active':
            current_task = ActiveTasks.query.filter_by(id=id, user_id=current_user.id).first()
            if request.method == "POST":
                current_task.deadline = request.form.get('deadline')
                current_task.title = request.form.get('title')
                current_task.description = request.form.get('description')
                current_task.priority = request.form.get('priority')
                db.session.commit()
                return redirect(url_for('active_tasks'))
        elif status == 'completed':
            current_task = CompletedTasks.query.filter_by(id=id, user_id=current_user.id).first()
            if request.method == 'POST':
                current_task.deadline = request.form.get('deadline')
                current_task.title = request.form.get('title')
                current_task.description = request.form.get('description')
                current_task.priority = request.form.get('priority')
                db.session.commit()
                return redirect(url_for('completed_tasks'))
    else:
        return redirect(url_for('active_tasks'))


if __name__ == "__main__":
    app.run(debug=True)
