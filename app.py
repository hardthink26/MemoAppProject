from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment 
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
moment = Moment(app)


class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        memo = Memo(title=title, content=content, created_at=datetime.utcnow(),)
        db.session.add(memo)
        db.session.commit()
    memos = Memo.query.order_by(Memo.id).all()
    return render_template("index.html", memos=memos) 


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    memo = Memo.query.get_or_404(id)
    if request.method == "POST":
        memo.title = request.form.get("title", "")
        memo.content = request.form.get("content", "")
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", memo=memo)


@app.route("/delete/<int:id>")
def delete(id):
    memo = Memo.query.get_or_404(id)
    db.session.delete(memo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

