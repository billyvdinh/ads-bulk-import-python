import unittest
import random
from entities.ad import Ad


class AdTest(unittest.TestCase):
    def test_success_create_ad(self):
        id = random.randint(1, 1000)
        ad_group_id = random.randint(1, 1000)
        title = "ad title"
        post_id = "post id"
        ad = Ad(id, ad_group_id, title, post_id)
        self.assertEqual(id, ad.id)
        self.assertEqual(ad_group_id, ad.ad_group_id)
        self.assertEqual(title, ad.title)
        self.assertEqual(post_id, ad.post_id)

    def test_exception_create_ad(self):
        id = random.randint(1, 1000)
        ad_group_id = random.randint(1, 1000)
        title = "ad title"
        post_id = "post id"

        with self.assertRaises(Exception) as e:
            Ad('invalid', ad_group_id, title, post_id)
        self.assertEqual(str(e.exception), 'id must be integer')

        with self.assertRaises(Exception) as e:
            Ad(id, 'invalid ad group id', title, post_id)
        self.assertEqual(str(e.exception), 'ad group id must be integer')

        with self.assertRaises(Exception) as e:
            Ad(id, ad_group_id, 123, post_id)
        self.assertEqual(str(e.exception), 'title must be string or None')

        with self.assertRaises(Exception) as e:
            Ad(id, ad_group_id, title, 123)
        self.assertEqual(str(e.exception), 'post id must be string or None')
