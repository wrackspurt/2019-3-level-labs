from flask import Flask, render_template
import json
from requests_prep_kis_yu import base_url, jpath, get_html_page, find_articles, publish_report


app = Flask(__name__)


@app.route('/', methods=['GET'])
def habr_articles():
    publish_report(jpath, find_articles(get_html_page(base_url)))
    with open(jpath, 'r', encoding='utf-8') as fl:
        dtitles = json.load(fl)
        return render_template('index.html', habr_articles=dtitles['articles'], habr_url=dtitles)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
