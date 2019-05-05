from app_init import app
from flask import request
from models import NewsApi
from flask_cors import CORS


@app.route('/tencentnews', methods=['GET'])
@app.route('/tencentnews/', methods=['GET'])
def news_by_pubtime():
    if request.method == 'GET':
        res = NewsApi.get_news()
        return res
    else:
        return 'Request Error!'\


@app.route('/tencentnews/view_rank', methods=['GET'])
@app.route('/tencentnews/view_rank/', methods=['GET'])
def news_by_view():
    if request.method == 'GET':
        res = NewsApi.get_news_by_view()
        return res
    else:
        return 'Request Error!'


@app.route('/tencentnews/detail/<string:newsid>', methods=['GET'])
@app.route('/tencentnews/detail/<string:newsid>/', methods=['GET'])
def news_by_id(newsid):
    if request.method == 'GET':
        res = NewsApi.get_news_by_id(newsid)
        return res
    else:
        return 'Request Error!'


if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True)
