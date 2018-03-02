import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import math
from config import *

Client = discord.Client()
prefix= "w."
client = commands.Bot(command_prefix=prefix)

startup_extensions = ["roledescriptions","gamecommands"]

game_channel = client.get_channel("392995027909083137")
voting_channel = client.get_channel("393470084217176075")
notes_channel = client.get_channel("393476547954212874")
dead_channel = client.get_channel("392995124423950344")

global Day, PlayerInfo
Day = False
PlayerInfo = []

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name="Say w.help"))
    chan = client.get_channel("392995207894925313")
    await client.send_message(chan, "WolfieBot online!")

client.remove_command("help")

@client.command(pass_context=True)
async def help(ctx):
    await client.say("""Hi there! My name is **Wolfie**! I'm the (WIP) bot for the **Werewolf Server** built by **Army** :3. This is what I can do:
```md
<w.help> - Shows this message.
<w.gm_help> - Shows commands available for GMs only.
<w.gamerules> - Provides a link to the rules for playing the game.
<w.rolelist> - Provides a list of roles in the game, plus commands to see more information.
<w.generatelist> - Shows commands to generate rolelists.
<w.randomchoice (comma seperated list of options)> - Randomly chooses from given options.
<w.randomrole (space seperated list of tags as parameters)> - Randomly gives a role that has all the tags provided.
<w.listroles (space seperated list of tags as parameters)> - Lists all roles that have all the tags provided.
<w.flip (number of coins to flip)> - Flips a specified amount of coins.
<w.roll (#d#)> - Rolls specified dice.
<w.vote (options to vote between seperated by commas)> - Displays a list of specified options to vote on.
<w.score (wins:loses)> - Displays score for given statistics.
<w.icon (role)> - Displays icon for given role.```""")

@client.command(pass_context=True)
async def gm_help(ctx):
    await client.say("""```md
<w.setplayers (mentions)> - Sets all users mentioned as Player.
<w.gamestatus> - Returns all players in the current game with information about them. 
<w.giveroles (player: role, etc)> - Gives players listed the applied role.
<w.playervote> - Creates a vote in #voting for the players.
<w.daytimer (n; seconds; announcements)> - Sets a timer for the day, unlocks #game at start, locks #game when it ends. Seperate lines in announcements with /.
<w.night> - Ends day.
<w.mayor (@player)> - Sets given player as Mayor.
<w.deputy (@player)> - Sets given player as Deputy.
<w.kill (@player)> - Kills the given player.
<w.lockjaw (@player boolean)> - If boolean true, lockjaws player; if false, unlockjaws player.
<w.medium (@player boolean)> - If boolean true, gives player perms to see #dead; if false, removes perms.```""")

@client.command(pass_context=True)
async def gamerules(ctx):
    embed=discord.Embed(description="""This link details the rules for playing Werewolf.
If you have any questions or suggestions for improvement on the rules, contact Army with them. They'll be happy to help!
(If on mobile, press on the icon to access the document.)""")
    embed.set_author(name="Werewolf Party Game Rules", url='https://docs.google.com/document/d/1yPUNomeB7Fpw5iXS9J9QOITFU6jWstxIOCnXorfhV3s/edit?usp=sharing', icon_url='https://i.imgur.com/soFqp3g.png')
    await client.say(embed=embed)

