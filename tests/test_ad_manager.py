import unittest
from ad_manager import AdManager


class AdsManagerTest(unittest.TestCase):
    def setUp(self):
        self.ad_manager = AdManager()

    def test_success_load_row(self):
        row = {
            'Campaign ID': '',
            'Campaign Title': 'Test Campaign2',
            'Campaign Objective': 'IMPRESSIONS',
            'Ad Group ID': '',
            'Ad Group Campaign ID': '',
            'Ad Group Title': 'Ad group 2',
            'Geo Locations': 'GB, AU, US-CA',
            'Start Date': '1/1/20',
            'End Date': '1/10/20',
            'Ad ID': '',
            'Ad Title': 'Ad 2',
            'Ad Ad Group ID': '',
            'Post ID': 't2_2'
        }
        campaign, ad_group, ad, message = self.ad_manager.load_row(row)
        self.assertEqual(message, 'Success')

    def test_success_missing_id_generate_integer(self):
        test_row = {
            'Campaign ID': '',
            'Campaign Title': 'Test Campaign2',
            'Campaign Objective': 'IMPRESSIONS',
            'Ad Group ID': '',
            'Ad Group Campaign ID': '',
            'Ad Group Title': 'Ad group 2',
            'Geo Locations': 'GB, AU, US-CA',
            'Start Date': '1/1/20',
            'End Date': '1/10/20',
            'Ad ID': '',
            'Ad Title': 'Ad 2',
            'Ad Ad Group ID': '',
            'Post ID': 't2_2'
        }
        campaign, ad_group, ad, message = self.ad_manager.load_row(test_row)
        self.assertEqual(type(campaign.id), int)
        self.assertEqual(type(ad_group.id), int)
        self.assertEqual(type(ad_group.id), int)
        self.assertEqual(message, 'Success')

    def test_success_duplicated_id_generate_new_id(self):
        row = {
            'Campaign ID': '100',
            'Campaign Title': 'Test Campaign2',
            'Campaign Objective': 'IMPRESSIONS',
            'Ad Group ID': '101',
            'Ad Group Campaign ID': '',
            'Ad Group Title': 'Ad group 2',
            'Geo Locations': 'GB, AU, US-CA',
            'Start Date': '1/1/20',
            'End Date': '1/10/20',
            'Ad ID': '102',
            'Ad Title': 'Ad 2',
            'Ad Ad Group ID': '',
            'Post ID': 't2_2'
        }

        campaign1, ad_group1, ad1, message1 = self.ad_manager.load_row(row)
        campaign2, ad_group2, ad2, message2 = self.ad_manager.load_row(row)

        self.assertEqual(message1, 'Success')
        self.assertEqual(message2, 'Success')
        self.assertTrue(campaign1.id != campaign2.id)
        self.assertTrue(ad_group1.id != ad_group2.id)
        self.assertTrue(ad1.id != ad2.id)

    def test_exception_invalid_date_type(self):
        test_row = {
            'Campaign ID': '',
            'Campaign Title': 'Test Campaign2',
            'Campaign Objective': 'IMPRESSIONS',
            'Ad Group ID': '',
            'Ad Group Campaign ID': '',
            'Ad Group Title': 'Ad group 2',
            'Geo Locations': 'GB, AU, US-CA',
            'Start Date': '1//20',
            'End Date': '1/10/20',
            'Ad ID': '',
            'Ad Title': 'Ad 2',
            'Ad Ad Group ID': '',
            'Post ID': 't2_2'
        }

        with self.assertRaises(ValueError) as e:
            self.ad_manager.load_row(test_row)
        self.assertEqual(str(e.exception), "time data '1//20' does not match format '%m/%d/%y'")


if __name__ == '__main__':
    unittest.main()
