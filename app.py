from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    response = requests.get("http://10.0.0.3:5000/companies")
    print(response.status_code)
    json = str(response.content)
    return json

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001)