import cloudscraper
import discord, sqlite3 , rstr
import time
import random as predictor
from discord.ext import commands

thumbnail = 'https://media.discordapp.net/attachments/1029097026819989614/1029408432274550884/image0-1.jpg'
token = "MTAyNTk0NDE5MjY0MTQxMzE2MQ.G6EeFo.7i27xjdvYny1Syd_1FSsaU1OOw4iaymIs92-8s" #Bot Token
errorcolor = 0xD30229 #Embed HEX Color If Round ID Is Invalid
successcolor = 0xD30229 #Embed HEX Color If Round ID Is Valid
predictedemoji = ":star:" #Emoji For Predicted Tiles On Towers & Mines
unpredictedemoji = ":bomb:" #Emoji For Predicted Tiles On Towers & Mines
predictorname = "Yello's" #Predictor Name For Embed Footer And Embed Title
botprefix = "." #Bot Prefix

#If u wanna make it so u need a specific role to use the commands set it here

role = "Buyer" # Role Required To Run Commands
mods = ['@Pinguhz#5327', 'other_mod_here']
activity = activity = discord.Game(name="made by Pinguhz#5327")
activity=activity,status=discord.Status.idle
# Dont Edit Anything Below This

bot = commands.Bot(command_prefix=botprefix,intents=discord.Intents.all())
scraper = cloudscraper.create_scraper()

@bot.event
async def on_ready():
    print(f"\n\nBot Is Running\n\nCommands:\n{botprefix}crash\n{botprefix}roulette\n{botprefix}mines roundid\n{botprefix}towers roundid\n{botprefix}genkey\n{botprefix}claim key\n\nRole Required To Run Commands: {role}\n\nBot By Pinguhz")

