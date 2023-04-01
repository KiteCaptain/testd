import unittest
from unittest.mock import MagicMock
from lambda_functions import lambda_handler, DBConnect

class TestLambdaHandler(unittest.TestCase):

    def setUp(self):
        self.event = {}
        self.context = MagicMock()

    def test_lambda_handler_returns_success_response(self):
        # mock DB connection and find method
        mock_response = [{'name': 'India', 'population': 1380004385}, {'name': 'USA', 'population': 331449281}]
        mock_find = MagicMock(return_value=mock_response)
        mock_collection = MagicMock()
        mock_collection.find = mock_find
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_client = MagicMock()
        mock_client.__getitem__.return_value = mock_db
        mock_connect = MagicMock(return_value=mock_client)
        DBConnect.__connect__ = mock_connect

        # call lambda_handler
        result = lambda_handler(self.event, self.context)

        # assert response
        expected_result = {
            'isError': False,
            'body': [{'name': 'India', 'population': 1380004385}, {'name': 'USA', 'population': 331449281}]
        }
        self.assertEqual(result, expected_result)

    def test_lambda_handler_returns_error_response(self):
        # mock DB connection and find method to raise an error
        mock_find = MagicMock(side_effect=Exception('Connection Error'))
        mock_collection = MagicMock()
        mock_collection.find = mock_find
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_client = MagicMock()
        mock_client.__getitem__.return_value = mock_db
        mock_connect = MagicMock(return_value=mock_client)
        DBConnect.__connect__ = mock_connect

        # call lambda_handler
        result = lambda_handler(self.event, self.context)

        # assert response
        expected_result = {
            'isError': True,
            'body': 'Error occurred: Connection Error'
        }
        self.assertEqual(result, expected_result)
