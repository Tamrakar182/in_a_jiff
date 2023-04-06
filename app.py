import requests
from decouple import config
from flask import Flask, render_template, request

app = Flask(__name__)

apiurl = "https://tenor.googleapis.com/v2/search"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_query = request.form['search_query']

        # Parameters for the Tenor API request
        params = {
            'key': config("API_KEY"),
            'q': search_query,
            'client_key': "in_a_jiff",
            'limit': 9
        }

        response = requests.get(apiurl, params=params)
        json_data = response.json()
        gif_urls = [result["media_formats"]["gif"]["url"] for result in json_data['results']]

        return render_template('results.html', gif_urls=gif_urls, search_query=search_query)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)