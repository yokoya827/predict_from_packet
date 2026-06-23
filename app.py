# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import threading
import subprocess
from time import sleep
from table import make_a_list,make_graph
from table_gen import table_cooking


app = Flask(__name__)

#threadingで自動で立ち上げる
def auto_open():
    sleep(2.4)
    print('WEBで表示します。')
    try:
        subprocess.check_call("termux-open http://127.0.0.1:5000/",shell=True)
    except:
        print('コマンドが機能しませんでした。手動でhttp://127.0.0.1:5000/へアクセスして下さい。')

def html_source(html_file):
    url = './templates/' + html_file
    with open(url, encoding="utf-8") as f:
        reader = f.read()
    reader = reader.replace('<html>\n<head><meta charset="utf-8" /></head>\n<body>','')
    reader = reader.replace('</body>\n</html>','')
    return reader


@app.route('/',methods=['GET'])
def get_posi():
    population = make_a_list()
    make_graph()
    data = table_cooking(population)
    return render_template('index.html',\
        data = '<p class="spacer">以下のデータを地図上で表示します。</p>' + data)

@app.route('/bo')
def bo():
    html_file = 'bo.html'
    data = html_source(html_file)
    return render_template('index.html',\
        data = data)


@app.route('/oresen')
def oresen():
    html_file = 'oresen.html'
    data = html_source(html_file)
    return render_template('index.html',\
        data = data)


@app.route('/en')
def en():
    html_file = 'en.html'
    data = html_source(html_file)
    return render_template('index.html',\
        data = data)

@app.route('/hour')
def hour():
    html_file = 'hour.html'
    data = html_source(html_file)
    return render_template('index.html',\
        data = data)

@app.route('/table')
def table():
    html_file = 'table.html'
    data = html_source(html_file)
    return render_template('index.html',\
        data = data)


@app.route('/refresh')
def refresh():
    population = make_a_list()
    make_graph()
    data = table_cooking(population)
    return render_template('index.html',\
        data = '<p class="spacer">データを現在時刻のものに更新しました。</p>' + data)


if __name__ == '__main__':
    sub= threading.Thread(target=auto_open)
    sub.start() 
    app.run()