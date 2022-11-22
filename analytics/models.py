from flask import Flask, jsonify, request, session, redirect
from bson import json_util
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
import json
from bson.json_util import dumps, loads
from __main__ import app


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class Analytics:  
  def get(self):
    analytics = list(db.analytics.find({
      "city": request.args.get('city')
    }))
    print(len(analytics))
    print(type(analytics[0]))
    # data = loads(dumps(analytics))
    # print(type(data))
    return dumps(analytics)

  def get_latest_data(self, city):
    analytics = db.analytics.find_one({
      "city": city
    }, sort = [("timestamp", -1)]);
    return analytics