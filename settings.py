import os
import redis


DEBUG = os.environ.get('DEBUG', True)
DB = redis.Redis(
    host=os.environ.get('DB_HOST', 'localhost'),
    port=os.environ.get('DB_PORT', 6379),
    db=os.environ.get('DB_NUMBER', 0)
)
