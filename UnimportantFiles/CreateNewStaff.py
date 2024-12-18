import pymysql

conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="12345678",db="AbioticFactor")
cursor = conn.cursor()
sql="insert into staff(name,password,authorized) values(%s,%s,%s)"
cursor.execute(sql,["zmoke","666","1"])
conn.commit()
cursor.close()
conn.close()