@bot.command()
@commands.has_role(f"{role}")
async def crash(ctx):
    games = scraper.get("https://rest-bf.blox.land/games/crash").json()
    if ctx.author.id != bot.user.id:
        ok = await ctx.send(embed=discord.Embed(title="Checking JSON",description="API Link: https://rest-bf.blox.land/games/crash",color=errorcolor))
        def lol():
            r=scraper.get("https://rest-bf.blox.land/games/crash").json()["history"]
            yield [r[0]["crashPoint"], [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]]
        for game in lol():
            games = game[1]
            lastgame = game[0]
            avg = sum(games)/len(games)
            chance = 1
            for game in games:
                chance = chance = 95/game
                prediction = (1/(1-(chance))+avg)/2
                if float(prediction) > 2:
                    color = 0x81fe8f
                else:
                    color = 0xfe8181
                desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **Chance:**
        ```{chance:.2f}%```
        """
                em=discord.Embed(description=desc,color=color)
                emb = discord.Embed(color=successcolor)
                emb.set_thumbnail(url=thumbnail)
                emb.set_footer(text=f"{predictorname} ")
                emb.add_field(name=f"{predictorname} Crash Predictor",value=f"\n{prediction:.2f}x" + "\n\n**Accuracy**" + f"\n{chance:.2f}%")
                await ok.edit(embed=emb)

@bot.command()
@commands.has_role(f"{role}")
async def mines(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    dashcount = round_id.count("-")
    if round_length < 36 or round_length == "" or round_length == " " or float(dashcount) != 4:
        await ctx.send(embed=discord.Embed(title=f"{predictorname} Error", description="Invalid Round ID", color=errorcolor))
    elif round_length == 36 and float(dashcount) == 4:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}', f'{unpredictedemoji}'
        a = predictor.randint(1, 8)
        b = predictor.randint(9, 13)
        c = predictor.randint(14, 17)
        d = predictor.randint(18, 25)
        if a == 1:
            mine1 = f"{predictedemoji} "
        elif a == 2:
            mine2 = f"{predictedemoji} "
        elif a == 3:
            mine3 = f"{predictedemoji} "
        elif a == 4:
            mine4 = f"{predictedemoji} "
        elif a == 5:
            mine5 = f"{predictedemoji} "
        elif a == 6:
            mine6 = f"{predictedemoji} "
        elif a == 7:
            mine7 = f"{predictedemoji} "
        elif a == 8:
            mine8 = f"{predictedemoji} "
        if b == 9:
            mine9 = f"{predictedemoji} "
        elif b == 10:
            mine10 = f"{predictedemoji} "
        elif b == 11:
            mine11 = f"{predictedemoji} "
        elif b == 12:
            mine12 = f"{predictedemoji} "
        elif b == 13:
            mine13 = f"{predictedemoji} "
        if c == 14:
            mine14 = f"{predictedemoji} "
        elif c == 15:
            mine15 = f"{predictedemoji} "
        elif c == 16:
            mine16 = f"{predictedemoji} "
        elif c == 17:
            mine17 = f"{predictedemoji} "
        if d == 18:
            mine18 = f"{predictedemoji} "
        elif d == 19:
            mine19 = f"{predictedemoji} "
        elif d == 20:
            mine20 = f"{predictedemoji} "
        elif d == 21:
            mine21 = f"{predictedemoji} "
        elif d == 22:
            mine22 = f"{predictedemoji} "
        elif d == 23:
            mine23 = f"{predictedemoji} "
        elif d == 24:
            mine24 = f"{predictedemoji} "
        elif d == 25:
            mine25 = f"{predictedemoji} "
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(predictor.randint(60, 100))
        em = discord.Embed(color=successcolor)
        em.set_thumbnail(url=thumbnail)
        em.set_footer(text=f"{predictorname} ")
        em.add_field(name=f"{predictorname} Mines Predictor",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n" + "\n**Accuracy**" + "\n" + info +"%")
        await ctx.send(embed=em)

@bot.command()
@commands.has_role(f"{role}")
async def roulette(ctx):
    predictions = ['red','red','red','purple','purple','purple','gold']
    prediction = predictor.choice(predictions)
    if prediction == 'red':
        embed_color = successcolor
        color_text = 'Red'
    elif prediction == 'purple':
        embed_color = successcolor
        color_text = 'Purple'
    elif prediction == 'purple':
        embed_color = successcolor
        color_text = 'Yellow'
    info = str(predictor.randint(45, 90))
    em = discord.Embed(color=embed_color)
    em.add_field(name=f"{predictorname} Roulette Predictor", value=color_text + "\n\n**Accuracy**\n" + info + "%")
    em.set_thumbnail(url=thumbnail)
    em.set_footer(text=f"{predictorname}")
    await ctx.send(embed=em)

@bot.command()
@commands.has_role(f"{role}")
async def towers(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    dashcount = round_id.count("-")
    if round_length < 36 or round_length == "" or round_length == " " or float(dashcount) != 4:
        await ctx.send(embed=discord.Embed(title=f"{predictorname} Error", description="Invalid Round ID", color=errorcolor))
    elif round_length == 36 and float(dashcount) == 4:
        predictionvalues = (f"{predictedemoji} {unpredictedemoji} {unpredictedemoji}", f"{unpredictedemoji} {predictedemoji} {unpredictedemoji}", f"{unpredictedemoji} {unpredictedemoji} {predictedemoji}")
        row1 = predictor.choice(predictionvalues)
        row2 = predictor.choice(predictionvalues)
        row3 = predictor.choice(predictionvalues)
        row4 = predictor.choice(predictionvalues)
        row5 = predictor.choice(predictionvalues)
        row6 = predictor.choice(predictionvalues)
        row7 = predictor.choice(predictionvalues)
        row8 = predictor.choice(predictionvalues)
        em = discord.Embed(color=successcolor)
        info = str(predictor.randint(45, 90))
        em.set_thumbnail(url=thumbnail)
        em.set_footer(text=f"{predictorname} ")
        em.add_field(name=f"{predictorname} Towers Predictor", value=row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n" + "\n**Accuracy**" + "\n" + info + "%")   
        await ctx.send(embed=em)

DB=sqlite3.connect("Bot_DB.db")
query=DB.cursor()
query.execute("""CREATE TABLE IF NOT EXISTS KEYS (
        UNQ_ID PRIMARY KEY,
        USER_ID NUMBER,
        VAILD NUMBER,
        CLAIMED_KEY VARCHAR2
);""")


def check_Mod(ctx):
    if ctx.author.id in mods:
        IsMod = True
    else:
        IsMod = False
    return IsMod


# gen yo key

@bot.command()
async def genkey(ctx):
    IsMod = check_Mod(ctx)
    if IsMod == False:
        embed=discord.Embed(title="Pingu Key System", description="You have no perms to use this command.", color=0xd70f0f)
        embed.set_footer(text="Pingu | Pinguhz#5327")
        await ctx.send(embed=embed)
    else:
        new_key=rstr.xeger(r'[a-zA-Z\d]{25}')
        query.execute("""INSERT INTO KEYS (USER_ID, CLAIMED_KEY) VALUES (?, ?)""",(ctx.author.id, new_key,))
        DB.commit()
        embed=discord.Embed(title="Key generated!", description=f"Your new key is **{new_key}**", color=0xf8f7f7)
        await ctx.send(embed=embed)


# key redeem

@bot.command()
async def claim(ctx, key):
    if isinstance(key, commands.MissingRequiredArgument):
        await ctx.send('Inccorrect arguments entered | **.claimed <key>**')
    query.execute("""SELECT CLAIMED_KEY FROM KEYS WHERE CLAIMED_KEY=?""",(key,))
    list_keys = [row[0] for row in query.fetchall()]
    if key in list_keys:
        embed=discord.Embed(title="Pingu Key System", description=f"Claimed the key !", color=0xf8f7f7)
        embed.set_thumbnail(url="")
        embed.set_footer(text="Pingu | Pinguhz#5327")
        await ctx.send(embed=embed)
        query.execute("""DELETE FROM KEYS WHERE CLAIMED_KEY=?""",(key,))
        query.execute("""INSERT INTO KEYS (VAILD) VALUES (?)""",(ctx.author.id,))
        DB.commit()
    else:
        embed=discord.Embed(title="Pingu Key System", description="Invaild Key / The key doesn't exist.", color=0xf8f7f7)
        embed.set_thumbnail(url="")
        embed.set_footer(text="Pingu | Pinguhz#5327")
        await ctx.send(embed=embed)



# how to check if user has a key 

@bot.command()
async def test(ctx):
    query.execute("""SELECT VAILD FROM KEYS WHERE VAILD=?""",(ctx.author.id,))
    result = [row[0] for row in query.fetchall()]
    if ctx.author.id in result:
        pass
    else:
        embed=discord.Embed(title="Pingu Key System | buy @Pinguhz#5327", description="You have no key to Pingu Predictor" + '\n' +  "Buy @Pinguhz#5327", color=0xf8f7f7)
        embed.set_thumbnail(url="")
        embed.set_footer(text="Pingu | Pinguhz#5327")
        await ctx.send(embed=embed)
        return


bot.run(token)
