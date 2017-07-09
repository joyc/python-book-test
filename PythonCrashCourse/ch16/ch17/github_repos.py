#! python3
# -*- coding:utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 设置查询语言并执行 API
language = 'php'
url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# 设置变量存储返回内容
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 获取相关仓库信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    description = repo_dict['description']
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,Projects on GitHab
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 将获取排行可视化
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 22
my_style.label_font_size = 12
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Starred ' + language.title() + ' Projects on GitHab'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('%s_repos.svg' %(language))