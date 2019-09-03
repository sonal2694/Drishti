import subprocess

BASE_URL = "/Users/zeko/dev/projects/drishti/machine_learning/scripts/"

FASTTEXT_LOCATION = BASE_URL + "fasttext/fastText-0.2.0/fasttext"

TRAIN_DATASET = BASE_URL + "data/fasttext_datasets/train_set.txt"
TEST_DATASET = BASE_URL + "data/fasttext_datasets/test_set.txt"

TARGET_MODEL = BASE_URL + "data/models/fasttext_model"
GENERATED_MODEL = BASE_URL + "data/models/fasttext_model.bin"
# GENERATED_MODEL = "./test_model"

TRAINING_ARGS = [FASTTEXT_LOCATION, "supervised", "-input", TRAIN_DATASET, "-output", TARGET_MODEL]
TESTING_ARGS = [FASTTEXT_LOCATION, "test", GENERATED_MODEL, TEST_DATASET, "2"]

# debug
print("command run for training: ")
print(' '.join(TRAINING_ARGS))

print("Generating model")
res = subprocess.check_output(TRAINING_ARGS)
for line in res.splitlines():
    print(line)
print()

# debug
print("command run for testing: ")
print(' '.join(TESTING_ARGS))

print("Testing model")
res = subprocess.check_output(TESTING_ARGS)
for line in res.splitlines():
    print(line)
print()

print("Testing the model")





