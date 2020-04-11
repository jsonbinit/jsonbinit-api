from falcon import testing
import json
import os
import pytest

os.environ["DEBUG"] = "0"

import main


class MockDB:
    def __init__(self, *args, **kwargs):
        self._data = {}

    def set(self, key, val):
        self._data[key] = val

    def get(self, key):
        return self._data.get(key, None)


@pytest.fixture()
def client():
    return testing.TestClient(main.api)


def test_get_not_existing_json(client, mocker):
    mocker.patch.object(main.settings, 'DB')
    main.settings.DB = MockDB()
    not_found = {'status': 'JSON not found'}
    result = client.simulate_get('/bins/er12hg56')
    assert result.json == not_found


def test_post_not_valid_url(client, mocker):
    mocker.patch.object(main.settings, 'DB')
    main.settings.DB = MockDB()
    result = client.simulate_post('/bins/er12hg56')
    assert result.status_code == 404


def test_store_json(client, mocker):
    mocker.patch.object(main.settings, 'DB')
    main.settings.DB = MockDB()
    result = client.simulate_post(
        '/bins/',
        body=json.dumps({'value' : 3}),
        headers={'Content-type' : 'application/json'}
    )
    assert len(result.json['bin']) == 8
    result = client.simulate_get('/bins/' + result.json['bin'])
    assert result.json['value'] == 3


def test_store_json_with_collision(client, mocker):
    mocker.patch.object(main.settings, 'DB')
    main.settings.DB = MockDB()
    mocker.patch('main.random_string')
    main.random_string.side_effect = ['ABCdEfgh', 'ABCdEfgh', 'bazyBazy']
    result = client.simulate_post(
        '/bins/',
        body=json.dumps({'value' : 3}),
        headers={'Content-type' : 'application/json'}
    )
    assert len(result.json['bin']) == 8
    result = client.simulate_get('/bins/' + result.json['bin'])
    assert result.json['value'] == 3
    result = client.simulate_post(
        '/bins/',
        body=json.dumps({'value' : 3}),
        headers={'Content-type' : 'application/json'}
    )
    assert len(result.json['bin']) == 8
    result = client.simulate_get('/bins/' + result.json['bin'])
    assert result.json['value'] == 3
