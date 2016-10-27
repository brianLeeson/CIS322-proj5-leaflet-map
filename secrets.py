import flask

app = flask.Flask(__name__)

API_KEY = 'tJlzGsSGdYSIkkEn8oXTll8GumKoLGN5'


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    with open("poi.txt") as poi:
        places = poi.readlines()
    for i in range(len(places)):
        split_place = places[i].split(',')
        places[i] = split_place
    return flask.render_template('index.html', secret_key=API_KEY, places=places)

@app.errorhandler(404)
def error_404(e):
  app.logger.warning("++ 404 error: {}".format(e))
  return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert app.debug == False #  I want to invoke the debugger
    return flask.render_template('500.html'), 500

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
