from multiprocessing.spawn import import_main_path
from flask import Blueprint, redirect, render_template, request
from extensions import db
from models import Urls

main = Blueprint('main', __name__)


@main.route('/')
def Main():
    return render_template('index.html')


@main.route('/<short_url>')
def RedirectToUrl(short_url):
    link = Urls.query.filter_by(short=short_url).first_or_404()
    link.views += 1

    db.session.commit()
    return redirect(link.long)


@main.route('/addLink', methods=['POST'])
def AddLink():
    long = request.form['longUrl']
    link = Urls(long=long)
    db.session.add(link)
    db.session.commit()

    return render_template('addLink.html', long=link.long, short=link.short)


@main.before_request
def beforeRequest():
    db.create_all()
