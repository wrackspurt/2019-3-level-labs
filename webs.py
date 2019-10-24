from flask import Flask, render_template, redirect, url_for, request
import json
from requests_prep_kis_yu import base_url, jpath, get_html_page, find_articles, publish_report, find_another_articles, \
    another_url


app = Flask(__name__)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.route('/', methods=['GET', 'POST'])
def choose_source():
    publish_report(jpath, find_articles(get_html_page(base_url)), find_another_articles(get_html_page(another_url)))
    with open(jpath, 'r', encoding='utf-8') as fl:
        dtitles = json.load(fl)
    sources = ["habr", "ars technica"]
    if request.method == 'POST':
        source = request.form.get('sources')
        if source == 'habr':
            return redirect(url_for('post_habr_articles'))
        elif source == 'ars technica':
            return redirect(url_for('post_ars_articles'))
    return render_template('dropdown.html', date=dtitles['creationDate'], sources=sources)


@app.route('/habr_articles', methods=['GET', 'POST'])
def post_habr_articles():
    publish_report(jpath, find_articles(get_html_page(base_url)), find_another_articles(get_html_page(another_url)))
    with open(jpath, 'r', encoding='utf-8') as fl:
        dtitles = json.load(fl)
    return render_template('habr_articles.html', date=dtitles['creationDate'], habr_url=dtitles['habrUrl'],
                           habr_articles=dtitles['habrArticles'])


@app.route('/ars_articles', methods=['GET', 'POST'])
def post_ars_articles():
    publish_report(jpath, find_articles(get_html_page(base_url)), find_another_articles(get_html_page(another_url)))
    with open(jpath, 'r', encoding='utf-8') as fl:
        dtitles = json.load(fl)
    return render_template('ars_articles.html', date=dtitles['creationDate'], ars_url=dtitles['arsUrl'],
                           ars_articles=dtitles['arsArticles'])


@app.route('/update_habr', methods=['POST'])
def update_habr_articles():
    return redirect(url_for('post_habr_articles'))


@app.route('/update_ars', methods=['POST'])
def update_ars_articles():
    return redirect(url_for('post_ars_articles'))


@app.route('/back', methods=['POST'])
def back_to_start():
    return redirect(url_for('choose_source'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
