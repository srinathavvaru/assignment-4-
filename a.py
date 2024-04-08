import MySQLdb
conn=MySQLdb.Connect(host='localhost',database='test',user='system',password='anas1234')
print('Connectin Sucessfully Established')
c=conn.cursor()
c.execute("select * from emp1")
r=c.fetchall()
for row in r:
    print(row)
c.close()
conn.close()