from controller import app
import unittest


class FlaskTestCase(unittest.TestCase):
    # Check if flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/orders', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    # Check if the returned content is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/orders', content_type="html/text")
        self.assertEqual(response.content_type, "application/json")

    # Test order_items and deliveries database model relationship
    # Check if there are deliveries are loaded with their corresponding order_items
    def test_deliveries(self):
        tester = app.test_client(self)
        response = tester.get('/order_items', content_type="html/text")
        self.assertTrue(b'deliveries' in response.data)


if __name__ == '__main__':
    unittest.main()
