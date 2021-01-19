import psycopg2
from flask_login import UserMixin


class User_remade(UserMixin):

    def __init__(self,username,password,email,createdate,name,surname):
        self.active = True
        self.username= username
        self.password = password
        self.email = email
        self.createdate = createdate
        self.name = name
        self.surname = surname
    
    def get_id(self):
        return self.username
    def get_username(self):
        return (self.username)

    def insert(self,con,cur):
        
        cur.execute("INSERT INTO \"user\" (username,password,email,createdate,name,surname) VALUES(  %s,%s,%s,%s,%s,%s)" ,(self.username,self.password,self.email,self.createdate,self.name,self.surname))
        con.commit()

    
    @property
    def is_active(self):
        return self.active
    


def get_user(username):
    
    con = psycopg2.connect("dbname='d35q9ogcrt02v1' user='zlcsxccctwmvdp' host='ec2-34-194-198-238.compute-1.amazonaws.com' password='b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4'")
    cur = con.cursor()
    
    cur.execute("ROLLBACK")
    con.commit()
    cur.execute("SELECT * FROM \"user\"  WHERE \"username\" = (%s)",(username,) )
    rows = cur.fetchall()
    if len(rows)>0:
        username = rows[0][1]
        password = rows[0][2]
        email = rows[0][3]
        createdate = rows[0][4]
        name = rows[0][5]
        surname = rows[0][6]
        prfimg = rows[0][7]
        con.commit()
        user = User_remade(username,password,email,createdate,name,surname)
    else:
        return None    
    return user


class Cont_remade(UserMixin):

    def __init__(self,username,password,email,createdate,name,surname,university,researcharea):
        self.active = True
        self.username= username
        self.password = password
        self.email = email
        self.createdate = createdate
        self.name = name
        self.surname = surname
        self.university = university
        self.surname = surname
        self.researcharea = researcharea
    
    def get_id(self):
        return self.username
    def get_username(self):
        return (self.username)

    def insert(self,con,cur):
        
        cur.execute("INSERT INTO \"contributor\" (username,password,email,createdate,name,surname,university,researcharea) VALUES(  %s,%s,%s,%s,%s,%s,%s,%s)" ,(self.username,self.password,self.email,self.createdate,self.name,self.surname,self.university,self.researcharea))
        con.commit()

    
    @property
    def is_active(self):
        return self.active
    


def get_cont(username,con,cur):
    
    cur.execute("SELECT * FROM \"contributor\"  WHERE \"username\" = (%s)",(username,) )
    rows = cur.fetchall()
    if len(rows)>0:
        username = rows[0][1]
        password = rows[0][2]
        email = rows[0][3]
        createdate = rows[0][4]
        name = rows[0][5]
        surname = rows[0][6]
        university = rows[0][7]
        researcharea = rows[0][8]
        prfimg = rows[0][9]
        con.commit()
        cont = Cont_remade(username,password,email,createdate,name,surname,university,researcharea)
    
    else: 
        return None
    return cont


class Region_remade():
    def __init__(self,region) :
        self.active = True
        self.region = region

    def get_region(self):
        return (self.region)

    def insert(self,con,cur):
        
        
        cur.execute("INSERT INTO \"region\" (region) VALUES(  %s)" ,(self.region))
        con.commit()

def get_reg(region,con,cur):
    
    cur.execute("SELECT * FROM \"region\"  WHERE \"region\" = (%s)",(region,) )
    rows = cur.fetchall()
    if len(rows)>0:
        region = rows[0][1]
        
        con.commit()
        reg = Region_remade(region)
    
    else: 
        return None
    return reg



class Knownp_remade():
    def __init__(self,region) :
        self.active = True
        self.knownperson = region

    def get_region(self):
        return (self.region)

    def insert(self,con,cur):
        con = psycopg2.connect("dbname='d35q9ogcrt02v1' user='zlcsxccctwmvdp' host='ec2-34-194-198-238.compute-1.amazonaws.com' password='b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4'")
        cur = con.cursor()
        
        cur.execute("ROLLBACK")
        con.commit()
        
        cur.execute("INSERT INTO \"famousperson\" (region) VALUES(  %s)" ,(self.knownperson))
        con.commit()

def get_fp(knownperson,con,cur):
    
    cur.execute("SELECT * FROM \"famousperson\"  WHERE \"knownperson\" = (%s)",(knownperson,) )
    rows = cur.fetchall()
    if len(rows)>0:
        region = rows[0][1]
        
        con.commit()
        fp = Region_remade(knownperson)
    
    else: 
        return None
    return fp