"""
Very simple Flask web site, with one page
displaying a course schedule.

"""

import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging

# Our own module 
import process_POI

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG

app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.secret_key  # Should allow using session variables

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
  app.logger.debug("Main page entry")
  flask.session["points"] = process_POI.process()
  
  return flask.render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    #flask.session['linkback'] =  flask.url_for("/")
    #flask.session['linkback'] =  flask.url_for("/")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers 
#   These return JSON, rather than rendering pages. 
#
###############
'''
@app.route("/_calc_times")
def _calc_times():
  """
  returns datasctructure that contains the POIs
  """
  app.logger.debug("Got a JSON request");
  
  #Get args
  km = request.args.get('km', 0, type=float)
  distance = request.args.get('distance', 0, type=float)
  date = request.args.get('date', 0, type=str)
  time = request.args.get('time', 0, type=str)
  
  #format date_time
  date_time = date + ' ' + time + ':00' 
  arrow_time = arrow.get(date_time, 'YYYY-MM-DD HH:mm:ss')
  
  open_time = acp_times.open_time(km, distance, arrow_time.isoformat())
  close_time = acp_times.close_time(km, distance, arrow_time.isoformat())
  result={ "open": open_time, "close": close_time }
  
  return jsonify(result=result)
'''


#############

if __name__ == "__main__":
    # Standalone. 
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server, 
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service.
    app.debug=False

