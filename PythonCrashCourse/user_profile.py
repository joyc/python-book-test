#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/03 0:51
# @Author  : Hython.com
# @File    : user_profile.py
# @IDE     : PyCharm

def build_profile(first, last, **user_info):
    """创建一个字典"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einistein',
                             location = 'princeton',
                             field='physics')

print(user_profile)