@client.command(pass_context=True)
async def rolelist(ctx):
    await client.say("""__**Roles**__
```md
[+][Alchemist] - Neutral, Chaos, Human, Unique - <w.roles_alchemist>
[+][Arsonist] - Neutral, Killing, Human, Unique - <w.roles_arsonist>
[+][Backstabber] - Evil, Counteractive/Killing, Human, Unique - <w.roles_backstabber>
[+][Bard] - Neutral, Chaos/Killing, Human, Unique - <w.roles_bard>
[+][Companion] - Modifier, Achievable - <w.roles_companion>
[+][Cultist] - Evil, Counteractive/Support, Human, Unique - <w.roles_cultist>
[+][Cyberhound] - Evil, Counteractive/Killing, Wolf, Unique, Achievable - <w.roles_cyberhound>
[+][Dentist] - Evil, Counteractive, Human, Unique - <w.roles_dentist>
[+][Dire Wolf] - Evil, Killing/Support, Wolf, Unique - <w.roles_direwolf>
[+][Doctor] - Good, Killing/Protective, Human - <w.roles_doctor>
[+][Dodomeki] - Evil, Investigative, Non-Human, Unique, Achievable - <w.roles_dodomeki>
[+][Drunk] - Neutral, Chaos, Human, Unique - <w.roles_drunk>
[+][Fate] - Neutral, Chaos, Non-Human, Unique - <w.roles_fate>
[+][Feral] - Modifier - <w.roles_feral>
[+][Gladiator] - Good, Counteractive/Killing, Human, Unique - <w.roles_gladiator>
[+][Glazier] - Good, Counteractive, Non-Human - <w.roles_glazier>
[+][Guide] - Modifier, Achievable - <w.roles_guide>
[+][Hacker] - Good, Investigative/Support, Human, Unique, Achievable - <w.roles_hacker>
[+][Hangman] - Neutral, Chaos/Counteractive, Human, Unique - <w.roles_hangman>
[+][Heir] - Evil, Counteractive, Human, Unique - <w.roles_heir>
[+][Herald] - Neutral, Chaos/Killing, Non-Human, Unique, Achievable - <w.roles_herald>
```""")
    await client.say("""```md
[+][Hermit] - Neutral, Investigative/Counteractive, Human, Unique - <w.roles_hermit>
[+][Hooligan] - Evil, Killing/Support, Human - <w.roles_hooligan>
[+][Hunter] - Good, Killing/Protective, Human - <w.roles_hunter>
[+][Inevitable] - Neutral, Chaos/Killing, Non-Human, Unique, Achievable - <w.roles_inevitable>
[+][Inventor] - Neutral, Chaos/Killing, Human, Unique - <w.roles_inventor>
[+][Jailor] - Good, Counteractive/Protective, Human, Unique - <w.roles_jailor>
[+][Jester] - Evil, Chaos/Killing, Non-Human - <w.roles_jester>
[+][Knight] - Good, Killing/Support, Human, Unique - <w.roles_knight>
[+][Mage] - Good, Chaos/Investigative, Human - <w.roles_mage>
[+][Maid] - Neutral, Support, Human, Unique - <w.roles_maid>
[+][Medium] - Good, Support, Human - <w.roles_medium>
[+][Merchant] - Neutral, Chaos/Support, Human, Unique - <w.roles_merchant>
[+][Minstrel] - Modifier, Achievable - <w.roles_minstrel>
[+][Morty] - Modifier - <w.roles_morty>
[+][Multiple Agent] - Neutral, Chaos/Protective, Human - <w.roles_multipleagent>
[+][Noir] - Good, Investigative/Killing, Human, Unique - <w.roles_noir>
[+][Page] - Neutral, Support, Human, Unique - <w.roles_page>
[+][Paladin] - Good, Human, Counteractive/Protective, Unique, Achievable - <w.roles_paladin>
[+][Philanthropist] - Neutral, Counteractive/Support, Human, Unique - <w.roles_philanthropist>
[+][Pixie] - Good, Counteractive/Investigative, Non-Human - <w.roles_pixie>
[+][Politician] - Evil, Killing/Support, Human, Unique - <w.roles_politician>
[+][Poltergeist] - Evil, Chaos/Investigative, Non-Human - <w.roles_poltergeist>
```""")
    await client.say("""```md
[+][Poser] - Good, Support, Human - <w.roles_poser>
[+][Priest] - Good, Counteractive/Support, Human, Unique - <w.roles_priest>
[+][Prince] - Good, Support, Human, Unique - <w.roles_prince>
[+][Researcher] - Good, Investigative, Human, Unique - <w.roles_researcher>
[+][Rogue] - Good, Counteractive/Protective, Human, Unique - <w.roles_rogue>
[+][Rōjinbi] - Neutral, Chaos, Non-Human, Unique - <w.roles_rojinbi>
[+][Romantic] - Neutral, Protective, Human, Unique - <w.roles_romantic>
[+][Santa] - Neutral, Support, Non-Human, Unique - <w.roles_santa>
[+][Scarecrow] - Neutral, Chaos/Support, Non-Human, Unique - <w.roles_scarecrow>
[+][Seer] - Good, Investigative, Human - <w.roles_seer>
[+][Shifter] - Neutral, Chaos, Non-Human - <w.roles_shifter>
[+][Shinigami] - Neutral, Counteractive/Killing, Non-Human, Unique - <w.roles_shinigami>
[+][Souleater] - Neutral, Chaos/Killing, Non-Human, Achievable - <w.roles_souleater>
[+][Spectre] - Modifier, Achievable - <w.roles_spectre>
[+][Spider] - Evil, Counteractive/Support, Non-Human, Unique - <w.roles_spider>
[+][Spinster] - Neutral, Chaos/Investigative, Non-Human, Unique, Achievable - <w.roles_spinster>
[+][Stand User] - Modifier - <w.roles_standuser>
[+][Sylph] - Good, Support, Non-Human, Unique - <w.roles_sylph>
[+][TARDIS Engineer] - Good/Evil, Support, Human, Unique, Achievable - <w.roles_tardisengineer>
[+][Thief] - Neutral, Chaos/Counteractive, Human, Unique - <w.roles_thief>
[+][Time Lord] - Good, Investigative/Support, Non-Human - <w.roles_timelord>
[+][Twin] - Modifier - <w.roles_twin>
[+][Understudy] - Neutral, Chaos/Support, Human, Unique - <w.roles_understudy>
[+][Warlock] - Evil, Chaos/Killing, Human, Unique, Achievable - <w.roles_warlock>
[+][Werewolf] - Evil, Killing, Wolf - <w.roles_werewolf>
[+][Whisperer] - Good, Investigative/Support, Human, Unique - <w.roles_whisperer>
[+][Witch] - Neutral, Killing/Protective, Non-Human - <w.roles_witch>
```""")

