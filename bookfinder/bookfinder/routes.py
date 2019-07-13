from flask import render_template, request
from bookfinder import app, db
from bookfinder.models import books

@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html")



@app.route('/search', methods=['GET'])
def search():
	if request.method == "GET":
		query = request.args.get('query')
		result_by_title = books.query.filter(books.title.like('%' + query + '%')).all()
		result_by_writer = (books.query.filter(books.writer.like('%' + query + '%')).all())
		result_by_subject = (books.query.filter(books.subject.like('%' + query + '%')).all())
		result = result_by_writer + result_by_subject + result_by_title
		result = list(set(result))
                                
		return render_template("search.html", results=result)


@app.route('/admin', methods=['GET', 'POST'])
def addbook():
	if request.method == "POST":
		title = request.form['title']
		writer = request.form['writer']
		subject = request.form['subject']
		edition = request.form['edition']
		if writer == '':
			writer = '-'
		if subject == '':
			subject = '-'
		if edition == '':
			edition = '-'
		entry = books(title=title, writer=writer, subject=subject, edition=edition)
		db.session.add(entry)
		db.session.commit()


	return render_template("add_books.html", title="Add Books")
