from bookfinder import db

class books(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	writer = db.Column(db.String(100), nullable=True)
	subject = db.Column(db.String(100), nullable=True)
	edition = db.Column(db.String(40), nullable=True)

	def __repr__(self):
		return f"Book('{self.title}', '{self.writer}', '{self.edition}')"