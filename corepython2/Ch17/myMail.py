#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
通过SMTP邮件服务器发送一封测试电子邮件到目的地址，
并马上（通过POP）把电子邮件从服务器上收回来。
"""
from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'

origHdrs = ['From: wesley@python.is.cool',
            'To: wesley@python.is.cool',
            'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('wesley@python.is.cool',
                        ('wesley@python.is.cool', ), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)   # wait for mail to be delivered

recvSvr = POP3(POP3SVR)
recvSvr.user('wesley')
recvSvr.pass_('youllNeverGuess')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody # assert identical
