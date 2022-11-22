from flask import Flask, render_template, request, session
from analytics.models import Analytics
from __main__ import app
from app import login_required
from bson.json_util import dumps, loads

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/analytics', methods=['GET'])
@login_required
def get():
  data = Analytics().get()
  # return render_template('dashboard.html', data=data)
  return data

@app.route('/analytics/<parameter>', methods=['GET'])
@login_required
def get_aqi_for_user_cities(parameter):
  if parameter not in ["aqi", "co", "dew", "h", "no2", "o3", "p", "pm10", "pm25","t", "w"]:
    return None
  cities = session['user']['cities']
  response = []
  if not cities or len(cities)==0:
    return None

  for city in cities:
    city_data = Analytics().get_latest_data(city)
    response.append({"city": city_data["city"].capitalize(), parameter: city_data.get(parameter)})
  return response


@app.route('/dashboard/', methods=['GET'])
@login_required
def display():
  return render_template('graph.html')
