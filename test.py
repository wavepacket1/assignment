import unittest
import json
import requests
from fib import app

class TestFibonacciAPI(unittest.TestCase):
    def setUp(self):
        self.app=app.test_client()

    def test_empty_input(self):
        response=self.app.get()
        data=json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code,400)
        self.assertEqual(data['status'],400)
        self.assertEqual(data['message'],"Bad request.")

    def test_negative_input(self):
        response=self.app.get('/?n=-1')
        data=json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code,400)
        self.assertEqual(data['status'],400)
        self.assertEqual(data['message'],"Bad request.")

    def test_zero_input(self):
        response=self.app.get('/?n=0')
        data=json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code,400)
        self.assertEqual(data['status'],400)
        self.assertEqual(data['message'],"Bad request.")
    
    def test_string_input(self):
        response=self.app.get('/?n=str')
        data=json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code,400)
        self.assertEqual(data['status'],400)
        self.assertEqual(data['message'],"Bad request.")

    def test_decimals_input(self):
        response=self.app.get('/?n=0.1')
        data=json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code,400)
        self.assertEqual(data['status'],400)
        self.assertEqual(data['message'],"Bad request.")
    

    def test_value_input(self):
        response=self.app.get('/?n=1')
        data=json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['result'],1)

    def test_value_input_sample(self):
            response=self.app.get('/?n=99')
            data=json.loads(response.get_data(as_text=True))

            self.assertEqual(response.status_code,200)
            self.assertEqual(data['result'],218922995834555169026)
    

if __name__=="__main__":
    unittest.main()
