from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# # ルートにおいて、index.htmlをレンダリングさせる
@app.route('/')
def index():
    sample_title = "title"
    sample_array = ['x', 'y', 'z']
    sample_json = {"title": "sample_title", "desc": "sample_desc"}
    return render_template('index.html', title=sample_title, array=sample_array, json=sample_json)

# # testというリクエスト受けた時に、実行する関数
@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        logging.log(30, 'warning')
        logging.log(100, 'test1')
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = request.form['post_value']
    return res

# # Localhostを立てるためのコマンド
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
