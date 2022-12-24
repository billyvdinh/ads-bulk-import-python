import unittest
import random
from entities.campaign import Campaign


class CampaignTest(unittest.TestCase):
    def test_success_create_campaign(self):
        id = random.randint(1, 1000)
        title = "test campaign"
        objective = "CLICKS"
        campaign = Campaign(id, title, objective)
        self.assertEqual(id, campaign.id)
        self.assertEqual(title, campaign.title)
        self.assertEqual(objective, campaign.objective)

    def test_exception_create_campaign(self):
        with self.assertRaises(Exception) as e:
            Campaign('invalid', "test campaign", 'CLICKS')
        self.assertEqual(str(e.exception), 'id must be integer')

        with self.assertRaises(Exception) as e:
            Campaign(1, 123, 'CLICKS')
        self.assertEqual(str(e.exception), 'title must be string or None')

        with self.assertRaises(Exception) as e:
            Campaign(1, "test campaign", True)
        self.assertEqual(str(e.exception), 'objective must be string or None')
