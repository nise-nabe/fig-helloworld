from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(
    host=os.environ.get('FIGTEST_REDIS_1_PORT_6379_TCP_ADDR'),
    port=int(os.environ.get('FIGTEST_REDIS_1_PORT_6379_TCP_PORT'))
)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
