import memcache
"""
windows:
schtasks /create /sc onstart /tn memcached /tr "'c:\memcached\memcached.exe' -m 512"
c:\memcached\memcached.exe -vv start
"""
# 分布式可以连接多个server ip
mc = memcache.Client(["127.0.0.1:11211"], debug=True)

mc.set('username', 'erdan', time=120)

mc.set_multi({'title': 'gangtiexia', 'content': 'hello world!'}, time=120)

# username = mc.get('username')
# print(username)

# mc.delete('username')
# username = mc.get('username')
# print(username)

mc.set('age', 18)
mc.incr('age', delta=10)
age = mc.get('age')
print(age)


