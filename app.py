"""Main application file"""
from flask import Flask
app = Flask(__name__)
# aaaaaa
@app.route('/<random_string1>')
def returnBackwardsString(random_string1):
    """Reverse and return the provided URI"""
    return "".join(reversed(random_string1))

@app.route('/hello')
def hello():
   return "Hello AWS-Github!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)