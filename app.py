from http import client
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://azharyazied2:14juni2002@cluster0.4uh4rdq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbyzd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/analis", methods=["POST"])
def analis_post():
    url_receive = request.form['url_give']
    date_receive = request.form['date_give']
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one(' title ').text
    og_description = soup.select_one('meta[property="og:description"]')
    og_image = soup.select_one('meta[property="og:image"]')

    desc = og_description['content']
    image = og_image['content']

    doc = {
        'URL': url_receive,
        'Date': date_receive,
        'Title': title,
        'Description': desc,
        'Gambar': image
    }

    db.analis.insert_one(doc)
    return jsonify({'msg':'Input Berhasil!'})

@app.route("/analis", methods=["GET"])
def analis_get():
    analis_list = list(db.analis.find({}, {'_id': False}))
    return jsonify({'analisis': analis_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# Nama : Azhari Yazid
# NIM : 20200801298