@client.command(pass_context=True)
async def randomchoice(ctx, *, message=""):
    if message == "":
        await client.say("""Usage of command <w.randomchoice>:
```md
<w.randomchoice (comma seperated list of options)>

Example: <w.randomchoice A, B, C>
Output: 'C'```""")
    else:
        options = message.split(", ")
        result = random.choice(options)
        await client.say("**{}**".format(result))
        return result

@client.command(pass_context=True)
async def randomrole(ctx, *, message=""):
    if message == "":
        await client.say("""Usage of command <w.randomrole>:
```md
<w.randomrole (space seperated list of tags as parameters)>

Tags:
> Good
> Evil
> Neutral
> Human
> Non-Human
> Wolf
> Chaos
> Counteractive
> Investigative
> Killing
> Protective
> Support
> Unique
> Achievable

Include 'all' in parameters to discard parameters and allow all roles.
Include 'modifier' in parameters to include and limit selection to modifiers.
Precede tags with 'x-' to exclude roles with them.

Example: <w.randomrole good>
Output: 'Jailor'```""")
    else:
        global AllRoles, Modifiers
        conditions = message.split(" ")
        for c in conditions:
            c = c.lower()
        if "modifier" in conditions:
            All = list(Modifiers)
            Valid = list(All)
            for r in All:
                if "achievable" in conditions:
                    if r not in AchievableModifiers:
                        Valid.remove(r)
                    continue
                if "x-achievable" in conditions:
                    if r in AchievableModifiers:
                        Valid.remove(r)
                    continue
        else:
            All = list(AllRoles)
            Valid = list(All)
            ref = {"good" : GoodRoles, "evil" : EvilRoles, "neutral" : NeutralRoles, "chaos" : ChaosRoles, "counteractive" : CounteractiveRoles, "investigative" : InvestigativeRoles,
                   "killing" : KillingRoles, "protective" : ProtectiveRoles, "support" : SupportRoles, "human" : HumanRoles, "nonhuman" : NonHumanRoles, "non-human" : NonHumanRoles,
                   "wolf" : WolfRoles, "unique" : UniqueRoles, "achievable" : AchievableRoles}
            xref = {"x-good" : GoodRoles, "x-evil" : EvilRoles, "x-neutral" : NeutralRoles, "x-chaos" : ChaosRoles, "x-counteractive" : CounteractiveRoles,
                    "x-investigative" : InvestigativeRoles, "x-killing" : KillingRoles, "x-protective" : ProtectiveRoles, "x-support" : SupportRoles, "x-human" : HumanRoles,
                    "x-nonhuman" : NonHumanRoles, "x-non-human" : NonHumanRoles, "x-wolf" : WolfRoles, "x-unique" : UniqueRoles, "x-achievable" : AchievableRoles}
            if message.lower() != "all":
                for r in All:
                    for c in conditions:
                        if c in ref:
                            if r not in ref[c]:
                                Valid.remove(r)
                                break
                        elif c in xref:
                            if r in xref[c]:
                                Valid.remove(r)
                                break
        if Valid == []:
            await client.say("No roles exist that fit all parameters, sorry. :(")
        else:
            while True:
                role = random.choice(Valid)
                if role == "Good TARDIS Engineer" or role == "Evil TARDIS Engineer":
                    if "Good TARDIS Engineer" in Valid and "Evil TARDIS Engineer" in Valid:
                        x = random.randint(0,1)
                        if x == 0:
                            continue
                break
            await client.say("**{}**".format(role))
            return role

