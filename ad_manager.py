import csv

from entities.campaign import Campaign
from entities.ad_group import AdGroup
from entities.ad import Ad


class AdManager:
    def __init__(self):
        self.campaigns = []
        self.ad_groups = []
        self.ads = []
        self.results = []

    def load_csv(self, path):
        rows = []
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rows.append(row)

        print(rows)
        return rows

    def export_result(self):
        pass

    def upload(self, path):
        self.load_csv(path)
        print("CSV loaded successfully")

        self.export_result()
        print("Result exported successfully")

    def print(self, path, entity_type, entity_id):
        pass
