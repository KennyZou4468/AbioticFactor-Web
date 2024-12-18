import pymysql

conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="12345678",db="AbioticFactor")
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("delete from staff where name = %s",["zmoke"])
conn.commit()
cursor.close()
conn.close()




