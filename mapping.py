import csv
import pickle as pickle


csv_file = 'dataset.csv'

with open(csv_file) as csvfile:
    reader = csv.DictReader(csvfile)

    mapping = {}
    for row in reader:
        mapping[row['img_id']] = row['img_name']

    pickle.dump(mapping, open('model/mapping.pkl', 'wb'))
