##Alec Davidson - Summer 2014
import flask, flask.views, os, dnd_main

app = flask.Flask(__name__)

app.secret_key = "CorrectTurtleBatteryStaple"

class View(flask.views.MethodView):
  def get(self):
    return flask.render_template('index.html')
  
  def post(self):
	party = str(flask.request.form['party'])
	reroll = str(flask.request.form['reroll'])

	dnd_main.start(party,reroll)
	return self.get()
  
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])

port = int(os.environ.get('PORT', 5000))

app.run(host='0.0.0.0', port=port)

