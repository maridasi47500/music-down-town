from dotenv import load_dotenv
load_dotenv()
import openai
from openai import AsyncOpenAI
import asyncio
import torch
from transformers import pipeline


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
        self.con.commit()
        self.text=""
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from chat")

        row=self.cur.fetchall()
        return row
    async def hey(self,model="",messages=[]):
        client = AsyncOpenAI()
        reponse=await client.chat.completions.create(model=model, messages=messages)
        self.text=(reponse.choices[0].message.content)
    def deletebyid(self,myid):

        self.cur.execute("delete from chat where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def gettextbyuserid(self,myid):
        self.cur.execute("select * from chat where user_id = ?",(myid,))
        job=self.cur.fetchall()
        chat=[]
        text=""
        for x in job:
          chat.append({
            'role':("user" if x["me"] == "1" else "system"),
            'content':x["text"],
          })
        model="gpt-3.5-turbo"
        try:
            asyncio.run(self.hey(model=model, messages=chat))
            #print(dict(response))
            #print(list(response)) 
            #print(tuple(response))
            hey=self.create({"user_id":myid, "text":self.text,"me":"0"})
            return hey
        except:
            #except
            model="meta-llama/Meta-Llama-3-8B-Instruct"
            pipe = pipeline("text-generation", model, torch_dtype=torch.bfloat16, device_map="auto")
            response = pipe(chat, max_new_tokens=512)
            text=(response[0]['generated_text'][-1]['content'])
            hey=self.create({"user_id":myid, "text":self.text,"me":"0"})
            return hey
