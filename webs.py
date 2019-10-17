from flask import Flask, render_template, redirect, url_for
import json
from requests_prep_kis_yu import base_url, jpath, get_html_page, find_articles, publish_report


app = Flask(__name__)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.route('/', methods=['GET'])
def habr_articles():
    publish_report(jpath, find_articles(get_html_page(base_url)))
    with open(jpath, 'r', encoding='utf-8') as fl:
        dtitles = json.load(fl)
        return render_template('index.html', habr_articles=dtitles['articles'], habr_url=dtitles)


@app.route('/update_page', methods=['POST'])
def update_page():
    return redirect(url_for('habr_articles'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
