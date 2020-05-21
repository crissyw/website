from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Forcing a hard refresh of static assets to prevent caching while previewing builds
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Task %r>' % self.id

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/work')
def work():
	"""
	Images of YouTube videos: https://img.youtube.com/vi/<insert-youtube-video-id-here>/0.jpg
	Template for dict:
		'TITLE': {'url': 'LINK', 'file_path':'/static/images/portfolio/IMG.JPG'}
	"""
	work_content = {
		'How to Experiment with Product Improvements - Tech in Asia Singapore': {
			'url': 'https://www.youtube.com/watch?v=WRUSryfaxhk',
			'file_path':'/static/images/portfolio/youtube-tia-sg-2018.jpg'},
		'My Personal OKRs': {'url': 'https://medium.com/life-at-go-jek/personal-okrs-b10585010361', 'file_path':'/static/images/portfolio/medium-personal-okrs.jpeg'},
		'Gojek x Data Science Weekend': {'url': 'https://www.youtube.com/watch?v=mEzHlzPeFSw', 'file_path':'/static/images/portfolio/gojek-dsw.jpg'},
		'GoFigure: Gojek\'s Growth Dilemma': {'url': 'https://www.youtube.com/watch?v=YyNrgZSYY9c', 'file_path':'/static/images/portfolio/gofigure-podcast.jpg'},
		'BukaTalks: Big Data?': {'url': 'https://www.youtube.com/watch?v=3grep1OVyeg','file_path':'/static/images/portfolio/bukatalks.jpg'},
		'North Star Metrics': {'url': 'https://www.youtube.com/watch?v=WOcxmEWqI0c', 'file_path':'/static/images/portfolio/nsm.jpg'},
		'KrAsia: Women In Tech': {'url': 'https://kr-asia.com/crystal-widjaja-on-gojeks-growth-and-gender-diversity-in-it-women-in-tech', 'file_path':'/static/images/portfolio/krasia.jpeg'},
		'e27: Delivering 3M Martabaks in a Year': {'url': 'https://e27.co/go-jek-uses-data-business-intelligence-20170905/', 'file_path':'/static/images/portfolio/e27.jpg'}
		}
	return render_template('work.html', work_content=work_content)

@app.route('/test')
def test():
	if request.method == 'POST':
		#logic for task
		task_content = request.form['content']
		new_task = Todo(content=task_content)

		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue adding your task.'

	else:
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
	task_to_delete = Todo.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return 'There was a problem deleting your task'
	
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	task = Todo.query.get_or_404(id)

	if request.method == 'POST':
		task.content = request.form['content']
		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue updating your task.'
	else:
		return render_template('update.html',task=task)

def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)

if __name__ == "__main__":
	app.run(debug=True)