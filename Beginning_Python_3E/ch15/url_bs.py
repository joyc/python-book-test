# 用Beautiful Soup的抓取
from urllib.request import urlopen
from bs4 import BeautifulSoup


text = urlopen('http://python.org/jobs').read()
soup = BeautifulSoup(text, 'html.parse')

jobs = set()
for job in soup.body.section('h2'):
    jobs.add('{} ({})'.format(job.a.string, job.a['href']))

print('\n'.join(sorted(jobs), key=str.lower))
