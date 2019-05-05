from app_init import app
from flask_pymongo import PyMongo
from bson import json_util
import jieba.analyse
import json

app.config['MONGO_URI'] = 'mongodb://localhost:27017/News'
mongo = PyMongo(app)


class NewsApi:
    @staticmethod
    def get_news():
        news_li = mongo.db.TencentNews.find({}, {'_id': 0}).sort([('publish_time', -1)])
        res = json_util.dumps(news_li)
        return res

    @staticmethod
    def get_news_by_view():
        news_li = mongo.db.TencentNews.find({}, {'_id': 0}).sort([('view_count', -1)]).limit(10)
        res = json_util.dumps(news_li)
        return res

    @staticmethod
    def get_news_by_id(id):
        news_li = mongo.db.TencentNews.find_one_or_404({'id': id}, {'_id': 0})
        res = json.loads(json_util.dumps(news_li))
        intro = res.get('intro').strip()
        hot_words = dict(jieba.analyse.extract_tags(intro, withWeight=True, topK=5, allowPOS=('n', 'nr', 'ns')))
        new_dict = {'res_body': res, 'hot_words': hot_words}
        res = json_util.dumps(new_dict)
        return res
