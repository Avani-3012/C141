from flask import Flask, jsonify, request

import itertools
from demographic_filtering import output
from content_filtering import get_recommendations
import pandas as pd
import csv

all_articles = []

with open('articles.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_article = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-article")
def get_movie():
    article_data = {
        "title": all_articles[0][19],
      
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_movie():
    article = all_articles[0]
    not_liked_article.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch_view():
    article = all_articles[0]
    did_not_watch.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-movies")
def popular_movies():
    article_data = []
    for article in output:
        _d = {
            "title": article[0],
            
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_article():
    all_recommended=[]
    for liked_article in liked_articles:
        output=get_recommendations(liked_article[19])
        for data in output:
            all_recommended.append(data)
        
    all_recommended.sort()
    article_data=[]
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200



if __name__ == "__main__":
  app.run()