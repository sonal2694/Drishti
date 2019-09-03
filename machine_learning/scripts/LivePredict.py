import sklearn
from sklearn_pandas import DataFrameMapper
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd
import datetime
import os
import re
import json

MODEL = None
CURR_DATE = datetime.datetime.now().date()
COUNTRY = ''
CLEAN_NEWS_DIR = ''
SENTIMENT_NEWS_DIR = ''
DATASET = None


def init(country):

    global MODEL
    global COUNTRY
    global CLEAN_NEWS_DIR
    global SENTIMENT_NEWS_DIR
    global DATASET

    COUNTRY = country
    CLEAN_NEWS_DIR = './data/processed_news_{}/'.format(COUNTRY)
    SENTIMENT_NEWS_DIR = './data/sentiment_news_{}/'.format(COUNTRY)

    dataset_file_path = './data/saved_datasets/{}.pkl'.format(COUNTRY)
    model_file_path = './data/models/ensemble/model_{}.pkl'.format(COUNTRY)

    # Load from file
    with open(model_file_path, 'rb') as file:
        MODEL = pickle.load(file)

    # Load from file
    with open(dataset_file_path, 'rb') as f:
        DATASET = pickle.load(f)


def get_cities():

    global CLEAN_NEWS_DIR

    cities = []

    for filename in os.listdir(CLEAN_NEWS_DIR):
        # match = re.search(r'(.+)__(.+)\.json', filename)
        match = re.search(re.escape('{}'.format(CURR_DATE)) + r'__(.+)\.txt', filename)
        if match:
            location = match.group(1)
            cities.append(location)

    return cities


def get_cleaned_news(cities):
    news = []
    for city in cities:
        # print('here')
        filepath = "{}{}__{}.txt".format(CLEAN_NEWS_DIR, CURR_DATE, city)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as text_file:
                news.append(text_file.read())
        else:
            news.append('')
    return news


def compute_avg_score(sentiment_file):
    s = 0.0
    ct = 0
    for i in sentiment_file:
        if i is not None:
            s += i['score'] * i['magnitude'] * 100
            ct += 1
    if ct is not 0:
        return s / ct
    else:
        return 0


def get_sentiment(cities):

    global SENTIMENT_NEWS_DIR
    global CURR_DATE

    sentiments = []
    for city in cities:
        # print('here')
        filepath = "{}{}__{}.txt".format(SENTIMENT_NEWS_DIR, CURR_DATE, city)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as text_file:
                data = json.load(text_file)
                sentiments.append(compute_avg_score(data))
        else:
            sentiments.append(0)
    return sentiments


def run(country):

    global MODEL
    global CURR_DATE

    # initialize
    init(country)
    cities = get_cities()
    # print(cities)
    news = get_cleaned_news(cities)
    sentiments = get_sentiment(cities)

    # df = pd.DataFrame({'news': news, 'sentiment_score': sentiments})

    # src_last = DATASET['src'][-1*len(cities):]
    # print(src_last)

    # df_last = DATASET[-1*len(cities):]

    mapper = DataFrameMapper([
        ('news', TfidfVectorizer()),
        ('sentiment_score', None),
        # ('src', None)
    ])


    # today_records = DATASET.index[DATASET['src'].startswith('{}'.format(CURR_DATE))].tolist()
    # print('{}'.format(CURR_DATE))
    df = DATASET[DATASET.src.str.startswith('{}'.format(CURR_DATE))]
    print(df)

    # print(DATASET.describe(include='all'))

    X = mapper.fit_transform(DATASET)
    # X_live = X[X.src.str.startswith('{}'.format(CURR_DATE))]
    # X_live.drop(['src'], axis=1, inplace=True)

    print(MODEL.predict(X))





    # get current date

    # get all cleaned news for the date
    # get all sentiments for the previous records
    # combine into a X_test
    # predict
