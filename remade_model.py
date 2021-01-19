import psycopg2
from flask_login import UserMixin


class User_remade(UserMixin):

    def __init__(self,username,password,email,createdate,name,surname   ) :
        self.username = username
        self.password = password
        self.email = email
        self.createdate = createdate

        self.name = name
        self.surname = surname

 

    def insert(self):
        con = psycopg2.connect("dbname='d35q9ogcrt02v1' user='zlcsxccctwmvdp' host='ec2-34-194-198-238.compute-1.amazonaws.com' password='b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4'")
        cur = con.cursor()
        
        cur.execute("ROLLBACK")
        con.commit()
        
        cur.execute("INSERT INTO \"user\" (username,password,email,createdate,name,surname) VALUES(  %s,%s,%s,%s,%s,%s)" ,(self.username,self.password,self.email,self.createdate,self.name,self.surname))
        con.commit()

    

    