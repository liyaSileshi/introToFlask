import requests
from flask import Flask
#
app = Flask(__name__)

@app.route('/')
def make_joke():
    params = {
    "q": "spongebob",
    "Key": "CEED88MTT59M"
    }
    response = requests.get(
    'https://api.tenor.com/v1/search',
    params = params)
    joke_json = r.json()
    return "Hello worlkd"




if __name__ == "__main__":
    app.run(debug=True, port=5000)



#spongebob gif query
params = {
"q": "trump",
"Key": "CEED88MTT59M"
}
response = requests.get(
'https://api.tenor.com/v1/search',
params = params)

gif_json= response.json()
