from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password'),
      "cities": []
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Invalid login credentials" }), 401

  def addcity(self):
    city = request.args.get('city')
    if not city:
      return jsonify({ "error": "Fill City Name" }), 400
    city = city.lower()
    if city in session['user']['cities']:
      return jsonify({ "error": "City Already Present" }), 401
    user = db.users.find_one_and_update({'_id': session['user']['_id']}, {'$push': {'cities': city}})
    if user:
      session['user'] = user
      return jsonify({ "success": "City Added Successfully" }), 200
    return jsonify({ "error": "Adding city failed" }), 400

  def removecity(self):
    city = request.args.get('city')
    if not city:
      return jsonify({ "error": "Fill City Name" }), 400
    city = city.lower()
    if city not in session['user']['cities']:
      return jsonify({ "error": "You don't have this city added" }), 401
    user = db.users.find_one_and_update({'_id': session['user']['_id']}, {'$pull': {'cities': city}})
    if user:
      session['user'] = user
      return jsonify({ "success": "City Removed Successfully" }), 200
    return jsonify({ "error": "Removing city failed" }), 400