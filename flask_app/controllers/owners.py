from flask_app import app
from flask import Flask, redirect, render_template, session, request
from ..models import owner

@app.route('/')
def index():
  return render_template('index.html', all_owners = owner.Owner.get_all_owners())

@app.route('/owners/new')
def new_owner():
  return render_template('create_owner.html')