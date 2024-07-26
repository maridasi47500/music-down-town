# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Song(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists song(
        id integer primary key autoincrement,
        artist text,
            title text,
            image text,
            filename text,
            mytext text,
            link text
    , MyTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def track_list_some_songs(self):
        self.cur.execute("select * from song where lower(artist) like '%presley%'")
        malist=[]

        row=self.cur.fetchall()
        for x in row:
            malist.append({
            "id": x["id"],
            "name": x["title"],
            "link": x["link"],
            "mytext": x["mytext"],
            "artist": x["artist"],
            "image": ("/uploads/"+x["image"] or "https://source.unsplash.com/Qrspubmx6kE/640x360"),
            "path": "/uploads/"+x["filename"]
            })

        #xx=select("songs.*").where("lower(songs.title) not like '%barbie%' and (select count(idontlikes.id) from idontlikes where idontlikes.song_id = songs.id) = 0").to_a.shuffle.map do |x|
        return malist
    def track_list(self):
        self.cur.execute("select * from song")
        malist=[]

        row=self.cur.fetchall()
        for x in row:
            malist.append({
            "id": x["id"],
            "name": x["title"],
            "artist": x["artist"],
            "link": x["link"],
            "mytext": x["mytext"],
            "image": ("/uploads/"+x["image"] or "https://source.unsplash.com/Qrspubmx6kE/640x360"),
            "path": "/uploads/"+x["filename"]
            })

        #xx=select("songs.*").where("lower(songs.title) not like '%barbie%' and (select count(idontlikes.id) from idontlikes where idontlikes.song_id = songs.id) = 0").to_a.shuffle.map do |x|
        return malist
    def getall(self):
        self.cur.execute("select * from song")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from song where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyname(self,myid):
        self.cur.execute("select * from song where title = ?",(myid,))
        row=None
        try:
          row=dict(self.cur.fetchone())
        except:
          row=None
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from song where id = ?",(myid,))
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
          self.cur.execute("insert into song (link,mytext,artist,title,filename,image) values (:link,:mytext,:artist,:title,:filename,:image)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["song_id"]=myid
        azerty["notice"]="votre song a été ajouté"
        return azerty