@client.command(pass_context=True)
async def listroles(ctx, *, message=""):
    if message == "":
        await client.say("""Usage of command <w.listroles>:
```md
<w.listroles (space seperated list of tags as parameters)>

Tags:
> Good
> Evil
> Neutral
> Human
> Non-Human
> Wolf
> Chaos
> Counteractive
> Investigative
> Killing
> Protective
> Support
> Unique
> Achievable

Include 'all' in parameters to discard parameters and allow all roles.
Include 'modifier' in parameters to include and limit selection to modifiers.
Precede tags with 'x-' to exclude roles with them.

Example: <w.listroles wolf>
Output: '3 roles found:
 - Cyberhound
 - Dire Wolf
 - Werewolf'```""")
    else:
        global AllRoles, Modifiers
        conditions = message.split(" ")
        for c in conditions:
            c = c.lower()
        if "modifier" in conditions:
            All = list(Modifiers)
            Valid = list(All)
            for r in All:
                if "achievable" in conditions:
                    if r not in AchievableModifiers:
                        Valid.remove(r)
                    continue
                if "x-achievable" in conditions:
                    if r in AchievableModifiers:
                        Valid.remove(r)
                    continue
        else:
            All = list(AllRoles)
            Valid = list(All)
            ref = {"good" : GoodRoles, "evil" : EvilRoles, "neutral" : NeutralRoles, "chaos" : ChaosRoles, "counteractive" : CounteractiveRoles, "investigative" : InvestigativeRoles,
                   "killing" : KillingRoles, "protective" : ProtectiveRoles, "support" : SupportRoles, "human" : HumanRoles, "nonhuman" : NonHumanRoles, "non-human" : NonHumanRoles,
                   "wolf" : WolfRoles, "unique" : UniqueRoles, "achievable" : AchievableRoles}
            xref = {"x-good" : GoodRoles, "x-evil" : EvilRoles, "x-neutral" : NeutralRoles, "x-chaos" : ChaosRoles, "x-counteractive" : CounteractiveRoles,
                    "x-investigative" : InvestigativeRoles, "x-killing" : KillingRoles, "x-protective" : ProtectiveRoles, "x-support" : SupportRoles, "x-human" : HumanRoles,
                    "x-nonhuman" : NonHumanRoles, "x-non-human" : NonHumanRoles, "x-wolf" : WolfRoles, "x-unique" : UniqueRoles, "x-achievable" : AchievableRoles}
            if message.lower() != "all":
                for r in All:
                    for c in conditions:
                        if c in ref:
                            if r not in ref[c]:
                                Valid.remove(r)
                                break
                        elif c in xref:
                            if r in xref[c]:
                                Valid.remove(r)
                                break
        if Valid == []:
            await client.say("No roles exist that fit all parameters, sorry. :(")
        else:
            display = "{} roles found:\n```".format(len(Valid))
            for r in Valid:
                display = "{} - {}\n".format(display, r)
            display = "{}```".format(display)
            await client.say(display)

