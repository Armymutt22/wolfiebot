import discord
from discord.ext import commands
import asyncio
from wolfiebot import *
from config import *

# PlayerInfo structure:
# player : [user, channel ref, role, [modifiers], alignment, alive/dead]

global NeedDeputy
NeedDeputy = True

class GameCommands():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def setplayers(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            player_role = discord.utils.get(ctx.message.server.roles, name="Player")
            players = ctx.message.mentions
            for p in players:
                if "Player" not in [y.name for y in p.roles]:
                    await self.client.add_roles(p, player_role)

    @commands.command(pass_context=True)
    async def rungame(self, ctx, *, message: str):
        global PlayerInfo, NeedDeputy
        await self.client.say("This command is in development.")
        return
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            player_role = discord.utils.get(ctx.message.server.roles, name="Player")
            message = message.split("; ")
            gamemode = message[0]
            await ctx.invoke(self.client.get_command("giveroles",message=message[1]))
            report = "Game Start!"
            if "Cultist" in [PlayerInfo[p][2] for p in PlayerInfo]:
                report == "{}/A Cultist is present in this game!".format(report)
            if "Priest" in [PlayerInfo[p][2] for p in PlayerInfo]:
                report == "{}/A Priest is present in this game!".format(report)
            if "Merchant" in [PlayerInfo[p][2] for p in PlayerInfo]:
                report == "{}/A Merchant is present in this game!".format(report)
            n = 0
            while True:
                n = n+1
                report = "{}; 900; {}".format(n,report)
                await ctx.invoke(self.client.get_command("daytimer"),message=report)
                mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
                deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
                if mayor_role not in [x for y in [p.roles for p in ctx.message.server.members if player_role in p.roles] for x in y]:
                    if deputy_role in [x for y in [p.roles for p in ctx.message.server.members if player_role in p.roles] for x in y]:
                        deputy = [p for p in ctx.message.server.members if deputy_role in p.roles][0]
                        await self.client.add_roles(deputy, mayor_role)
                        await self.client.remove_roles(deputy, deputy_role)
                        await self.client.send_message(game_channel,"{} has become Mayor! Choose your deputy with *w.choosedeputy @player*.".format(deputy.mention))
                        NeedDeputy = True
                        while NeedDeputy == True:
                            await asyncio.sleep(5)
                    else:
                        await self.client.send_message(voting_channel,"MAYORAL ELECTION")
                        mayor = await ctx.invoke(self.client.get_command("playervote"))
                        elected = [p for p in ctx.message.server.members if p.nick == mayor][0]
                        await self.client.add_roles(elected, mayor_role)
                        await self.client.send_message(game_channel,"{} has been elected as Mayor! Choose your deputy with *w.choosedeputy @player*.".format(elected.mention))
                        NeedDeputy = True
                        while NeedDeputy == True:
                            await asyncio.sleep(5)
                if n != 1:
                    await self.client.send_message(voting_channel,"LYNCH")
                    lynched = await ctx.invoke(self.client.get_command("playervote"))
                    lynched = [p for p in ctx.message.server.members if p.nick == lynched][0]
                    if True: # if not saved
                        await ctx.invoke(self.client.get_command("kill"),player=lynched.mention)
                        await self.client.send_message(game_channel,"{} has been voted to be Lynched!\n\nThey were a {} {}!".format(lynched.mention))
                        # message declaring lynched, role
                    else: # if saved
                        await self.client.send_message(game_channel,"{} has been voted to be Lynched!\n\nBut they were saved!".format(lynched.mention))
                        # remove used up save
                # keep working on this
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def giveroles(self, ctx, *, message: str):
        global PlayerInfo
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            message = message.split(", ")
            x = []
            for m in message:
                m = m.split(": ")
                m[0] = m[0].lower()
                if "(" in m[1]:
                    y = m[1].split(" (")
                    m[1] = y[0]
                    modifier = y[1]
                    m.append(modifier[:-1])
                else:
                    m.append("")
                chan = discord.utils.get(ctx.message.server.channels, name="{}-priv".format(m[0]))
                m.append(chan)
                gm_role = discord.utils.get(ctx.message.server.roles, name="Game Master")
                bot_role = discord.utils.get(ctx.message.server.roles, name="Bots")
                user = [u for u in ctx.message.server.members if chan.permissions_for(u).read_messages == True and gm_role not in u.roles and bot_role not in u.roles][0]
                m.append(user)
                x.append(m)
            PlayerInfo = {m[0] : [m[4], m[3], m[1], [m[2]]] for m in x}
            for player in PlayerInfo:
                if PlayerInfo[player][3] == [""]:
                    PlayerInfo[player][3] = []
                    modifier = False
                else:
                    modifier = True
                if PlayerInfo[player][2] in GoodRoles:
                    alignment = "Good"
                elif PlayerInfo[player][2] in EvilRoles:
                    alignment = "Evil"
                elif PlayerInfo[player][2] in NeutralRoles:
                    alignment = "Neutral"
                else:
                    await self.client.say("{} is not a role!".format(PlayerInfo[player][2]))
                PlayerInfo[player].append(alignment)
                PlayerInfo[player].append("Alive")
                if modifier == True:
                    mod = " {}".format(PlayerInfo[player][3][0])
                else:
                    mod = ""
                ali = ""
                if PlayerInfo[player][3] == "Good" or PlayerInfo[player][4] == "Neutral":
                    ali = " {}".format(PlayerInfo[player][4])
                elif PlayerInfo[player][3] == "Evil":
                    ali = "n {}".format(PlayerInfo[player][4])
                print(ali)
                output = "You are a{} {}{}!".format(ali,PlayerInfo[player][2],mod)
                await self.client.send_message(PlayerInfo[player][1],output)
                await ctx.invoke(self.client.get_command(descCommands[PlayerInfo[player][2]]), where=PlayerInfo[player][1])
                if modifier == True:
                    await ctx.invoke(self.client.get_command(descCommands[PlayerInfo[player][3][0]]), where=PlayerInfo[player][1])
            rolereport = ""
            for p in PlayerInfo:
                mod = ""
                for m in PlayerInfo[p][3]:
                    mod = "{} {}".format(mod,m)
                rolereport = ("{}{} - {} {}{}\n".format(rolereport,p.upper(),PlayerInfo[p][4],PlayerInfo[p][1],mod))
            await self.client.send_message(notes_channel,rolereport)
        else:
            await self.client.say("You need to be a GM to use this command!")
            
    @commands.command(pass_context=True)
    async def gamestatus(self, ctx):
        global PlayerInfo
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            output = "```"
            for p in PlayerInfo:
                mod = ""
                for m in PlayerInfo[p][3]:
                    mod = "{} {}".format(mod,m)
                output = "{}\n{} - {} {}{} - {}".format(output,p.upper(),PlayerInfo[p][4],PlayerInfo[p][2],mod,PlayerInfo[p][5])
            output = "{}```".format(output)
            embed = discord.Embed(title="Game Status",description=output)
            await self.client.say(embed=embed)
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def daytimer(self, ctx, *, message: str):
        global Day
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            message = message.split("; ")
            n = message[0]
            secs = int(message[1])
            anno = message[2].split("/")
            a = ""
            for x in anno:
                a = "{}\n{}".format(a,x)
            await self.client.send_message(game_channel,"DAY {}\n{}".format(n, a))
            perms = discord.PermissionOverwrite()
            perms.read_messages = True
            perms.send_messages = False
            perms.add_reactions = True
            player = discord.utils.get(ctx.message.server.roles, name="Player")
            await self.client.edit_channel_permissions(voting_channel, player, perms)
            perms = discord.PermissionOverwrite()
            perms.send_messages = True
            perms.add_reactions = True
            player = discord.utils.get(ctx.message.server.roles, name="Player")
            await self.client.edit_channel_permissions(game_channel, player, perms)
            Day = True
            for i in range(0, secs):
                await asyncio.sleep(1)
                if (secs-i) % 300 == 0:
                    await self.client.send_message(game_channel,"{} minutes remaining until Night!".format(int((secs-i)/60)))
                if (secs-i) == 180:
                    await self.client.send_message(game_channel,"3 minutes remaining until Night!")
                if (secs-i) == 120:
                    await self.client.send_message(game_channel,"2 minutes remaining until Night!")
                if (secs-i) == 60:
                    await self.client.send_message(game_channel,"1 minute remaining until Night!")
                if (secs-i) == 30:
                    await self.client.send_message(game_channel,"30 seconds remaining until Night!")
                if (secs-i) <= 10 and (secs-i) != 1:
                    await self.client.send_message(game_channel,"{} seconds remaining until Night!".format(secs-i))
                if (secs-i) == 1:
                    await self.client.send_message(game_channel,"1 second remaining until Night!")
                if Day == False:
                    break
            Day = False
            await self.client.send_message(game_channel,"NIGHT {}".format(n))
            perms = discord.PermissionOverwrite()
            perms.read_messages = True
            perms.send_messages = False
            perms.add_reactions = False
            player = discord.utils.get(ctx.message.server.roles, name="Player")
            await self.client.edit_channel_permissions(voting_channel, player, perms)
            perms = discord.PermissionOverwrite()
            perms.send_messages = False
            perms.add_reactions = True
            player = discord.utils.get(ctx.message.server.roles, name="Player")
            await self.client.edit_channel_permissions(game_channel, player, perms)
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def playervote(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            options = ""
            role = discord.utils.get(ctx.message.server.roles, name="Player")
            players = [p.nick for p in ctx.message.server.members if role in p.roles and p.nick != None]
            for name in [p.name for p in ctx.message.server.members if role in p.roles and p.nick == None]:
                players.append(name)
            players = sorted(players)
            for p in players:
                if p == players[0]:
                    options = p
                else:
                    options = "{}, {}".format(options,p)
            n = len([p.nick for p in ctx.message.server.members if role in p.roles])/2+1
            voted = await ctx.invoke(self.client.get_command("vote"),message=options,where=voting_channel,needed=n)
            return voted
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def choosedeputy(self, ctx, *, chosen: discord.Member):
        global NeedDeputy
        if NeedDeputy == True:
            if "Mayor" in [y.name for y in ctx.message.author.roles]:
                await ctx.invoke(self.client.get_command("deputy"),player=chosen,invoked=True)
                NeedDeputy = False
                await self.client.say("{} has been chosen as Deputy!".format(chosen.mention))
            else:
                await self.client.say("You need to be the Mayor to use this command!")
        else:
            await self.client.say("A Deputy cannot be chosen at this time.")

    @commands.command(pass_context=True)
    async def night(self, ctx):
        global Day
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if Day == False:
                await self.client.say("It is either already night or there is no game happening.")
            else:
                Day = False
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def kill(self, ctx, player: discord.Member):
        player_role = discord.utils.get(ctx.message.server.roles, name="Player")
        dead_role = discord.utils.get(ctx.message.server.roles, name="Dead")
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if "Player" in [y.name for y in player.roles]:
                await self.client.add_roles(player, dead_role)
                await self.client.remove_roles(player, player_role)
                if "Mayor" in [y.name for y in player.roles]:
                    mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
                    await self.client.remove_roles(player, mayor_role)
                if "Deputy" in [y.name for y in player.roles]:
                    deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
                    await self.client.remove_roles(player, deputy_role)
            else:
                await self.client.say("User is either already dead or not in the game.")
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def mayor(self, ctx, player: discord.Member):
        mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
        deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if "Player" in [y.name for y in player.roles]:
                if mayor_role not in [x for y in [p.roles for p in ctx.message.server.members if player_role in p.roles] for x in y]:
                    await self.client.add_roles(player, mayor_role)
                    if deputy_role in [y for y in player.roles]:
                        await self.client.remove_roles(player, deputy_role)
                else:
                    await self.client.say("There is already a Mayor in this game.")
            else:
                await self.client.say("User is either dead or not in the game.")
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def deputy(self, ctx, player: discord.Member, invoked=False):
        mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
        deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
        if "Game Master" in [y.name for y in ctx.message.author.roles] or invoked == True:
            if "Player" in [y.name for y in player.roles]:
                if deputy_role not in [x for y in [p.roles for p in ctx.message.server.members if player_role in p.roles] for x in y]:
                    if mayor_role not in [y for y in player.roles]:
                        await self.client.add_roles(player, deputy_role)
                    else:
                        await self.client.say("User is the Mayor.")
                else:
                    await self.client.say("There is already a Deputy in this game.")
            else:
                await self.client.say("User is either dead or not in the game.")
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def lockjaw(self, ctx, user: discord.Member, status: str):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            status = status.lower()
            await self.client.say(user.name)
            await self.client.say(game_channel.name)
            if status == "t" or status == "true":
                gperms = discord.PermissionOverwrite()
                vperms = discord.PermissionOverwrite()
                gperms.send_messages = False
                gperms.add_reactions = False
                vperms.add_reactions = False
                await self.client.edit_channel_permissions(game_channel, user, gperms)
                await self.client.edit_channel_permissions(voting_channel, user, vperms)
            elif status == "f" or status == "false":
                await self.client.delete_channel_permissions(game_channel, user)
                await self.client.delete_channel_permissions(voting_channel, user)
        else:
            await client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def medium(self, ctx, user: discord.Member, status: str):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            status = status.lower()
            if status == "t" or status == "true":
                perms = discord.PermissionOverwrite()
                perms.read_messages = True
                await self.client.edit_channel_permissions(dead_channel, user, perms)
            elif status == "f" or status == "false":
                await self.client.delete_channel_permissions(game_channel, user)
                await self.client.delete_channel_permissions(voting_channel, user)
        else:
            await client.say("You need to be a GM to use this command!")

def setup(client):
    client.add_cog(GameCommands(client))
