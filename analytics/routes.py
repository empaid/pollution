from flask import Flask, render_template
from __main__ import app
from analytics.models import Analytics
from app import login_required


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

@app.route('/display', methods=['GET'])
@login_required
def display():
  bar_labels=labels
  bar_values=values
  return render_template('graph.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)
