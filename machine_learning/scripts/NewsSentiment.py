import json
import re
import os

from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six


SRC_DATA_DIR = ''
DEST_DATA_DIR = ''

GOOGLE_CLOUD_CREDENTIAL = ''


def get_sentiment(article):

    content = article['title']
    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    try:

        response = client.analyze_sentiment(document)
        sentiment = response.document_sentiment

        # debug
        # print('Content: {}'.format(content))
        # print(response)
        # print('Score: {}'.format(sentiment.score))
        # print('Magnitude: {}'.format(sentiment.magnitude))
        # print()
        return {'content': content, 'score': sentiment.score, 'magnitude': sentiment.magnitude}

    except:
        print("Error occured in getting sentiment")
        print(document)
        return None


def process(filepath, curr_location):

    results = []

    with open(filepath, 'r', encoding='utf-8') as file:
        file_json = json.load(file)
        for article in file_json:
            curr_sentiment = get_sentiment(article)
            if curr_location is not None:
                results.append(curr_sentiment)

    return results


def save_output(out_file_path, input_data):
    with open(out_file_path, 'w') as out_file:
        json.dump(input_data, out_file)


def build_output_filepath(out_date, out_location):
    return "{}{}__{}.txt".format(DEST_DATA_DIR, out_date, out_location)


def init(country, google_cred):
    global SRC_DATA_DIR
    global DEST_DATA_DIR
    global GOOGLE_CLOUD_CREDENTIAL

    SRC_DATA_DIR = './data/raw_news_{}/'.format(country)
    DEST_DATA_DIR = './data/sentiment_news_{}/'.format(country)
    GOOGLE_CLOUD_CREDENTIAL = google_cred


def run(country, google_cred):

    # initialize
    init(country, google_cred)

    # set google cloud credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CLOUD_CREDENTIAL

    # creates output directory if it does not exist
    if not os.path.exists(DEST_DATA_DIR):
        os.makedirs(DEST_DATA_DIR)

    # Lists all files in the SRC_DATA_DIR directory
    # For each file, extracts the date and location from filename
    # Combines Text attributes and Cleans the data for that date and location
    # Builds path for output filename
    # Writes cleaned data to output file

    count = 0

    for filename in os.listdir(SRC_DATA_DIR):

        src_file_count = len([name for name in os.listdir(SRC_DATA_DIR) if os.path.isfile(SRC_DATA_DIR + name)])
        dest_file_count = len([name for name in os.listdir(DEST_DATA_DIR) if os.path.isfile(DEST_DATA_DIR + name)])

        print("Input Files: {} Processed Files {}".format(src_file_count, dest_file_count))

        if count > 50:
            break

        match = re.search(r'(.+)__(.+)\.json', filename)
        if match:
            date = match.group(1)
            location = match.group(2)

            src_filepath = SRC_DATA_DIR + filename
            dest_filepath = build_output_filepath(date, location)

            if os.path.isfile(dest_filepath):
                print("{} exists".format(dest_filepath))
                pass
            else:
                result = process(src_filepath, location)
                save_output(dest_filepath, result)
                print("Processed {} {}".format(date, location))
                count += 1

