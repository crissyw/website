from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import os

app = Flask(__name__)

# Forcing a hard refresh of static assets to prevent caching while previewing builds
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/reading_list')
def readingList():
	management = {
		'Radical Candor — Kim Scott': {'url': 'https://amzn.to/3eObUr7', 'file_path':'static/images/reading-list/radicalcandor.jpg'},
		'The Hard Thing About Hard Things — Ben Horowitz': {'url': 'https://amzn.to/32KaBHu', 'file_path':'static/images/reading-list/hardthingabouthardthings.jpg'},
		'Crucial Conversations': {'url': 'https://amzn.to/39ifoBf', 'file_path':'static/images/reading-list/crucialconversations.jpg'}
	}

	enduring_company = {
		'High Growth Handbook — Elad Gil': {'url': 'https://amzn.to/39qDzNN', 'file_path':'static/images/reading-list/highgrowthhandbook.jpg'},
		'Measure What Matters — John Doerr': {'url': 'https://amzn.to/30QUeGD', 'file_path':'static/images/reading-list/measurewhatmatters.jpg'},
		'The Advantage: Why Organizational Health Trumps Everything Else In Business — Patrick Lencioni': {'url': 'https://amzn.to/30BcXWv', 'file_path':'static/images/reading-list/theadvantage.jpg'},
		'High Output Management — Andy Grove': {'url': 'https://amzn.to/2Bqtkwu', 'file_path':'static/images/reading-list/highoutputmanagement.jpg'},
		'Good to Great: Why Some Companies Make the Leap and Others Don\'t — Jim Collins': {'url': 'https://amzn.to/3ho6wwH', 'file_path':'static/images/reading-list/goodtogreat.jpg'},
		'Bad Blood: Secrets and Lies in a Silicon Valley Startup — John Carreyrou': {'url': 'https://amzn.to/3hugE7g', 'file_path':'static/images/reading-list/badblood.jpg'}
	}

	user_empathy = {
		'The Creative Curve — Allen Gannett': {'url': 'https://amzn.to/2EairzS', 'file_path':'static/images/reading-list/thecreativecurve.jpg'},
		'The Everything Store: Jeff Bezos and the Age of Amazon — Brad Stone': {'url': 'https://amzn.to/2CVoDen', 'file_path':'static/images/reading-list/theeverythingstore.jpg'},
		'Made to Stick: Why Some Ideas Survive and Others Die — Chip Heath & Dan Heath': {'url': 'https://amzn.to/2CCUwZp', 'file_path':'static/images/reading-list/madetostick.jpg'}
	}

	data_literate = {
		'How Not to Be Wrong: The Power of Mathematical Thinking — Jordan Ellenberg': {'url': 'https://amzn.to/32LPJzE', 'file_path':'static/images/reading-list/hownottobewrong.jpg'},
		'Algorithms to Live By: The Computer Science of Human Decisions — Brian Christian & Tom Griffiths': {'url': 'https://amzn.to/2ZOmVob', 'file_path':'static/images/reading-list/algostoliveby.jpg'},
		'Introduction to Probability and Statistics — MIT': {'url': 'https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/class-slides/', 'file_path':'static/images/reading-list/mit.png'},
		'The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling — Ralph Kimball': {'url': 'https://amzn.to/32LZbmC', 'file_path':'static/images/reading-list/datawarehouse.jpeg'}
	}

	code_literate = {
		'Bitcoin and Cryptocurrency Technologies (stop at W5) — Princeton University': {'url': 'https://www.coursera.org/learn/cryptocurrency/home/welcome', 'file_path':'static/images/reading-list/coursera-social-logo.png'},
		'Dank Learning: Generating Memes Using Deep Neural Networks': {'url': 'https://arxiv.org/pdf/1806.04510.pdf', 'file_path':'https://github.com/alpv95/MemeProject/blob/master/Picture1.png?raw=true'},
		'Real Programmers Don\'t Use PASCAL': {'url': 'https://www.ee.ryerson.ca/~elf/hack/realmen.html', 'file_path':'static/images/reading-list/pascal.png'},
		'What is code? — Paul Ford': {'url': 'https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/', 'file_path':'static/images/reading-list/whatiscode.png'},
		'Learn SQL on W3 Schools': {'url': 'https://www.w3schools.com/sql/', 'file_path':'static/images/logo.png'}
	}

	return render_template('reading_list.html',management=management,user_empathy=user_empathy,enduring_company=enduring_company,data_literate=data_literate,code_literate=code_literate)

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
		'Forbes Indonesia: 30Under30': {'url': 'https://www.instagram.com/p/BuTKjF0BSX6/', 'file_path':'/static/images/portfolio/forbes30under30.png'},
		'General Electric: Women in STEM': {'url': 'https://www.ge.com/reports/56858-2/', 'file_path':'/static/images/portfolio/ge-womeninstem.png'},
		'My Personal OKRs': {'url': 'https://medium.com/life-at-go-jek/personal-okrs-b10585010361', 'file_path':'/static/images/portfolio/medium-personal-okrs.jpeg'},
		'Globe Asia: A Passion for Big Data': {'url': 'https://www.globeasia.com/cover-story/a-passion-for-big-data/', 'file_path':'/static/images/portfolio/globeasia.jpg'},
		'Gojek x Data Science Weekend': {'url': 'https://www.youtube.com/watch?v=mEzHlzPeFSw', 'file_path':'/static/images/portfolio/gojek-dsw.jpg'},
		'GoFigure: Gojek\'s Growth Dilemma': {'url': 'https://www.youtube.com/watch?v=YyNrgZSYY9c', 'file_path':'/static/images/portfolio/gofigure-podcast.jpg'},
		'Techsauce 2019: How Unicorns Use Data': {'url': 'https://www.facebook.com/ritu.marya/videos/10158319083299237/', 'file_path':'/static/images/portfolio/techsauce-entrepreneur.png'},
		'Mencari Cara Kerja Lebih Pintar': {'url': 'https://mediaindonesia.com/read/detail/277888-mencari-cara-kerja-lebih-pintar.html', 'file_path':'/static/images/portfolio/crystal-widjaja-mencari-cara-media-indonesia.jpg'},
		'BukaTalks: Big Data?': {'url': 'https://www.youtube.com/watch?v=3grep1OVyeg','file_path':'/static/images/portfolio/bukatalks.jpg'},
		'North Star Metrics': {'url': 'https://www.youtube.com/watch?v=WOcxmEWqI0c', 'file_path':'/static/images/portfolio/nsm.jpg'},
		'KrAsia: Women In Tech': {'url': 'https://kr-asia.com/crystal-widjaja-on-gojeks-growth-and-gender-diversity-in-it-women-in-tech', 'file_path':'/static/images/portfolio/krasia.jpeg'},
		'e27: Delivering 3M Martabaks in a Year': {'url': 'https://e27.co/go-jek-uses-data-business-intelligence-20170905/', 'file_path':'/static/images/portfolio/e27.jpg'},
		'Angin Spotlight': {'url': 'https://www.angin.id/2018/04/12/crystal-widjaja', 'file_path':'/static/images/portfolio/angin.jpg'},
		'Metabase Case Study': {'url': 'https://www.metabase.com/case_studies/go-jek/', 'file_path':'/static/images/portfolio/metabase.png'},
		'Go-Fast: The Data Behind Ramadan': {'url': 'https://blog.gojekengineering.com/go-fast-the-data-behind-ramadan-38037953561b', 'file_path':'/static/images/portfolio/gofast.jpeg'}
		}
	return render_template('work.html', work_content=work_content)

@app.route('/actualtest')
def actualtest():
	return render_template('index.html')

def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)

if __name__ == "__main__":
	app.run(debug=True)