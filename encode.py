# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         encode
# Description:  
# Author:       guohuanyang
# Date:         2021/12/15
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import hashlib
import base64

username = 'songcai'
tmpAuthString = username + '_cms_datagrand'
print(tmpAuthString)
tmpAuthBytes = bytes(tmpAuthString, encoding='utf-8')
print(tmpAuthBytes)
sha1 = hashlib.sha1(tmpAuthBytes)
tmpHashedAuthBytes = sha1.digest()
# tmpHashedAuthBytes = bytes(tmpHashedAuthBytes, encoding='utf-8')
print(tmpHashedAuthBytes)
tmpHashedString = str(base64.b64encode(tmpHashedAuthBytes), encoding='utf-8')
print(tmpHashedString)

aaa = base64.b64decode(tmpHashedString)
print(aaa)