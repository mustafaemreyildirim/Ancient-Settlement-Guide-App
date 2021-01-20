import psycopg2
from flask_login import UserMixin


con = psycopg2.connect("dbname='d35q9ogcrt02v1' user='zlcsxccctwmvdp' host='ec2-34-194-198-238.compute-1.amazonaws.com' password='b2b27bc4b07b3b309412b7c51e0483eaea106ba964509517379406b3ae762bf4'")
cur = con.cursor()

cur.execute("ROLLBACK")
con.commit()

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

    def insert(self):
        
        cur.execute("INSERT INTO \"user\" (username,password,email,createdate,name,surname) VALUES(  %s,%s,%s,%s,%s,%s)" ,(self.username,self.password,self.email,self.createdate,self.name,self.surname))
        con.commit()

    
    @property
    def is_active(self):
        return self.active
    


def get_user(username):
    
    
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

    def insert(self):
        
        cur.execute("INSERT INTO \"contributor\" (username,password,email,createdate,name,surname,university,researcharea) VALUES(  %s,%s,%s,%s,%s,%s,%s,%s)" ,(self.username,self.password,self.email,self.createdate,self.name,self.surname,self.university,self.researcharea))
        con.commit()

    
    @property
    def is_active(self):
        return self.active
    


def get_cont(username):
    
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

    def insert(self):
        
        
        cur.execute("INSERT INTO \"region\" (region) VALUES(  %s)" ,(self.region,))
        con.commit()

def get_reg(region):
    
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
    def __init__(self,knownperson) :
        self.active = True
        self.knownperson = knownperson

    def get_knownperson(self):
        return (self.knownperson)

    def insert(self):
        
        
        cur.execute("INSERT INTO \"famousperson\" (knownperson) VALUES(  %s)" ,(self.knownperson,))
        con.commit()



def kp_id_ret(kp_id):
    cur.execute("SELECT knownperson FROM \"famousperson\" WHERE  \"knownpersonid\"=(%s)",(kp_id,))
    rows =cur.fetchall()
    print("--------------------------------",len(rows))

    return rows[0][0]

def region_id_ret(reg_id):
    cur.execute("SELECT region FROM \"region\" WHERE  \"regionid\"=(%s)",(reg_id,))
    rows =cur.fetchall()
    return rows[0][0]

def civi_id_ret(civ_id):
    cur.execute("SELECT civilizationname FROM \"civilization\" WHERE  \"civid\"=(%s)",(civ_id,))
    rows =cur.fetchall()
    return rows[0][0]

def location_id_ret(location_id):
    cur.execute("SELECT location FROM \"location\" WHERE  \"locationid\"=(%s)",(location_id,))
    rows =cur.fetchall()
    print(rows)

    return rows[0][0]

def cont_id_ret(cont_id):
    cur.execute("SELECT username FROM \"contributor\" WHERE  \"contid\"=(%s)",(cont_id,))
    rows =cur.fetchall()
    return rows[0][0]

def get_fp(knownperson):
    
    cur.execute("SELECT * FROM \"famousperson\"  WHERE \"knownperson\" = (%s)",(knownperson,) )
    rows = cur.fetchall()
    if len(rows)>0:
        knownperson = rows[0][1]
        
        con.commit()
        fp = Knownp_remade(knownperson)
    
    else: 
        return None
    return fp


class Civi_remade():
    def __init__(self,civilizationname,goldenage,knownperson) :
        self.active = True
        self.civilizationname = civilizationname
        self.goldenage = goldenage
        self.knownperson = knownperson


    def get_civilizationname(self):
        return (self.civilizationname)

    def insert(self):
        
        
        cur.execute("INSERT INTO \"civilization\" (civilizationname,goldenage,knownpersonid) VALUES(  %s,%s,(SELECT knownpersonid FROM \"famousperson\" WHERE \"knownperson\"=%s))" ,(self.civilizationname,self.goldenage,self.knownperson))
        con.commit()

def get_civi(civilizationname):
    
    cur.execute("SELECT * FROM \"civilization\"  WHERE \"civilizationname\" = (%s)",(civilizationname,) )
    rows = cur.fetchall()
    if len(rows)>0:
        civilizationname = rows[0][1]
        goldenage =  rows[0][2]
        knowperson = kp_id_ret(rows[0][3])
        
        con.commit()
        fp = Civi_remade(civilizationname,goldenage,knowperson)
    
    else: 
        return None
    return fp




class Location_remade():
    def __init__(self,location,region) :
        self.active = True
        self.location = location
        self.region = region


    def get_location(self):
        return (self.location)

    def insert(self):
        
        cur.execute("INSERT INTO \"location\" (location,regionid) VALUES(  %s,(SELECT regionid FROM \"region\" WHERE \"region\"=%s))" ,(self.location,self.region))
        con.commit()

