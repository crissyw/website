from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import os

app = Flask(__name__)

# Forcing a hard refresh of static assets to prevent caching while previewing builds
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about-crystal-widjaja')
def about():
	return render_template('about-crystal-widjaja.html')

@app.route('/reading_list')
def readingListReroute():
	return redirect("reading-list")

@app.route('/reading-list')
def readingList():
	management = {
		'Radical Candor — Kim Scott': {'url': 'https://amzn.to/3eObUr7', 'file_path':'static/images/reading-list/radicalcandor.jpg', 'book_summary':'This book really put into perspective my own management style, and helped me define and pick where along the spectrums of kindness and firmness I wanted to be. Great tips and scenarios to test yourself through!'},
		'The Hard Thing About Hard Things — Ben Horowitz': {'url': 'https://amzn.to/32KaBHu', 'file_path':'static/images/reading-list/hardthingabouthardthings.jpg', 'book_summary':'I\'ve gone back to this book for their checklists on how to hire a VP of Sales, how to fire, how to compensate and title, and so much more. Truly an executive\'s guidebook.'},
		'Crucial Conversations': {'url': 'https://amzn.to/39ifoBf', 'file_path':'static/images/reading-list/crucialconversations.jpg', 'book_summary':'Ever been in a situation where opinions differ and tensions are high? This book completely changed how I mediate product discussions like \"What is delight?\" If you feel like your conversations with teams go nowhere, Crucial Conversations are a great framework to start with.'}
	}

	enduring_company = {
		'High Growth Handbook — Elad Gil': {'url': 'https://amzn.to/39qDzNN', 'file_path':'static/images/reading-list/highgrowthhandbook.jpg', 'book_summary':'Elad has taught me a lot about what it means to be in a high growth business and has a genuine, rare sense of empathy that makes him an incredible guide throughout the journey. The book includes great guest features from people like Jerry Chen of Greylock and Claire Hughes Johnson from Stripe. There\'s practical advice too, like what PMs should be responsible for, how to build a recruitment org, and hiring for culture & values.'},
		'Measure What Matters — John Doerr': {'url': 'https://amzn.to/30QUeGD', 'file_path':'static/images/reading-list/measurewhatmatters.jpg', 'book_summary':'The book of OKRs. Enough said.'},
		'The Advantage: Why Organizational Health Trumps Everything Else In Business — Patrick Lencioni': {'url': 'https://amzn.to/30BcXWv', 'file_path':'static/images/reading-list/theadvantage.jpg', 'book_summary':'Another book about culture in theoretical practice. Reading this while working on your own organization\'s cultural mess can be cathartic in a way. My favorite quote: \'An organization knows that it has identified its core values correctly when it will allow itself to be punished for living those values and when it accepts the fact that employees will sometimes take those values too far. Core values are not a matter of convenience.\''},
		'High Output Management — Andy Grove': {'url': 'https://amzn.to/2Bqtkwu', 'file_path':'static/images/reading-list/highoutputmanagement.jpg', 'book_summary':'Andy introduced the concept of managerial leverage to me. It taught me to look for ways to make my teams perform at their best and highest potential. The concept of \'limiting steps\' applies not just to supply chain operations, but in product development, too.'},
		'Good to Great: Why Some Companies Make the Leap and Others Don\'t — Jim Collins': {'url': 'https://amzn.to/3ho6wwH', 'file_path':'static/images/reading-list/goodtogreat.jpg', 'book_summary':'The authors took a very statistical approach to evaluating the companies that are deemed \'great\' based on stock returns. If you\'re looking for something with more rigor and analysis, this is an interesting read on the effects of compounding good decisions, diligently executed.'},
		'Bad Blood: Secrets and Lies in a Silicon Valley Startup — John Carreyrou': {'url': 'https://amzn.to/3hugE7g', 'file_path':'static/images/reading-list/badblood.jpg', 'book_summary':'Well, this is what not to do.'}
	}

	user_empathy = {
		'The Creative Curve — Allen Gannett': {'url': 'https://amzn.to/2EairzS', 'file_path':'static/images/reading-list/thecreativecurve.jpg', 'book_summary':'Bahari, VP of Creative at Gojek, recommended this to me as his book of the year — and what a book. If you struggle with being traditionally or artistically creative, this book helps explain the process and shines a light on alternative creativity.'},
		'The Everything Store: Jeff Bezos and the Age of Amazon — Brad Stone': {'url': 'https://amzn.to/2CVoDen', 'file_path':'static/images/reading-list/theeverythingstore.jpg', 'book_summary':'I may not agree with all of Amazon\'s practices, but they completely win on customer obsession. The stories of how they practice customer obsession in practice are wild — things like wooden doors as tables, and keeping an empty seat open during meetings for the aforementioned customer.'},
		'Made to Stick: Why Some Ideas Survive and Others Die — Chip Heath & Dan Heath': {'url': 'https://amzn.to/2CCUwZp', 'file_path':'static/images/reading-list/madetostick.jpg', 'book_summary':'This book changed how I approach rhetoric, the art of speaking. If you\'re at a creative block, feel unoriginal, or just need ideas of how to tell your customers for the one millionth time what type of services you provide, Made to Stick has a great list of methods to start coming up with good ideas again.'},
		'Hacking Growth: How Today\'s Fastest-Growing Companies Drive Breakout Success — Sean Ellis & Morgan Brown': {'url': 'https://amzn.to/2BwySFM', 'file_path':'static/images/reading-list/hackinggrowth.jpg', 'book_summary':'Get templates on how to survey users about new features, strategies to compare cohorts, and practical guidance on how to use data to personalize user experiences.'}
	}

	data_literate = {
		'How Not to Be Wrong: The Power of Mathematical Thinking — Jordan Ellenberg': {'url': 'https://amzn.to/32LPJzE', 'file_path':'static/images/reading-list/hownottobewrong.jpg', 'book_summary':'I\'ve personally given several seminars on the contents of this book because it really does give you the basics of statistical thinking. If you want to become more intelligible and critical about the data your teams give you, this is a fantastic start.'},
		'Algorithms to Live By: The Computer Science of Human Decisions — Brian Christian & Tom Griffiths': {'url': 'https://amzn.to/2ZOmVob', 'file_path':'static/images/reading-list/algostoliveby.jpg', 'book_summary':'This is probably more targeted towards the geeks and nerds in all of us. If you ever wondered about how your systems fetch data or why lists load so slowly, this explains the conceptual approaches that computers take to retreive information in a way that is incredibly engaging.'},
		'Introduction to Probability and Statistics — MIT': {'url': 'https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/class-slides/', 'file_path':'static/images/reading-list/mit.png', 'book_summary':'At the end of the day, if you really want to be data literate, the best way is to formally study their foundations!'},
		'The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling — Ralph Kimball': {'url': 'https://amzn.to/32LZbmC', 'file_path':'static/images/reading-list/datawarehouse.jpeg', 'book_summary':'When I first joined Gojek, I read this book and kept it at my side for the entire first year of my career.'}
	}

	code_literate = {
		'Bitcoin and Cryptocurrency Technologies — Princeton University': {'url': 'https://www.coursera.org/learn/cryptocurrency/home/welcome', 'file_path':'static/images/reading-list/coursera-social-logo.png', 'book_summary':'Cryptocurrency could redefine how we think about value, wealth, and the systems that manufacture it. The content is pretty up-to-date until Week 5 which is where I would stop.'},
		'Dank Learning: Generating Memes Using Deep Neural Networks': {'url': 'https://arxiv.org/pdf/1806.04510.pdf', 'file_path':'https://github.com/alpv95/MemeProject/blob/master/Picture1.png?raw=true', 'book_summary':'Is this a joke? Well, yes, and no. The real joke is why nobody\'s done this sooner. An entertaining, but entirely academically sound read.'},
		'Real Programmers Don\'t Use PASCAL': {'url': 'https://www.ee.ryerson.ca/~elf/hack/realmen.html', 'file_path':'static/images/reading-list/pascal.png', 'book_summary':'I mean, they can\'t possibly use Rust.'},
		'What is code? — Paul Ford': {'url': 'https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/', 'file_path':'static/images/reading-list/whatiscode.png', 'book_summary':'An interactive, free way to play around with virtual boards.'},
		'Learn SQL on W3 Schools': {'url': 'https://www.w3schools.com/sql/', 'file_path':'static/images/logo.png', 'book_summary':'My first interaction with code was through SQL. By knowing where data is coming from, how it is populated, and how it can be used, you will absolutely become a better programmer (or at least know how to talk to programmers).'}
	}

	return render_template('reading-list.html',management=management,user_empathy=user_empathy,enduring_company=enduring_company,data_literate=data_literate,code_literate=code_literate)

