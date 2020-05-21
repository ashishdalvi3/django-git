from django.test import TestCase
import unittest
import requests
from app.views import index, test

class test_views(unittest.TestCase):

        def test_index_status_code(self):
                url = index(requests)
                self.assertEqual(url.status_code, 200)
                

        def test_index_verify_response(self):
                url = index(requests)
                self.assertEqual(url.content, b'Hello World!')       

        def test_test_status_code(self):
                url = test(requests)
                self.assertEqual(url.status_code, 200)
                

        def test_test_verify_response(self):
                url = test(requests)
                self.assertEqual(url.content, b'My second view!')      