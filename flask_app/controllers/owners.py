from flask_app import app
from flask import Flask, redirect, render_template, session, request

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/owners/new')
def new_owner():
  return render_template('create_owner.html')