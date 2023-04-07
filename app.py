from flask import Flask, render_template, jsonify, request
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    page_size = 40
    page = request.args.get("page", 1, type=int)
    country = "in"
    api_key = "9ad2852f515c4ab5b1446c632061b2d2"
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}&pageSize={page_size}&page={page}"
    response = requests.get(url)
    articles = response.json()["articles"]
    return render_template("index.html", articles=articles)

@app.route('/world_news')
@app.route('/world_news/<category>')
def world_news(category=None):
    if category:
        news_api_key = os.environ.get('API_KEY')
        url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={news_api_key}"   
        response = requests.get(url)
        articles = response.json().get('articles', []) 
        return render_template('world.html', articles=articles, category=category)
    else:
        page_size = 40
        page = request.args.get("page", 1, type=int)
        country = "in"
        api_key = "9ad2852f515c4ab5b1446c632061b2d2"
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}&pageSize={page_size}&page={page}"
        response = requests.get(url)
        articles = response.json()["articles"]
        return render_template("index.html", articles=articles)
@app.route('/category/<category>')
def category_news(category):
    news_api_key = os.environ.get('API_KEY')
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={news_api_key}"   
    response = requests.get(url)
    articles = response.json().get('articles', []) 
    return render_template('category.html', articles=articles, category=category)

@app.route('/search')
def search():
    query = request.args.get('query')
    news_api_key = os.environ.get('API_KEY')
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={news_api_key}"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return render_template('search.html', articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
