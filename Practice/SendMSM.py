# !/usr/bin/env python3
# *coding:utf-8*
__author__ = 'loaderlin'

import requests
import time
import hashlib
import json


class SendMessage(object):

    def __init__(self, accountsid, token):
        self.token = token
        self.accountSid = accountsid
        self.url = "https://api.miaodiyun.com/20150822/industrySMS/sendSMS"
        self.timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

    def send_sms(self, code, mobile):
        params = {
            "accountSid": self.accountSid,
            "templateid": "146697495",
            "param": code,
            "to": mobile,
            "timestamp": self.timestamp,
            "sig": hashlib.md5((self.accountSid + self.token + self.timestamp).encode('utf-8')).hexdigest(),
        }
        response = requests.post(self.url, data=params)
        re_dict = json.loads(response.text)

        return re_dict

if __name__ == "__main__":
    # from util.SendSMS import SendMessage
    # from Book.settings import ACCOUNT_SID, TOKEN
    # sendmessage = SendMessage(ACCOUNT_SID, TOKEN)
    # sms_status = sendmessage.send_sms(code=code, mobile=mobile)
    # if sms_status['respCode'] != "00000":
        # return Response({}, status=status.HTTP_400_BAD_REQUEST)