import unittest
import csv
import json

class TestCSVtoJSONConversion(unittest.TestCase):

    def test_csv_columns(self):
        with open('profiles1.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)
            self.assertEqual(len(headers), 12, "CSV should contain 12 columns")

    def test_csv_rows(self):
        with open('profiles1.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
            self.assertTrue(len(rows) > 900, "CSV should contain more than 900 rows")

    def test_json_properties(self):
        with open('data.json', mode='r') as json_file:
            data = json.load(json_file)
            self.assertTrue(all('column1' in row for row in data), "JSON should contain all required properties")

    def test_json_rows(self):
        with open('data.json', mode='r') as json_file:
            data = json.load(json_file)
            self.assertTrue(len(data) > 900, "JSON should contain more than 900 rows")