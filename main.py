import discord
from discord.ext import commands
from discord import app_commands
import os
import random
from keep_alive import keep_alive

TOKEN=os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

list_ = ["⭕", "❌"]
list_1 = ['1️⃣', '2️⃣', '3️⃣']
list_2 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
list_3 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']

@bot.event
async def on_ready ():
    print("起動")

    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)}個のコマンドを同期")
    except Exception as e:
        print(e)

@bot.tree.command(name="yes-no")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="⭕   "+q1,value="",inline=False)
    embed.add_field(name="❌   "+q2,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_)):
     await message.add_reaction(list_[i])

@bot.tree.command(name="question3")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_1)):
     await message.add_reaction(list_1[i])
    return

@bot.tree.command(name="question4")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str, q4:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    embed.add_field(name="4   "+q4,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_2)):
     await message.add_reaction(list_2[i])
    return

@bot.tree.command(name="question5")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str, q4:str, q5:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    embed.add_field(name="4   "+q4,value="",inline=False)
    embed.add_field(name="5   "+q5,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_3)):
     await message.add_reaction(list_3[i])
    return

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
   embed = discord.Embed(description="## __Command description__")
   embed.add_field(name="/yes-no",value="投票を開始",inline=False)
   embed.add_field(name="`title`",value="投票のタイトル",inline=True)
   embed.add_field(name="`q1`",value="1つ目の回答を作成",inline=True)
   embed.add_field(name="`q2`",value="2つ目の回答を作成",inline=True)
   embed.add_field(name="/question",value="複数投票(q3～q5)を開始",inline=False)
   embed.add_field(name="`q1`",value="1つ目の回答を作成",inline=True)
   embed.add_field(name="`q2`",value="2つ目の回答を作成",inline=True)
   embed.add_field(name="`q3`",value="3つ目の回答を作成",inline=True)
   embed.add_field(name="/mc",value="Minecraft Serverの情報を表示",inline=False)
   embed.add_field(name="/omikuzi",value="おみくじを開始",inline=False)
   embed.add_field(name="/server",value="サーバー情報を表示",inline=False)
   embed.add_field(name="/user",value="ユーザー情報を表示",inline=False)
   user_id = "795470464909836329"
   member_list = list(bot.get_all_members())
   for i in range(len(member_list)):
        if str(member_list[i].id) == user_id:
            user = member_list[i]
   latte = f"{user._user.mention} "
   embed.add_field(name="⇩ご不明点",value=latte,inline=False)
   embed.set_author(name="py",icon_url="https://i.pinimg.com/564x/f2/bf/81/f2bf81b2bc34fbb6d5bc57dd33bfc551.jpg")
   await interaction.response.send_message(embed=embed,ephemeral=True)

@bot.tree.command(name="omikuzi")
async def omikuazi(interaction: discord.Interaction):
   text_random=random.choice(("大吉","中吉","小吉","吉","末吉","凶","大凶"))
   text_message=str(text_random)
   await interaction.response.send_message(text_message,ephemeral=True)

@bot.tree.command(name="mc")
async def mc(interaction: discord.Interaction): 
   embed = discord.Embed(description="### [MOD](https://d.kuku.lu/d87h2ccud) ＆ [Minecraft](https://www.youtube.com/watch?v=xt_1ASLcdY4)")
   embed.add_field(name="java : `java 17`",value="",inline=False)
   embed.add_field(name="mod : `dimension`",value="",inline=False)
   embed.add_field(name="ver : `FORGE 1.20.1`",value="",inline=False)
   embed.add_field(name="address : `black-tar.gl.joinmc.link`",value="",inline=False)
   embed.add_field(name="・黄昏の森",value="The Twilight Forest",inline=False)
   embed.add_field(name="・ディープアンドダーカー",value="Deeper and Darker",inline=False)
   embed.add_field(name="・ビヨンドアース",value="Beyond Earth",inline=False)
   embed.add_field(name="・ブルースカイズ",value="Blue Skies",inline=False)
   embed.add_field(name="・トロピクラフト",value="Tropicraft",inline=False)
   embed.add_field(name="・エーテル",value="The Aether",inline=False)
   user_id = "795470464909836329"
   member_list = list(bot.get_all_members())
   for i in range(len(member_list)):
        if str(member_list[i].id) == user_id:
            user = member_list[i]
   latte = f"{user._user.mention} "
   embed.add_field(name="⇩ご不明点",value=latte,inline=False)
   await interaction.response.send_message(embed=embed)

@bot.tree.command(name="server")
async def server(interaction: discord.Interaction): 
  guild = interaction.user.guild
  roles =[role for role in guild.roles]
  text_channels = [text_channels for text_channels in guild.text_channels]
  embed = discord.Embed(description="")
  embed.add_field(name="Adomin",value=f"{interaction.guild.owner}",inline=False)
  embed.add_field(name="ID",value=f"{interaction.guild.id}",inline=False)
  embed.add_field(name="Channel",value=f"{len(text_channels)}",inline=False)
  embed.add_field(name="Roll",value=f"{len(roles)}",inline=False)
  embed.add_field(name="Server Booster",value=f"{guild.premium_subscription_count}",inline=False)
  embed.add_field(name="Member",value=f"{guild.member_count}",inline=False)
  embed.add_field(name="Create Server",value=f"{guild.created_at}",inline=False)
  embed.add_field(name="Executor",value=f"{interaction.user}")
  await interaction.response.send_message(embed=embed)

@bot.tree.command(name="user")
async def user(interaction: discord.Interaction): 
  embed = discord.Embed(title=f"user {interaction.user.name}",description="userinfo")
  embed.add_field(name="Name",value=f"{interaction.user.mention}",inline=False)
  embed.add_field(name="ID",value=f"{interaction.user.id}",inline=False)
  embed.add_field(name="ACTIVITY",value=f"{interaction.user.activity}",inline=False)
  embed.add_field(name="TOP_ROLE",value=f"{interaction.user.top_role}",inline=False)
  embed.add_field(name="Discriminator",value=f"#{interaction.user.discriminator}",inline=False)
  embed.add_field(name="Join Server",value=f"{interaction.user.joined_at.strftime('%d.%m.%Y, %H:%M Uhr')}",inline=False)
  embed.add_field(name="Create Account",value=f"{interaction.user.created_at.strftime('%d.%m.%Y, %H:%M Uhr')}",inline=False)
  embed.set_thumbnail(url=f"{interaction.user.avatar.url}")
  embed.add_field(name="Executor",value=f"{interaction.user}")
  await interaction.response.send_message(embed=embed)
keep_alive()
  
bot.run(TOKEN)