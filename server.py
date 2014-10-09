##Alec Davidson - Summer 2014
import flask, flask.views, os, dnd_main

app = flask.Flask(__name__)

class View(flask.views.MethodView):
  def get(self):
    return flask.render_template('index.html')
  
  @property
  def post(self):
    party = str(flask.request.form['party'])
    reroll = str(flask.request.form['reroll'])

    dnd_main.start(party, reroll)
    return self.get()
  
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])


