from flask import Flask
from __main__ import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/user/addcity', methods=['GET'])
def addcity():
  return User().addcity()

@app.route('/user/removecity', methods=['GET'])
def removecity():
  return User().removecity()