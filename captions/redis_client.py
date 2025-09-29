import redis

# Connect to local Redis
redis_client = redis.StrictRedis(host="devnwvm", port=6379, db=0, decode_responses=True)
