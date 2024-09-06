from flask import render_template, redirect, url_for
from app.auth import auth_bp

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/signup')
def signup():
    return render_template('auth/signup.html')
