import os
import secrets

from flask import Flask, render_template, request, redirect, url_for, session

from config import config
from extensions import bootstrap, db, moment
from models import Memo, local_now


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memos.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    from auth import auth_bp

    app.register_blueprint(auth_bp)

    return app


app = create_app()

with app.app_context():
    db.create_all()


@app.route("/memos", methods=["GET", "POST"])
def index():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        now = local_now()
        memo = Memo(title=title, content=content, created_at=now, updated_at=now)
        db.session.add(memo)
        db.session.commit()
    memos = Memo.query.order_by(Memo.created_at.desc(), Memo.id.desc()).all()
    return render_template("index.html", memos=memos)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "username" not in session:
        return redirect(url_for("auth.login"))
    memo = Memo.query.get_or_404(id)
    if request.method == "POST":
        memo.title = request.form.get("title", "")
        memo.content = request.form.get("content", "")
        memo.updated_at = local_now()
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", memo=memo)


@app.route("/delete/<int:id>")
def delete(id):
    if "username" not in session:
        return redirect(url_for("auth.login"))
    memo = Memo.query.get_or_404(id)
    db.session.delete(memo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
