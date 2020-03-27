import falcon


class JSONResource:

    def on_get(self, req, resp):
        """Handles GET requests"""
        json_res = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = json_res


api = falcon.API()
api.add_route('/api/bins', JSONResource())
