from flask import Flask, render_template, request, redirect, url_for, flash
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.menu import MenuLink
from flask_admin.form.upload import ImageUploadField
from flask_admin.contrib.sqla import ModelView
import os
from dotenv import load_dotenv

load_dotenv()
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from config import Config
from models import db, User, About, Education, Experience, Project, Contact
from wtforms import PasswordField, validators, ValidationError

from flask_admin.contrib.sqla.validators import Unique
import re

# Patch Flask-Admin's Unique validator for WTForms 3.x compatibility
if hasattr(Unique, 'field_flags') and isinstance(Unique.field_flags, tuple):
    Unique.field_flags = {'unique': True}

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Secure Admin Views
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

def password_complexity_check(form, field):
    password = field.data
    if password:
        if len(password) < 10:
            raise ValidationError('Password must be at least 10 characters long.')
        if not any(c.isalpha() for c in password):
            raise ValidationError('Password must contain at least one letter.')
        if not any(c.isdigit() for c in password):
            raise ValidationError('Password must contain at least one number.')
        if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for c in password):
            raise ValidationError('Password must contain at least one special character.')

class UserView(MyModelView):
    column_exclude_list = ['password_hash']
    form_columns = ['username', 'password']

    form_extra_fields = {
        'password': PasswordField('Password', description='Password must be at least 10 characters long and contain letters, numbers, and special characters.', validators=[
            validators.Optional(), 
            password_complexity_check
        ])
    }



    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

class AboutView(MyModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

    form_overrides = {
        'profile_image': ImageUploadField
    }

    form_args = {
        'profile_image': {
            'label': 'Profile Image',
            'base_path': os.path.join(app.root_path, 'static', 'images'),
            'url_relative_path': 'images/',
            'allowed_extensions': ['jpg', 'jpeg', 'png', 'gif']
        }
    }

# Setup Flask-Admin
admin = Admin(app, name='Portfolio CMS', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_link(MenuLink(name='Back to Site', url='/'))
admin.add_view(AboutView(About, db.session))
admin.add_view(MyModelView(Education, db.session))
admin.add_view(MyModelView(Experience, db.session))
admin.add_view(MyModelView(Project, db.session))
admin.add_view(MyModelView(Contact, db.session))
admin.add_view(UserView(User, db.session)) # Allow managing users once logged in

@app.route('/')
def index():
    about = About.query.first()
    education = Education.query.order_by(Education.year_start.desc()).all()
    experience = Experience.query.order_by(Experience.year_start.desc()).all()
    projects = Project.query.all()
    projects = Project.query.all()
    form_endpoint = app.config.get('FORM_ENDPOINT')
    return render_template('index.html', about=about, education=education, experience=experience, projects=projects, form_endpoint=form_endpoint)

@app.route('/project/<int:project_id>.html')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return redirect(url_for('index', _anchor='contact'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        new_contact = Contact(name=name, email=email, message=message)
        try:
            db.session.add(new_contact)
            db.session.commit()
            flash('Message sent successfully!', 'success')
        except:
            flash('There was an issue sending your message.', 'danger')
        return redirect(url_for('index') + '#contact')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin.index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
