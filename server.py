##Alec Davidson - Summer 2014
import flask, flask.views, os, dnd_main

app = flask.Flask(__name__)

app.secret_key = "GenericKey"  # figure out how to hide this or something idk probs not important for this project

class View(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		party = flask.request.form['party']
		reroll = flask.request.form['reroll']
		fate = flask.request.form['fate']
		dnd_main.start(party, reroll, fate)
		return self.get()
  
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])


