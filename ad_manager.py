import csv
from datetime import datetime
from entities.campaign import Campaign
from entities.ad_group import AdGroup
from entities.ad import Ad


class AdManager:
    def __init__(self):
        self.campaigns = []
        self.ad_groups = []
        self.ads = []
        self.results = []

    @staticmethod
    def generate_id(entities):
        available_id = 1
        assigned_ids = [entity.id for entity in entities]

        while available_id in assigned_ids:
            available_id += 1

        return available_id

    @staticmethod
    def get_entity(entities, id):
        entity = None

        for item in entities:
            if item.id == id:
                entity = item

        return entity

    def load_row(self, row):
        result_message = "Success"

        try:
            campaign_id = int(row['Campaign ID'])
            campaign = self.get_entity(self.campaigns, campaign_id)
            if campaign:
                raise Exception("Campaign id conflict")
        except Exception as e:
            # Campaign id is invalid or conflict
            campaign_id = self.generate_id(self.campaigns)

        campaign = Campaign(
            campaign_id,
            row['Campaign Title'],
            row['Campaign Objective']
        )
        self.campaigns.append(campaign)

        try:
            ad_group_id = int(row['Ad Group ID'])
            ad_group = self.get_entity(self.ad_groups, ad_group_id)
            if ad_group:
                raise Exception("Ad group id conflict")
        except Exception as e:
            # Ad group id is invalid or conflict
            ad_group_id = self.generate_id(self.ads)

        ad_group = AdGroup(
            ad_group_id,
            campaign.id,
            row['Ad Group Title'],
            row['Geo Locations'].split(', '),
            datetime.strptime(row['Start Date'], "%m/%d/%y"),
            datetime.strptime(row['End Date'], "%m/%d/%y")
        )
        self.ad_groups.append(ad_group)

        try:
            ad_id = int(row['Ad ID'])
            ad = self.get_entity(self.ads, ad_id)
            if ad:
                raise Exception("Ad id conflict")
        except Exception as e:
            # Ad id is invalid or conflict
            ad_id = self.generate_id(self.ads)

        ad = Ad(ad_id, ad_group.id, row['Ad Title'], row['Post ID'])
        self.ads.append(ad)

        return campaign, ad_group, ad, result_message

    def load_csv(self, path):
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result = {
                    'Campaign ID': row['Campaign ID'],
                    'Campaign Title': row['Campaign Title'],
                    'Campaign Objective': row['Campaign Objective'],
                    'Ad Group ID': row['Ad Group ID'],
                    'Ad Group Campaign ID': row['Ad Group Campaign ID'],
                    'Ad Group Title': row['Ad Group Title'],
                    'Geo Locations': row['Geo Locations'],
                    'Start Date': row['Start Date'],
                    'End Date': row['End Date'],
                    'Ad ID': row['Ad ID'],
                    'Ad Title': row['Ad Title'],
                    'Ad Ad Group ID': row['Ad Ad Group ID'],
                    'Post ID': row['Post ID'],
                    'Results': 'Success',
                }

                try:
                    campaign, ad_group, ad, message = self.load_row(row)
                    result["Campaign ID"] = campaign.id
                    result["Ad Group ID"] = ad_group.id
                    result["Ad Group Campaign ID"] = campaign.id
                    result["Ad ID"] = ad.id
                    result["Ad Ad Group ID"] = ad_group.id
                    result["Results"] = message
                except Exception as e:
                    print(e)
                    result["Results"] = str(e)

                self.results.append(result)

    def export_result(self):
        with open('csv/Result.csv', 'w', newline='') as csvfile:
            field_names = self.results[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()

            for result in self.results:
                writer.writerow(result)

    def upload(self, path):
        self.load_csv(path)
        print("CSV loaded successfully")

        self.export_result()
        print("Result exported successfully")

    def print(self, path, entity_type, entity_id):
        pass
