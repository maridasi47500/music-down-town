# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Jobscript(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists jobscript(
        id integer primary key autoincrement,
        job_id text,
            user_id text,
            name text
    ,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from jobscript")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from jobscript where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyuseridjobid(self,myid,jobid):
        self.cur.execute("select * from jobscript where user_id = ? and job_id = ?",(myid,jobid,))
        row=dict(self.cur.fetchone())
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from jobscript where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into jobscript (job_id,user_id,name) values (:job_id,:user_id,:name)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["jobscript_id"]=myid
        azerty["notice"]="votre jobscript a été ajouté"
        return azerty




