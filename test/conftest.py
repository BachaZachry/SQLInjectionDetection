import pytest
from flask import Flask
from app import app



@pytest.fixture
def client():
    client = app.test_client()
    return client