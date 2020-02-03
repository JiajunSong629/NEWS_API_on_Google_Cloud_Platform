from flask import Flask, flash, redirect, render_template, request, url_for
from flask import jsonify
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'name':'cnn'}, {'name':'bbc-news'},
            {'name':'reuters'},{'name':'google-news'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    newsapi = NewsApiClient(api_key="3ce897ffb4bc49bcb5ca9dd364e9a79e")
    news_source = request.form.get('comp_select')
    topheadlines = newsapi.get_top_headlines(sources=news_source)
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news, desc, img)
 
    return render_template('result.html', context=mylist)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)