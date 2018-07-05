#encoding: utf-8

from redis import Redis

cache = Redis(host='127.0.0.1', port=6379)  # 可加密码

# 1. 操作字符串
# cache.set('username', 'erdan')
# print(cache.get('username'))

# 2. 列表的操作
# cache.lpush('languages', 'chinese')
# cache.lpush('languages', 'japanese')
# cache.lpush('languages', 'english')
# print(cache.lrange('languages', 0, -1))

# 3. 集合的操作
# cache.sadd('team', 'li')
# cache.sadd('team', 'wang')
# cache.sadd('team', 'zhang')
# print(cache.smembers('team'))

# 4. 哈希的操作
# cache.hset('website', 'baidu', 'www.baidu.com')
# cache.hset('website', 'google', 'www.google.com')
# print(cache.hgetall('website'))

# 5. 事务的操作
# pip = cache.pipeline()
# pip.set('username', 'sandan')
# pip.set('password', 'nicaicai')
# pip.execute()
# print(cache.get('username'))

# 6. 订阅和发布功能操作
# 异步发送邮件的功能
ps = cache.pubsub()
ps.subscribe('email')
while True:
    for item in ps.listen():
        # print(item)
        if item['type'] == 'message':
            data = item['data']
            print(data)
            # 发送邮件
