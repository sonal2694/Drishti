import json
import re
import os


# initialized in init()
SRC_DATA_DIR = ''
DEST_DATA_DIR = ''


def clean_raw_data(filepath, location):
    with open(filepath, 'r', encoding='utf-8') as file:
        file_json = json.load(file)
        full_text = ''
        for article in file_json:

            # combines all attributes
            combined = ''
            if 'title' in article and article['title'] is not None:
                combined += article['title']
            # if 'description' in article and article['description'] is not None:
            #     combined += article['description'] + " "
            # if 'content' in article and article['content'] is not None:
            #     combined += article['content'] + " "

            # combined = re.sub(r'…\s\[\+.+chars\]', '', combined) # remove the last ...585 chars more part
            combined = re.sub(r"([.!?,'/():\"-])", r"", combined) # remove punctuations
            combined = combined.lower()
            # combined = combined.replace("\n", " ") # remove new lines
            # combined = combined.replace(" ", " ") # remove a special ASCII char

            full_text += combined + "\n"

        return full_text


def save_output(out_file_path, input):
    with open(out_file_path, 'w') as out_file:
        out_file.write(input)


def build_output_filepath(out_date, out_location):
    return "{}{}__{}.txt".format(DEST_DATA_DIR, out_date, out_location)


def init(country):

    global SRC_DATA_DIR
    global DEST_DATA_DIR

    SRC_DATA_DIR = './data/raw_news_{}/'.format(country)
    DEST_DATA_DIR = './data/processed_news_{}/'.format(country)


def run(country):

    # initialize
    init(country)

    # creates output directory if it does not exist
    if not os.path.exists(DEST_DATA_DIR):
        os.makedirs(DEST_DATA_DIR)

    # Lists all files in the SRC_DATA_DIR directory
    # For each file, extracts the date and location from filename
    # Combines Text attributes and Cleans the data for that date and location
    # Builds path for output filename
    # Writes cleaned data to output file

    for filename in os.listdir(SRC_DATA_DIR):
        match = re.search(r'(.+)__(.+)\.json', filename)
        if match:
            date = match.group(1)
            location = match.group(2)

            src_filepath = SRC_DATA_DIR + filename
            result = clean_raw_data(src_filepath, location.lower())

            dest_filepath = build_output_filepath(date, location)
            save_output(dest_filepath, result)

