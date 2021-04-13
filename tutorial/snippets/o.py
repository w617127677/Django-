import pymysql

db = pymysql.connect(host='localhost', user='root', password='zxc123456', port=3306,db='taobao')
cursor = db.cursor()
sql = ' ALTER TABLE ggooo ADD iq INT(16) NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST'
cursor.execute(sql)