@client.command(pass_context=True)
async def score(ctx, *, message=""):
    if message == "":
        await client.say("""Usage of command <w.score>:
```md
<w.score (wins:loses)>

Example: <w.score 10:6>
Output: '870'```""")
    else:
        message = message.split(":")
        W = int(message[0])
        L = int(message[1])
        score = round((100+(W+L)*2)*(W-L)*(1+(W+1)/(W+L+1)))
        await client.say(score)

@client.command(pass_context=True)
async def flip(ctx, *, message=""):
    if message == "":
        await client.say("""Usage of command <w.flip>:
```md
<w.flip (number of coins to flip)>

Example: <w.flip 3>
Output: 'T, H, H'```""")
    else:
        message = int(message)
        send=""
        tcount=0
        hcount=0
        for c in range(0,message):
            if c != 0:
                send="{}, ".format(send)
            i = random.randint(0,1)
            if i == 0:
                send=send+"T"
                tcount=tcount+1
            else:
                send=send+"H"
                hcount=hcount+1
        embed=discord.Embed(title=send)
        await client.say(embed=embed)
        return [hcount,tcount]

@client.command(pass_context=True)
async def roll(ctx, *, message=""):
    if message == "":
        await client.say("""Usage of command <w.roll>:
```md
<w.roll (#d#)>

Example: <w.roll 3d20>
Output: '19, 8, 14'```""")
    else:
        message = message.split("d")
        times = int(message[0])
        sides = int(message[1])
        send = ""
        for c in range(0,times):
            if c != 0:
                send="{}, ".format(send)
            i = str(random.randint(1,sides))
            send = send+i
        embed=discord.Embed(title=send)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def vote(ctx, *, message="", where="", needed=0):
    if message == "":
        await client.say("""Usage of command <w.vote>:
```md
<w.vote (options to vote between seperated by commas)>

Example: <w.vote 1, 2, 3>
Output: 'React with appropriate emoji to vote:
:A: --> 1
:B: --> 2
:C: --> 3'```""")
    else:
        if where == "":
                where = ctx.message.channel
        global VoteEmojis
        options = message.split(", ")
        if len(options) > 20:
            await client.say("Too many!")
        else:
            options = sorted(options)
            display=""
            for i in range(1,len(options)+1):
                display = display+("\n{} --> {}".format(VoteEmojis[i-1],options[i-1]))
            vote_message = await client.send_message(where,embed=discord.Embed(title="React with appropriate emoji to vote:",description=display))
            if needed != 0:
                return
                # return voted value

@client.command(pass_context=True)
async def icon(ctx, *, role=""):
    if role == "":
        await client.say("""Usage of command <w.icon>:
```md
<w.icon (role)>

Example: <w.icon seer>
Output: 'https://i.imgur.com/Ih7WkoX.png'```""")
    else:
        role = role.lower()
        role = role.replace(" ","")
        try:
            icon = icons[role]
            await client.say(icon)
        except KeyError:
            await client.say("That is not a role.")

@client.group(pass_context=True)
async def generatelist(ctx):
    if ctx.invoked_subcommand is None:
        await client.say("Available Gamemodes to generate lists for: \n(Give Players and Roles as comma seperated lists)\n```md\nStandard - <w.generatelist standard [players]>\n\
Anonymous Register - <w.generatelist anons [players] : [roles]>\nDuality - <w.generatelist duality [players]>\nMoral Feud - <w.generatelist morals [players]>\n\
Truth & Claw - <w.generatelist tac [players]>```")

