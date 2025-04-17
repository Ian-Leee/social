from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request
import requests
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = b'|?`\x9d\xf4\x9dTf\x10\xeak\xbctG\x87\xba'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update", methods=['POST'])
def update():
    print(request.form['name'])

    #x=name
    url = f"https://scholar.google.com.tw/scholar?hl=zh-TW&as_sdt=0%2C5&q={str(request.form['name'])}&btnG="

    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    Q = soup.find_all(class_ = "gs_ri")
    result = []

    for q in Q:
        inf = [q.find(class_ = "gs_a").getText()]
        result.append({
            "title" : q.find(class_ = "gs_rt").find("a").getText(), #get title
            "url" : q.find(class_ = "gs_rt").find("a")["href"], #get url
            "author" : [man.split('-')[0].replace(u'\xa0', u' ') for man in inf][0], #get author
            "publish Time ": [man.split('-')[1].split(',')[-1] for man in inf][0],  #get publish time
            "quotation_times" : q.find(class_ = "gs_fl").find_all("a")[2].getText()
        })

    return render_template("data.html", data=result)
@app.route("/image")     # 加入 path: 轉換成「路徑」的類型
def image():
    return render_template("image.html")
@app.route("/aqua")     # 加入 path: 轉換成「路徑」的類型
def aqua():
    return render_template("image/aqua.html")

app.run()
