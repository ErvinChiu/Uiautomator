# _*_coding:utf-8_*_
# @Time    :2022/3/321:10
# @Author  :ErvinChiu
# @Email   :ErvinChiu@outlook.com
# @File    :12.py
# @Sofeware:PyCharm
import  sqlite3
con = sqlite3.connect(r'D:\guest3\guest3\db.sqlite3')
cur = con.cursor()
cur.execute("select phone from sign_guest")
phones = cur.fetchall()
for phone in phones:
    print (phone)
cur.close()
con.close()