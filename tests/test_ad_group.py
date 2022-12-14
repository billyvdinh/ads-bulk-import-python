import unittest
import random
from datetime import datetime
from entities.ad_group import AdGroup


class AdGroupTest(unittest.TestCase):
    def test_success_create_ad_group(self):
        id = random.randint(1, 1000)
        campaign_id = random.randint(1, 1000)
        title = "test ad group"
        geolocations = "US, CA".split(', ')
        start_date = datetime.now()
        end_date = datetime.now()
        ad_group = AdGroup(id, campaign_id, title, geolocations, start_date, end_date)
        self.assertEqual(id, ad_group.id)
        self.assertEqual(campaign_id, ad_group.campaign_id)
        self.assertEqual(title, ad_group.title)
        self.assertEqual(geolocations, ad_group.geolocations)
        self.assertEqual(start_date, ad_group.start_date)
        self.assertEqual(end_date, ad_group.end_date)

    def test_exception_create_ad_group(self):
        id = random.randint(1, 1000)
        campaign_id = random.randint(1, 1000)
        title = "test ad group"
        geolocations = "US, CA".split(', ')
        start_date = datetime.now()
        end_date = datetime.now()

        with self.assertRaises(Exception) as e:
            AdGroup('invalid id', campaign_id, title, geolocations, start_date, end_date)
        self.assertEqual(str(e.exception), 'id must be integer')

        with self.assertRaises(Exception) as e:
            AdGroup(id, 'invalid campaign id', title, geolocations, start_date, end_date)
        self.assertEqual(str(e.exception), 'campaign id must be integer')

        with self.assertRaises(Exception) as e:
            AdGroup(id, campaign_id, title, 'invalid geolocation', start_date, end_date)
        self.assertEqual(str(e.exception), 'geolocations must be list or None')

        with self.assertRaises(Exception) as e:
            AdGroup(id, campaign_id, title, geolocations, 'invalid start date', end_date)
        self.assertEqual(str(e.exception), 'start date must be datetime or None')

        with self.assertRaises(Exception) as e:
            AdGroup(id, campaign_id, title, geolocations, start_date, 'invalid end date')
        self.assertEqual(str(e.exception), 'end date must be datetime or None')
