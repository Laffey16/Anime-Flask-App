import requests
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_caching import Cache
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
danbooru_key = os.getenv('DANBOORU_API_KEY')

cache = Cache(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/anime', methods=['GET', 'POST'])
def anime():
    if request.method == 'POST':
        user_input = request.form.get('anime_input')

        # Send user input to the external API using requests
        link = "https://danbooru.donmai.us/posts.json"
        querystring = {
            "limit": 50,
            "tags": f"{user_input}",
            "random": 1,
        }
        r = requests.get(link, params=querystring, auth=("Laffey16",str(danbooru_key)))
        status_code = r.status_code
        if status_code != 200:
            print(f"Request failed\nStatus code: {status_code}")

            if status_code == 422:
                flash(f'422: Cannot request more than 2 tags', 'error')
            return redirect(url_for('anime'))
        data = r.json()
        image_urls = []

        print("Got data")
        for i in range(0, len(data)):
            try:
                image_urls.append(data[i]['file_url'])
            except KeyError:
                flash(f'Could not find file_url on iteration: {i}', 'warning')

        if len(image_urls) == 0:
            print('No images found for this query.')
            flash('No images found for this query.', 'error')
            return redirect(url_for('anime'))

        return render_template('anime.html', image_urls=image_urls)

    return render_template('anime.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


