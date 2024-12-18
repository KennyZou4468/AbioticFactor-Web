import pymysql

conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="12345678",db="AbioticFactor")
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("select * from staff")
data_list=cursor.fetchall()
for i in data_list:
    print(i)
cursor.close()
conn.close()




