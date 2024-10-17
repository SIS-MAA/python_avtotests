import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '54b465bd7fa146a517ee1709065242e2'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
    }
TRAINER_ID = '11396'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_quariy():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"]== 'эмптиабан'


