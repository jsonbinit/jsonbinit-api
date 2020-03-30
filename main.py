import falcon
import json
import settings

import random
import string


def random_string(str_length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(str_length))


def get_json(json_id):
    db = settings.DB
    try:
        return json.loads(db.get(json_id))
    except TypeError:
        return None


def save_json(body):
    json_id = random_string()
    db = settings.DB
    while db.get(json_id):
        json_id = random_string()
    db.set(json_id, json.dumps(body))
    return json_id


class JSONResource:

    def on_get(self, req, resp, json_id):
        """Handles GET request to get a specific JSON"""
        json_get = get_json(json_id)
        if not json_get:
            resp.status = falcon.HTTP_404
            resp.media = {'status' : 'JSON not found'}
        else:
            resp.media = json_get

    def on_post(self, req, resp, json_id=None):
        """Handles POST request to save a JSON"""

        if json_id:
            resp.status = falcon.HTTP_404

        json_id = save_json(req.media)

        json_res = {
            'bin': json_id
        }

        resp.status = falcon.HTTP_201
        resp.media = json_res


api = falcon.API()
api.add_route('/api/bins/{json_id}', JSONResource())


if settings.DEBUG == True:
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
