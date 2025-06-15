from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_client = redis.StrictRedis(host=redis_host, port=6379, db=0)

@app.route('/')
def hello():
    count = redis_client.incr('hits')
    return f'Visitor Count: {count}'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)