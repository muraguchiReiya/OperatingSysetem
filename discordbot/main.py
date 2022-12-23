# -*- coding: utf-8 -*-
import os
import re
import discord
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime, timedelta, timezone
from db import DB
import mysql.connector

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
db_name=os.getenv('DB')
user_name=os.getenv('USER_NAME')
host_name=os.getenv('HOST')
user_password=os.getenv('PASS')
bot=commands.Bot(command_prefix="!")
db=DB(db_name,user_password,user_name,host_name)

@bot.event
async def on_ready():
    print('起動完了')
    
@bot.command()
async def test(ctx):
    print('test')
    await ctx.send("test.OK!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    reg_res=re.compile(r'^(\d{4})-(\d{4})').search(message.content)
    if(reg_res):
        m = re.match(r'^(\d{4})-(\d{4})', message.content)

        now=datetime.now()
        print(now)
        work_time=time(m.group(1),m.group(2))
        query=f"INSERT INTO IR VALUES('{message.author.id}','{message.author.name}',{now.year},{now.month},{now.day},{work_time},{m.group(1)},{m.group(2)},'{message.content[10:]}')"
        print(query)
        con=db.conect_db()
        con=db.create_db_connection()
        msg=db.execute_query(con,query)
        await message.channel.send(msg)
    elif(re.compile(r'^\d+月の集計').search(message.content)):
        m = re.match(r'^(\d*)月の集計', message.content)
        query=f"SELECT name,SUM(time) FROM IR WHERE month={m.group(1)} GROUP BY name;"
        print(query)
        con=db.conect_db()
        con=db.create_db_connection()
        results=db.read_query(con,query)
        embed = discord.Embed(title=f"{m.group(1)}月集計結果")
        embed.set_author(name="勤務管理bot")
        for result in results:
            embed.add_field(name=result[0],value=f"{result[1]}時間",inline=False)
        await message.channel.send(embed=embed)
    elif(message.content=="テーブル一覧"):
        query="SELECT * FROM IR;"
        con=db.conect_db()
        con=db.create_db_connection()
        results=db.read_query(con,query)
        embed = discord.Embed(title="IRテーブル")
        embed.set_author(name="勤務管理bot")
        name=""
        work=""
        content=""
        for result in results:
            result=list(result)
            name+=result[1]+"\n"
            work+=f"{result[5]}時間\n"
            content+=result[8]+"\n"
        embed.add_field(name="名前",value=name,inline=True)
        embed.add_field(name="勤務時間",value=work,inline=True)
        embed.add_field(name="勤務内容",value=content,inline=True)
        await message.channel.send(embed=embed)
    else:
        pass

def time(start,end):
    try:
        startT = datetime.strptime(start,'%H%M')
        endT = datetime.strptime(end,'%H%M')
        time=endT-startT
        time=float(time.total_seconds())/60/60
        return round(time,3)
    except ValueError as e:
        return e
bot.run(TOKEN)
