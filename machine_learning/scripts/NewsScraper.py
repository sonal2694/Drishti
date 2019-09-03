import csv
import datetime
import os.path
import requests
import json

# getset on init()
RAW_NEWS_DIR = ""
LOCATIONS = ""

api_keys = ["7e8673f621404230be4db20a136034ed", "64f1f474922343df9c888309de31e524", "2e074101f45d4f3890e074e6412d945a",
            "02367352fc644460891327a6cbb7e595", "334f0b6b14c048cb9bec97422acd35aa", "c3b5c481065b4fabab4948054b36a9f8",
            "0ee1cde1d0b14901a07f1ea3d16e1ff4", "2f69d20cadbb40e6adb3de00308a9bad", "b722ed504c0345dc885cdc54b0b9cee4"]


# decide api key
api_call_count = 0
api_key_index = 0

# list of dictionary objects returned by csv.DectReader
location_data = []


def load_locations():
    # read top 15 locations
    with open(LOCATIONS, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=['name', 'lat', 'long', 'freq'])

        # each row is an ordered dict
        for row in csv_reader:
            location_data.append(row)


# Today's date
news_end_date = datetime.datetime.now().date()

MAX_API_CALL_COUNT = 990


# Returns a key which is not exhausted
def get_active_api_key(last_failed=False):

    global api_key_index
    global api_call_count

    if last_failed:
        api_key_index += 1
        api_call_count = 0

    if api_key_index >= len(api_keys):
        print("NO API KEY LEFT")
        exit()

    if api_call_count >= MAX_API_CALL_COUNT:
        if api_key_index == len(api_keys) - 1:
            api_key_index += 1
            return None
        else:
            api_call_count = 0
            api_key_index += 1

    return api_keys[api_key_index]


# Helper method for making requests
def make_request(url):
    response = requests.get(url)
    return json.loads(response.content)


# makes the call to the API
def get_raw_news(news_location, news_date, api_key):

    url = "https://newsapi.org/v2/everything?pageSize=100&q={}&from={}&to={}&sortBy=relevancy&apiKey={}".format(news_location,
                                                                                                   news_date,
                                                                                                   news_date,
                                                                                                   api_key)
    response_json = make_request(url)

    print(response_json['articles'])

    if 'articles' in response_json:
        return response_json['articles']
    else:
        print("REQUEST FAILED - TRYING AGAIN")

        # debug
        # print(response_json)

        return get_raw_news(news_location, news_date, get_active_api_key(last_failed=True))


# Saves data to disk
def save_raw_news(new_file_path, raw_articles):
    with open(new_file_path, 'w') as out_file:
        json.dump(raw_articles, out_file)


# builds output file path
def build_file_path(event_date, event_location):
    return "{}{}__{}.json".format(RAW_NEWS_DIR, event_date, event_location)


def scrape(scrape_location, scrape_date):
    scrape_out_file_path = build_file_path(scrape_date, scrape_location)
    if os.path.isfile(scrape_out_file_path):
        print("{} exists".format(scrape_out_file_path))
        pass
    else:
        scraped_articles = get_raw_news(scrape_location, scrape_date, get_active_api_key())
        if scraped_articles is not None:
            save_raw_news(scrape_out_file_path, scraped_articles)
            print("Fetched {} articles for {} {}".format(len(scraped_articles), scrape_location, scrape_date))
        else:
            print("{} {} could not retrieve news".format(scrape_location, scrape_date))


def init(country):
    global RAW_NEWS_DIR
    global LOCATIONS
    global location_data

    location_data = []

    # set output directory
    RAW_NEWS_DIR = "./data/raw_news_{}/".format(country)
    if country is 'india':
        LOCATIONS = "./data/locations/top-15-india-locations.csv"

    load_locations()


# Scrape news for each day in the past 1 month
# Goes from Today's date to 29 days in the past (reverse order)
def run(country):
    init(country)
    for i in range(29):
        curr_date = news_end_date - datetime.timedelta(days=i)
        # for each location
        for location in location_data:
            scrape(location['name'], curr_date)

    print("")
    print("SCRAPING DONE FOR THE GIVEN PARAMS")
