from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User
from .forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))  # Redirect to your main page or dashboard
        else:
            flash('Login failed. Check your email and/or password.', 'danger')
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    # Add logic to handle logout, e.g., clearing session data
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

