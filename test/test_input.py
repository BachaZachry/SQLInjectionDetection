from .conftest import client
from flask import json

def test_wrong_http_request(client):
    response = client.get('/v1/sanitized/input/')
    assert response.status_code == 405


def test_input_sanitized(client):

    response = client.post('/v1/sanitized/input/',data=dict(payload="normal input that does not present a risk"))

    assert response.status_code == 200
    assert b'sanitized' in response.get_data()

def test_input_unsanitized_dash(client):
    response = client.post('/v1/sanitized/input/', data=dict(payload="this input -- might cause a problem"))

    assert response.status_code == 200
    assert b'unsanitized' in response.get_data()

def test_input_unsanitized_quote(client):
    response = client.post('/v1/sanitized/input/', data=dict(payload="this input'might cause a problem"))

    assert response.status_code == 200
    assert b'unsanitized' in response.get_data()

def test_input_unsanitized_semicol(client):
    response = client.post('/v1/sanitized/input/', data=dict(payload="this input might cause a problem;"))

    assert response.status_code == 200
    assert b'unsanitized' in response.get_data()

def test_input_unsanitized_comment(client):
    response = client.post('/v1/sanitized/input/', data=dict(payload="/*this input might cause a problem*/"))

    assert response.status_code == 200
    assert b'unsanitized' in response.get_data()


def test_input_unsanitized_one_line_comment(client):
    response = client.post('/v1/sanitized/input/', data=dict(payload="#this input might cause a problem"))

    assert response.status_code == 200
    assert b'unsanitized' in response.get_data()

def test_input_unsanitized_or(client):
    response = client.post('/v1/sanitized/input/', data=dict(payload="this input might cause a problem OR 1=1"))

    assert response.status_code == 200
    assert b'unsanitized' in response.get_data()