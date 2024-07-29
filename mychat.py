# coding=utf-8
import openai
import sqlite3
import sys
import re
from model import Model
from chat import Chat
class Mychat(Chat):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists chat(
        id integer primary key autoincrement,
        user_id text,
            me text,
            text text
    ,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from chat")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from chat where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def gettextbyuserid(self,myid,text):
        self.cur.execute("select * from chat where user_id = ?",(myid,))
        job=self.cur.fetchall()
        myarr=[]
        for x in job:
          myarr.append({
            'role':("user" if x["me"] == "1" else "system"),
            'content':x["text"],
          })
        model="gpt-3.5-turbo"
        openai.ChatCompletion.create(model=model, messages=myarr)

        text= response["choices"][-1]["0"]["message"]
        hey=self.create({"user_id":myid, "text":text,"me":"0"})
        return text
