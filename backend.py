from flask import Flask
import json
import datetime
import os  # 👈 Needed for Vercel to get the port

app = Flask(__name__)

@app.route('/news.all.get')
def get_news_all_articles():
    data = []
    with open('news_data.json', 'r') as file:
        data = json.load(file)
    app.logger.debug('_________________Hello ' + str(data))
    return json.dumps(data)

@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return json.dumps(data)

@app.route('/')
def index():
    return '{"title": "List of Categories", "time": "2025-11-01 22:45:03", "categories": [{"id": 1, "name": "Sports"}, {"id": 2, "name": "Politics"}, {"id": 3, "name": "Education"}]}'

if __name__ == '__main__':
    # 👇 Use environment variable PORT (required for Vercel)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