@generatelist.command()
async def standard(*, message: str):
    global GoodRoles, EvilRoles, NeutralRoles, AchievableRoles, Modifiers, AchievableModifiers
    Good=list(GoodRoles)
    for r in Good:
        if r in AchievableRoles:
            Good.remove(r)
    Evil=list(EvilRoles)
    for r in Evil:
        if r in AchievableRoles:
            Evil.remove(r)
    Evil.remove("Dire Wolf")
    Evil.remove("Werewolf")
    Evil.remove("Cultist")
    Neutral=list(NeutralRoles)
    for r in Neutral:
        if r in AchievableRoles:
            Neutral.remove(r)
    Mod=list(Modifiers)
    for r in Mod:
        if r in AchievableModifiers:
            Mod.remove(r)
    Mod.append("Morty")
    Mod.append("Twin")
    PlayerList = message.split(", ")
    PlayerList = sorted(PlayerList)
    if len(PlayerList) < 8:
        await client.say("Not enough players, sorry.")
        return
    else:
        while True:
            RoleList = ["Dire Wolf", "Seer"]
            EvilCount = 1
            GoodCount = 1
            x = round(len(PlayerList)/8)
            for i in range(0, x):
                RoleList.append("Werewolf")
                EvilCount = EvilCount+1
            y = random.randint((round(len(PlayerList)/3)), (round(len(PlayerList)/1.5)))
            for i in range(0, y):
                g = random.choice(Good)
                RoleList.append(g)
                if g in UniqueRoles:
                    Good.remove(g)
                GoodCount = GoodCount+1
            if "Priest" in RoleList:
                RoleList.append("Cultist")
                EvilCount = EvilCount+1
            for i in range(0, round((GoodCount-EvilCount)/2)):
                e = random.choice(Evil)
                RoleList.append(e)
                if e in UniqueRoles:
                    Evil.remove(e)
                EvilCount = EvilCount+1
            for i in range(0,(len(PlayerList)-len(RoleList))):
                n = random.choice(Neutral)
                RoleList.append(n)
                if n in UniqueRoles:
                    Neutral.remove(n)
            ModifierList = []
            TwinYes = False
            StandYes = False
            Minstrels=0
            TwinCount=1
            if "Bard" in RoleList:
                Minstrels=2
                Mod.append("Minstrel")
                Mod.append("Minstrel")
            for i in range(0, (len(PlayerList))):
                if Minstrels > 0:
                    ModifierList.append("Minstrel")
                    Minstrels=Minstrels-1
                elif TwinYes == True:
                    ModifierList.append("Twin {}" .format(TwinCount))
                    TwinCount = TwinCount+1
                    TwinYes = False
                elif StandYes == True:
                    ModifierList.append("Stand User")
                    StandYes = False
                else:
                    z = random.randint(1,4)
                    if z == 4:
                        m = random.choice(Mod)
                        if m == "Twin":
                            ModifierList.append("Twin {}" .format(TwinCount))
                            TwinYes = True
                        if m == "Stand User":
                            if "Stand User" not in ModifierList:
                                StandYes = True
                                Mod.append("Stand User")
                            ModifierList.append("Stand User")
                        else:
                            ModifierList.append(m)
                    else:
                        ModifierList.append("")
            random.shuffle(RoleList)
            random.shuffle(ModifierList)
            combined = "```md\n"
            for i in range(0,len(PlayerList)):
                string = "[+][{}] - {} {}\n" .format(PlayerList[i],RoleList[i],ModifierList[i])
                combined = combined+string
            finish = "```"
            combined = combined+finish
            if "Minstrel" in combined and "Bard" not in combined:
                continue
            if "Backstabber Twin" in combined or "Backstabber Minstrel" in combined or "Backstabber Morty" in combined or "Backstabber Feral" in combined:
                continue
            elif "Bard Minstrel" in combined:
                continue
            elif combined.count("Minstrel") == 1:
                continue
            elif combined.count("Stand User") == 1:
                continue
            elif combined.count("Twin") % 2 != 0:
                continue
            elif "Cultist" in combined and "Priest" not in combined:
                continue
            elif "Priest" in combined and "Cultist" not in combined:
                continue
            elif "Maid Feral" in combined:
                continue
            c = False
            for r in RoleList:
                if r in AchievableRoles:
                    c = True
            if c == True:
                continue
            if len(RoleList) == len(PlayerList):
                break
    await client.say(combined)

@generatelist.command()
async def anons(*, message: str):
    message = message.split(" : ")
    PlayerList = message[0]
    RoleList = message[1]
    if len(PlayerList) != len(RoleList):
        await client.say("Needs to have equal amount of players and roles!")
    elif len(PlayerList) < 8:
        await client.say("Not enough players, sorry.")
    else:
        PlayerList = PlayerList.split(", ")
        RoleList = RoleList.split(", ")
        PlayerList = sorted(PlayerList)
        random.shuffle(RoleList)
        combined = "```md\n"
        for i in range(0,len(PlayerList)):
            string = "[+][{}] - {}\n" .format(PlayerList[i],RoleList[i])
            combined = combined+string
        finish = "```"
        combined = combined+finish
        await client.say(combined)

