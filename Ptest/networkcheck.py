#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/18/0018 0:38
# @Author  : Hython.com
# @File    : networkcheck.py
#!/usr/bin/python 
#coding=utf-8 
from _winreg import *
import urllib
import json

def val2addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x " % ord(ch))
        addr = addr.strip(" ").replace(" ", ":")[0:17]
    return addr

def printNets():
    net = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print("\nNetworks You have Joined.")
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, addr, t) = EnumValue(netKey, 5)
            (n, name, t) = EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = name
            jsondata = urllib.urlopen('http://api.cellocation.com:81/wifi/?mac='+macAddr+'&output=json').read()
            data = json.loads(jsondata)['address']
            if data =='':
                address = 'unknow'
            else:
                address = data
            print('[+] ' + netName + '  ' + macAddr+' '+address)
            CloseKey(netKey)
        except:
            break


def main():
    printNets()
    input('please press enter')

if __name__ == '__main__':
    main()