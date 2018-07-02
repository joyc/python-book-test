from blinker import Namespace
from datetime import datetime
from flask import request, g

namespace = Namespace()

login_signal = namespace.signal('login')


def login_log(sender):
    print('用户登陆了！')
    # 记录用户名，登陆时间，IP地址
    now = datetime.now()
    ip = request.remote_addr
    log_line = f"{g.username}-{now}-{ip}"
    with open('login_log.txt', 'a') as fp:
        fp.write(log_line+"\n")


login_signal.connect(login_log)
