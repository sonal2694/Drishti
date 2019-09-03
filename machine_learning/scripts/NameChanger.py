import os
import re

data_dir = './data/raw_news/'

# DO NOT RUN
# CHANGES THE NAME OF THE FILE
# CONVERTS LOCATION__DATE.json -> DATE__LOCATION.json or vice versa
for filename in os.listdir(data_dir):

    match = re.search(r'(.+)__(.+)\.json', filename)

    if match:
        old_name = match.group()
        new_name = "{}__{}.json".format(match.group(2), match.group(1))

        print(old_name)
        print(new_name)

        os.rename(data_dir + old_name, data_dir + new_name)