@generatelist.command()
async def duality(*, message: str):
    global InvestigativeRoles, KillingRoles, AchievableRoles
    PlayerList = message.split(", ")
    PlayerList = sorted(PlayerList)
    if len(PlayerList) % 2 != 0:
        await client.say("Needs to be an even number of players!")
    elif len(PlayerList) < 8:
        await client.say("Not enough players, sorry.")
    else:
        Invest = list(InvestigativeRoles)
        Kill = list(KillingRoles)
        i = ["Time Lord", "Whisperer", "Mage", "Hacker", "Noir"]
        for r in i:
            Invest.remove(r)
        k = ["Jester", "Werewolf", "Dire Wolf", "Bard", "Inventor", "Gladiator", "Hooligan", "Politician", "Shinigami", "Hunter", "Backstabber", "Arsonist"]
        for r in k:
            Kill.remove(r)
        for r in AchievableRoles:
            if r in Invest:
                Invest.remove(r)
            if r in Kill:
                Kill.remove(r)
        t = int(len(PlayerList)/2)
        RoleList = []
        for sets in range(0,t):
            iRole = random.choice(Invest)
            kRole = random.choice(Kill)
            iRole = "{} Twin {}".format(iRole,(sets+1))
            kRole = "{} Twin {}".format(kRole,(sets+1))
            RoleList.append(iRole)
            RoleList.append(kRole)
        random.shuffle(RoleList)
        combined = "```md\n"
        for i in range(0,len(PlayerList)):
            string = "[+][{}] - {}\n" .format(PlayerList[i],RoleList[i])
            combined = combined+string
        finish = "```"
        combined = combined+finish
        await client.say(combined)

@generatelist.command()
async def morals(*, message: str):
    PlayerList = message.split(", ")
    PlayerList = sorted(PlayerList)
    if len(PlayerList) < 8:
        await client.say("Not enough players, sorry.")
    else:
        EvilCount = 1
        GoodCount = 1
        NeutralCount = 0
        x = round(len(PlayerList)/8)
        for i in range(0, x):
            EvilCount = EvilCount+1
        y = random.randint((round(len(PlayerList)/3)), (round(len(PlayerList)/1.5)))
        for i in range(0, y):
            GoodCount = GoodCount+1
        for i in range(0, round((GoodCount-EvilCount)/2)):
            EvilCount = EvilCount+1
        for i in range(0,(len(PlayerList)-GoodCount-EvilCount)):
            NeutralCount = NeutralCount+1
        Alignments = []
        for c in range(0, EvilCount):
            Alignments.append("Evil")
        for c in range(0, GoodCount):
            Alignments.append("Good")
        for c in range(0, NeutralCount):
            Alignments.append("Neutral")
        random.shuffle(Alignments)
        combined = "```md\n"
        for i in range(0,len(PlayerList)):
            string = "[+][{}] - {}\n" .format(PlayerList[i],Alignments[i])
            combined = combined+string
        finish = "```"
        combined = combined+finish
        await client.say(combined)

@generatelist.command()
async def tac(*, message: str):
    PlayerList = message.split(", ")
    PlayerList = sorted(PlayerList)
    if len(PlayerList) < 6:
        await client.say("Not enough players, sorry.")
    else:
        RoleList = []
        for i in range(0,round(len(PlayerList)/10+0.49999)):
            RoleList.append("Good Knight")
            RoleList.append("Evil Werewolf")
        for i in range(0,round(3*len(PlayerList)/5-0.49999)):
            RoleList.append("Good Time Lord")
        for i in range(0,(len(PlayerList)-len(RoleList))):
            RoleList.append("Evil Time Lord")
        random.shuffle(RoleList)
        combined = "```md\n"
        for i in range(0,len(PlayerList)):
            string = "[+][{}] - {}\n" .format(PlayerList[i],RoleList[i])
            combined = combined+string
        finish = "```"
        combined = combined+finish
        await client.say(combined)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
            
    client.run(TOKEN)
