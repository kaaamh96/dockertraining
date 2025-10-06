from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route ('/') 
def welcome():
    return 'welcome to the coderco containers challenge'

@app.route('/count')
def count():
    count = r.incr('visits')
    return f"this page has been visited {count} times"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)