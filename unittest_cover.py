import pytest
from pymongo.collection import Collection
from unittest.mock import Mock
from lambda_functions import lambda_handler

@pytest.fixture(scope='function')
def mocked_db_collection():
    mocked_collection = Mock(spec=Collection)
    mocked_collection.find.return_value = [{'name': 'USA', 'population': '328.2 million'}, {'name': 'Canada', 'population': '37.6 million'}]
    return mocked_collection

@pytest.fixture(scope='function')
def mocked_db_connection(monkeypatch, mocked_db_collection):
    mocked_connection = Mock()
    mocked_connection.__getitem__.return_value = mocked_db_collection
    monkeypatch.setattr('pymongo.MongoClient', lambda *args, **kwargs: mocked_connection)
    return mocked_connection

def test_lambda_handler(mocked_db_connection):
    expected_response = {'isError': False, 'body': [{'name': 'USA', 'population': '328.2 million'}, {'name': 'Canada', 'population': '37.6 million'}]}
    assert lambda_handler(None, None) == expected_response
