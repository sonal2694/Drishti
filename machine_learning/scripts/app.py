from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

import NewsScraper
import NewsTextCleaner
import NewsSentiment
import LivePredict

import json

app = Flask(__name__)
CORS(app)

# constants
GOOGLE_CREDENTIALS_SENTIMENT = 'YOUR_GOOGLE_CREDENTIALS'


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/update")
def update_news_data():

    # fetch latest news
    NewsScraper.run('india')

    # clean fetched news
    NewsTextCleaner.run('india')

    # process sentiment of news
    NewsSentiment.run('india', GOOGLE_CREDENTIALS_SENTIMENT)

    return "request initiated"


@app.route("/prediction/live")
def live_predict():
    country = request.args.get('country')
    print('country: {}'.format(country))

    with open('./data/saved_predictions/{}.json'.format(country), 'r') as f:
        data = json.load(f)
        return jsonify({'predictions': data})


if __name__ == "__main__":
    app.run(debug=True)
