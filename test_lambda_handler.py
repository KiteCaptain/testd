import pytest
# from pymongo import MongoClient
from lambda_functions import lambda_handler

def test_lambda_handler_success():
    # Arrange
    event = {}
    context = {}

    # Act
    result = lambda_handler(event, context)

    # Assert
    assert result['isError'] 
    assert len(result['body']) > 0

def test_lambda_handler_error():
    # Arrange
    event = {}
    context = {}

    # Act
    result = lambda_handler(event, context)

    # Assert
    assert result['isError']
    assert 'Error' in result['body']
