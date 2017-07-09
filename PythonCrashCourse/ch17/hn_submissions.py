#! python3
# -*- coding:utf-8 -*-
import requests
from operator import itemgetter

# 执行 API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对每篇文章执行一个 API 调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'link': 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id),
        'comments': response_dict.get('descendants', 0) # dict.get（）不确定字典中是否有 key 时候，如果没有这里返回0
    }
    submission_dicts.append(submission_dict)
    # 使用 operator 中的 itemgetter 函数取每个字典中的 comments 相关值后降排列
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Conmments:", submission_dict['comments'])