@app.route('/work')
def work():
	"""
	Images of YouTube videos: https://img.youtube.com/vi/<insert-youtube-video-id-here>/0.jpg
	Template for dict:
		'TITLE': {'url': 'LINK', 'file_path':'/static/images/portfolio/IMG.JPG'}
	"""
	work_content = {
		'Why Most Analytics Efforts Fail': {'url': 'https://www.reforge.com/blog/why-most-analytics-efforts-fail', 'file_path':'/static/images/portfolio/reforge.png'},
		'Future of Startup: The Prophecy of Crystal Widjaja — Nyaman Di Sosmed': {'url': 'https://open.spotify.com/episode/50cnuRUtvAbfCLzKSt6PkJ', 'file_path':'/static/images/portfolio/nyamandisosmed.png'},
		'Empowering Women and Underrepresented Groups in Tech — Ngobrolin Startup & Teknologi': {'url': 'https://open.spotify.com/episode/6B2V8KEklV7JuhS6h9ta7p?si=clt7NkadRfezGvzBWdZVWA', 'file_path':'/static/images/portfolio/empoweringwomen.jpeg'},
		'How to Experiment with Product Improvements - Tech in Asia Singapore': {
			'url': 'https://www.youtube.com/watch?v=WRUSryfaxhk',
			'file_path':'/static/images/portfolio/youtube-tia-sg-2018.jpg'},
		'Forbes Indonesia: 30 Under 30': {'url': 'https://www.instagram.com/p/BuTKjF0BSX6/', 'file_path':'/static/images/portfolio/forbes30under30.png'},
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
		'e27: Delivering 3M Martabaks in a Year - How Gojek Uses Data': {'url': 'https://e27.co/go-jek-uses-data-business-intelligence-20170905/', 'file_path':'/static/images/portfolio/e27.jpg'},
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