def get_loc(location):
    
    cur.execute("SELECT * FROM \"location\"  WHERE \"location\" = (%s)",(location,) )
    rows = cur.fetchall()
    if len(rows)>0:
        location = rows[0][1]
        region = region_id_ret(rows[0][2])
        
        con.commit()
        fp = Location_remade(location,region)
    
    else: 
        return None
    return fp

class AnSett_remade():
    def __init__(self,cityname,username,location,civilizationname,description,setimg) :
        self.active = True
        self.cityname = cityname

        self.location = location
        self.username = username
        self.civilizationname=civilizationname
        self.description=description
        self.setimg=setimg

    

    def get_cityname(self):
        return (self.cityname)

    def insert(self):
        
        cur.execute("INSERT INTO \"ancientsettlement\" (cityname,contid,locationid,civid,description,setimg) VALUES ( (%s),(SELECT contid FROM \"contributor\" WHERE \"username\"=%s),(SELECT locationid FROM \"location\" WHERE \"location\"=%s),(SELECT civid FROM \"civilization\" WHERE \"civilizationname\"=%s),%s,%s)",(self.cityname,self.username,self.location,self.civilizationname,self.description,self.setimg))
        con.commit()

def get_set(cityname):
    
    cur.execute("SELECT * FROM \"ancientsettlement\"  WHERE \"cityname\" = (%s)",(cityname,) )
    rows = cur.fetchall()
    if len(rows)>0:
        cityname = rows[0][1]
        username = cont_id_ret(rows[0][2])
        location = location_id_ret(rows[0][3]) 
        civilizationname = civi_id_ret(rows[0][4]) 
        description = rows[0][5]
        setimg = rows[0][6]        
        con.commit()
        fp = AnSett_remade(cityname,username,location,civilizationname,description,setimg)
    
    else: 
        return None
    return fp



class Path_remade():
    def __init__(self,pathname,artifact,civilizationname,location,pathimg) :
        self.active = True
        self.pathname = pathname

        self.artifact = artifact
        self.civilizationname=civilizationname
        self.location=location
        self.pathimg=pathimg

    

    def get_pathname(self):
        return (self.pathname)

    def insert(self):
        
        cur.execute("INSERT INTO \"paths\" (pathname , artifacts , civid , locationid , pathimg) VALUES ( (%s),(%s),(SELECT civid FROM \"civilization\" WHERE \"civilizationname\"=%s),(SELECT locationid FROM \"location\" WHERE \"location\"=%s),%s)",(self.pathname,self.artifact,self.civilizationname,self.location,self.pathimg))
        con.commit()

def get_path(pathname):
    
    cur.execute("SELECT * FROM \"paths\"  WHERE \"pathname\" = (%s)",(pathname,) )
    rows = cur.fetchall()
    if len(rows)>0:
        pathname = rows[0][1]
        artifact = rows[0][2]
        civilizationname = civi_id_ret(rows[0][3]) 
        location = location_id_ret(rows[0][4]) 
        pathimg = rows[0][5]
        con.commit()
        fp = Path_remade(pathname,artifact,civilizationname,location,pathimg)
    
    else: 
        return None
    return fp


def bring_all_cities():

    cur.execute("SELECT an.cityname,civ.civilizationname, civ.goldenage,kp.knownperson,con.username,loc.location,reg.region,an.description,an.setimg FROM civilization AS civ LEFT JOIN famousperson AS kp ON civ.knownpersonid = kp.knownpersonid LEFT JOIN ancientsettlement as an ON an.civid=civ.civid LEFT JOIN contributor AS con ON con.contid = an.contid LEFT JOIN location AS loc ON loc.locationid = an.locationid LEFT JOIN region as reg ON loc.regionid = reg.regionid;")
    rows = cur.fetchall()
    ls = []
    for i in range(len(rows)):
        if any(x is None for x in rows[i])==False:
            ls.append(rows[i])
    
    return ls


def bring_all_paths():

    cur.execute("SELECT pa.pathname,pa.artifacts,civ.civilizationname,civ.goldenage,kp.knownperson,loc.location,reg.region FROM paths AS pa LEFT JOIN civilization AS civ ON pa.civid = civ.civid LEFT JOIN famousperson as kp ON kp.knownpersonid=civ.knownpersonid LEFT JOIN location as loc ON loc.locationid = pa.locationid LEFT JOIN region as reg ON reg.regionid = loc.regionid;")
    rows = cur.fetchall()
    ls = []
    for i in range(len(rows)):
        if any(x is None for x in rows[i])==False:
            ls.append(rows[i])
    
    return ls

