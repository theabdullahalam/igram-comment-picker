from django.test import TestCase

class MainTestCase(TestCase):

    def test_index(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    

    # def test_useless(self):
    #     print('A useless test to see the output')
    #     self.assertEqual(True, False)
