import os
import redis


DEBUG = os.environ.get('DEBUG', True)
DB = redis.Redis(
    host=os.environ.get('DB_HOST', 'localhost'),
    port=os.environ.get('DB_PORT', 6379),
    db=os.environ.get('DB_NUMBER', 0)
)
LIMIT = os.environ.get('REQHOUR_LIMIT', 1000)
SENTRY_DSN = os.environ.get('SENTRY_DSN', None)
