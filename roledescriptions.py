import discord
from discord.ext import commands
import asyncio
from wolfiebot import *

class RoleDescriptions():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def roles_alchemist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Descended from a line of practitioners and continuing the work of their forefathers: Alchemy, an ancient art used to transmute - not only metals, but life itself.*
**Actions:**
*Homunculus* - At night, may create a Homunculus. That night, all Direwolves in the game appear to be a random Good Human role when targeted with *Investigate*. This action uses up one of the Alchemist's Potions.
*Chaos Serum* - At night, may target any player. That player's alignment changes from Good to Evil, or vice versa. If that player is Neutral, it changes to Evil. At the start of the second day after this action is used, the target player's alignment changes back to what it was before this action was used, even if their role or alignment has changed through other means since. This action uses up one of the Alchemist's Potions.
*Potion of Judas* - At night, may target any player. That player's role changes to a random role of the same alignment. This action uses up one of the Alchemist's Potions.
*Bewitch* - If targeted by *Maul* or *Pack Offensive*, may choose any player for the action to be redirected towards instead.
**Abilities:**
- Has an amount of potions equal to half the amount of players in the game. Only one potion may be used per night.
- Cannot become a Wolf by any means.
- Counts as Evil for the objectives of Wolves.
**Objectives:**
- Be the last player alive, excluding Wolves.
**Tags:**
- Neutral
- Chaos/Support
- Arcane
- Unique""",colour=0x8c8cff)
        embed.set_thumbnail(url=icons["alchemist"])
        await where.send("__**Alchemist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_anarchist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Strategically-Implemented Self-Murder* - Once per game, at night, commits Suicide.
*Spanner* - Once per night, target any player. Any actions that player makes that night automatically fail. 
*Persuade* - Twice per game, at night, while not using *Molotov*, select two other players. The two switch roles and alignments until the end of the following night. Cannot target the same player twice with this action. 
*Molotov* - Once every two nights, target any player with a Strong Attack. Cannot be used on the same night as *Strategically-Implemented Self-Murder*.
**Abilities:**
- If killed by a Lynching, becomes a Spectre.
**Objectives:**
- Finish the game with no living players. If the last player alive is the Anarchist, this objective fails. 
**Tags:**
- Neutral
- Chaos/Killing
- Human
- Unique""",colour=0xff9400)
        embed.set_thumbnail(url=icons["anarchist"])
        await where.send("__**Anarchist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_arsonist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*A box of matches. A stick of wood. A can of oil. A switch of a lighter. A smirk of victory. A city of flames.*
**Actions:**
*Douse* - Every night, chooses one player to douse in gasoline. Players do not know if they are doused in gasoline.
*Ignite* - Instead of using *Douse*, may ignite all players doused in gasoline. This targets them with an Unstoppable Attack, and they become no longer doused in gasoline. On the night that the Arsonist uses *Ignite*, all players who target them are doused in gasoline and also ignited, however the Arsonist is not saved from any attacks.
**Abilities:**
- Upon death, becomes a Spectre and loses access to *Douse* action.
**Objectives:**
- Be the last player alive, or finish the game with no living players.
**Tags:**
- Neutral
- Chaos/Killing
- Human
- Unique""",colour=0xff9400)
        embed.set_thumbnail(url=icons["arsonist"])
        await where.send("__**Arsonist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_backstabber(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Honour? Dignity? Loyalty? Oh, please, you're a child. I want to live and I'll do it by any means. I'll use you as a tool and the moment you're no longer useful to me, I'll toss you aside and pick another shield. I'll kick you in the balls and you'll smile to my face. I'll use you and abuse you and take every last penny from you until I drive a knife into your neck. And the best part? I will feel **nothing**.*
**Actions:**
*Betray* - Every night, may choose a player. If that player does not have the same alignment as the Backstabber, and has targeted the Backstabber with any action before the night this action is used, they are targeted with a Powerful Attack. If they die from this attack, it is announced that they committed Suicide.
**Abilities:**
- Always appears as a random Good role when targeted with *Investigate*.
- If any action or ability would cause the Backstabber to gain a Modifier or a Save, unless it is the action *Infect*, the player whose action or ability it was is targeted with an attack of Strength one level greater than the Save that would have been given, or Powerful if the Backstabber would have gained a Modifier. If they die from this attack, it is announced that they committed Suicide.
- Cannot begin the game with any Modifiers.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Counteractive/Killing
- Human
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["backstabber"])
        await where.send("__**Backstabber**__",embed=embed)


    @commands.command(pass_context=True)
    async def roles_bard(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*The composer in the concerto of life. Corralling crescendos to be measured and beat, listening to the symphonies of screams, tuned to perfection and ensembled in harmony.*
**Actions:**
*Direct* - Every night, chooses a player. Flip a coin for all players with the Minstrel Modifier, even if they are the chosen player. For one heads, the chosen player is targeted with a Standard Attack; for two, a Strong Attack; for three, a Powerful attack and for four or more an Unstoppable Attack. The Bard does not count as targeting the chosen player but all Minstrel players do. Players with the Minstrel Modifier are told which player was targeted but not the results of any coin flips.
*Initiate* - Once per game, is told when no players with the Minstrel Modifier remain, and chooses one player to apply the Modifier to.
**Abilities:**
- The Minstrel Modifier is only present in games where the Bard appears, and is guaranteed to be applied to at least two players (the Bard may not receive this Modifier). 
- The Bard does not know which players have the Minstrel Modifier and those with the Modifier do not know the identity of the Bard.
**Objectives:**
- Be the last player alive. May spare up to two players providing they have the Minstrel Modifier.
**Tags:**
- Neutral
- Chaos/Killing
- Human
- Faction: *Troupe*
- Unique""",colour=0xff0098)
        embed.set_thumbnail(url=icons["bard"])
        await where.send("__**Bard**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_baykok(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Spectral Arrows* - Every night, may choose any player, and a role. The player is targeted with a Standard Attack. If that player's role is Killing, they are targeted with a Powerful Attack instead. If that player is Support, the attack fails. If the player dies from this action and Baykok was the only player to target them with an Attack, they appear to have been killed by the role chosen by the Baykok.
*Harvest* - Once per game, at night, may choose any player. If that player has any limited-use actions, they lose all uses of them.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Counteractive/Killing
- Ethereal
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["baykok"])
        await where.send("__**Baykok**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_bloodhound(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Maul* - Discuss with the other wolves in a private channel who to Strong Attack during the Night
*Pack Offensive* - Once per game, at night, not before NIGHT 3, instead of using Maul, the Wolves may choose to each individually target any player with a Standard Attack
*Fangs* - Every two nights, all Vampires together may target any player. That player loses all of their saves. If that player had no saves, they become a Vampire. If the player targeted had also been targeted with Infect that night, was a Werewolf or had the Feral modifier, they become a Bloodhound rather than a Vampire.
*Unholy Tribute* - Once per game, may select any Wolf or Vampire and any other player. Both chosen players are targeted with an Unstoppable Attack.
**Abilities:**
- All Vampires and Bloodhounds in the game may speak in a collective private channel with one another. They may still speak in this channel after death.
- Whenever any player (other than one who was already a Vampire) becomes a Vampire or a Bloodhound, all Vampires and Bloodhounds other than the that player gain a Queued Standard Save.
- If targeted by any effect that would cause an alignment change without changing the Vampire's role, commits Suicide.
- If there are no Vampires alive and no Wolves other than the Bloodhound left alive, the Bloodhound gains a Queued Strong Save.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Killing/Support
- Wolf
- Factions: *Vampiric, Wolves*
- Unique
- Achievable""",colour=0x9b0029)
        embed.set_thumbnail(url=icons["bloodhound"])
        await where.send("__**Bloodhound**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_clockmaker(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*A thousand rusted, ancient cogs turning around in the belly of the beast. Dwelling inside your head, the infernal noise. Tick tock. Tick tock. Tick tock. With every second that passes, you take one step closer to your own demise.*
**Actions:**
*Pendulum* - Every night, can choose one player to target with a Standard Attack. If the targeted player dies and is Good, the Clockmaker's clock moves forwards one, if they are Evil, the clock moves backwards one, if they are Neutral, the clock moves forward three.
**Abilities:**
- Has a clock which starts set to 8.
- If their clock strikes 6, they commit Suicide.
- If their clock strikes 10, they gain a Queued Strong Save. This happens each time the clock strikes 10.
- If their clock strikes 11, Pendulum is a Powerful Attack rather than a Standard Attack.
- Cannot change alignment or objective by any means, unless they also change role. If an effect would cause the Clockmaker to change their alignment or objective without also changing their role, it fails.
**Objectives:**
- Have their clock strike 12.
**Tags:**
- Neutral
- Killing
- Human""",colour=0xff9400)
        embed.set_thumbnail(url=icons["clockmaker"])
        await where.send("__**Clockmaker**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_companion(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*When I saw the gleam in this child's eye, I knew I had to welcome them onboard. But I have to be careful, I can't let them go like the others... banished to another dimension... forced to forget... ripped apart by time itself... but not them. Never them.*
**Abilities:**
- See Time Lord (‘*w.roles_timelord*’).
- If targeted with *Invite*, becomes a TARDIS Engineer.
**Objectives:**
- Identical to their Time Lord.
**Tags:**
- Identical alignment to their Time Lord.
- Faction: *Tardis*
- Modifier
- Achievable""",colour=0x204eff)
        embed.set_thumbnail(url=icons["companion"])
        await where.send("__**Companion**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_conduit(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Abilities:**
- Every night from NIGHT 2 onwards, if any of their actions involve an Attack that attack increases in strength by one level permanently, to a maximum of Unstoppable.
- At the start of DAY 3 (or the first available day if this modifier is gained after this point), it is announced that a Seer has published the Conduit's identity. Their role will appear to be a random Evil role.
- May only be applied to players with Human Killing roles.
- If the player with this modifier is a Companion or a Twin, the other member of this faction also gains this modifier.
**Tags:** 
- Modifier""",colour=0x80659a)
        embed.set_thumbnail(url=icons["conduit"])
        await where.send("__**Conduit**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_cultist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*As your promulgator, I bid you, say it with me- Brothers! Sisters! The great devotion shall not be swayed, we shall be venerated! We shall see the rise of our one true saviour and live to see the day this world is cured of its sickness!*
**Actions:**
*Convert* - Once per game, can choose one player to convert to Evil. In the event that this player is already Evil, the Cultist may not try again.
*Sacrifice* - Once per game, at night, can choose two players, one of whom is already dead. The dead player is revived as a random non-Unique Evil role, and the living player commits Suicide.
*Curse* - Once per game, can remove all Lunar and Active Saves for Good roles.
**Abilities:**
- The presence of the Cultist is revealed at the start of the game, but not their identity.
- If the Cultist is present, the Priest must also be present.
- If any Priest becomes a Paladin, becomes a Warlock. 
- If alignment is changed to Good, becomes a Priest.
- If any Priest becomes a Cultist, becomes a Priest.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Counteractive/Support
- Human
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["cultist"])
        await where.send("__**Cultist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_cyberhound(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Maul* - Discuss with other Wolves in a private channel who to Strong Attack during the night.
*Pack Offensive* - Once per game, at night, not before NIGHT 3, instead of using *Maul*, the Wolves may choose to each individually target any player with a Standard Attack.
*Dox* - Every night, chooses two players and chooses a non-Unique role for each player. If either player dies during that night or the following day and their role has not been changed since, they appear to be the role chosen for them and the Cyberhound is told their actual role. If a player the Cyberhound has chosen during that night is targeted with *Shift*, the player using the action becomes the role chosen by the Cyberhound rather than the player’s actual role. They still gain any modifiers the player had.
**Abilities:**
- On death, the real roles of all the dead players that *Dox* took effect on are revealed.
- May still speak in the Wolf channel when dead.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Counteractive/Killing
- Wolf
- Faction: *Wolves*
- Unique
- Achievable""",colour=0xff5000)
        embed.set_thumbnail(url=icons["cyberhound"])
        await where.send("__**Cyberhound**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_dentist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*A recent study suggests 67.34% of children fear going to the dentist. I wonder why. Why would anyone fear having a cold, metallic scalpel digging around in their mouth? Why would anyone fear whizzing drills and powerful machinery burying into the gums of patients? Why would anyone fear having every tooth forcefully extracted from their bleeding jaws as they sing a symphony of roaring agony? C'mon, buddy, we're not all that bad if you get to know us...*
**Actions:**
*Lockjaw* - Every night, select any player. That player may not speak in *#game* or vote in *#voting* the following day. The town is not told about this effect, however the target player is. If the target player is Lynched, it is announced that they were lockjawed.
*Laughing Gas* - Once per game, at night, may select any player. If they were targeted with *Lockjaw* the previous night, that player becomes an Evil Jester.
**Abilities:**
- Is not affected by *Haunt*.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Counteractive
- Human
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["dentist"])
        await where.send("__**Dentist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_direwolf(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*The Direwolf is a beast, yet it doesn't rely on instinct. The Direwolf is a machine, yet it cannot be upgraded. The Direwolf is impossible, yet it is not fictional. The Direwolf is evil, yet it is not fallible. The Direwolf is godly, yet it is not righteous. The Direwolf is coming. The Direwolf is coming for you.*
**Actions:**
*Maul* - Discuss with other Wolves in a private channel who to Strong Attack during the night.
*Pack Offensive* - Once per game, at night, not before NIGHT 3, instead of using *Maul*, the Wolves may choose to each individually target any player with a Standard Attack.
*Infect* - Each night, choose a non-Wolf player. That player gains an Active Unstoppable Save. This Save is always bypassed by *Maul* and *Pack Offensive*. If this Save is used before the start of the next night, that player becomes an Evil Werewolf, or an Evil Bloodhound if they were a Vampire. Until the start of the next night, the chosen player appears to be an Evil Werewolf when targeted with *Investigate*.
**Abilities:**
- May still speak in the Wolf channel when dead.
- Leads the Wolves - while alive, always makes the final choice on the target of *Maul*.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Killing/Support
- Wolf
- Faction: *Wolves*
- Unique""",colour=0xff5000)
        embed.set_thumbnail(url=icons["direwolf"])
        await where.send("__**Direwolf**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_doctor(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*I tried, alright? I tried to be all I could be. I followed my oaths, I learned my ways, I did everything that was asked of me. But I needed the money and, well, can you blame me for it? This title is not one I deserve after what I've done and, in any other circumstance, I wouldn't take it. But these people are hurt, dying and constantly screaming for help. These people need a helping hand, a light through the tunnel, a saviour. These people need a doctor.*
**Actions:**
*Amputate* - May target one player with an amputation every night. If that player is Good, they lose all Queued Saves. If they are Neutral, they are targeted with a Standard Attack. If they are Evil, they are targeted with a Powerful Attack.
*Heal* - If they don't use *Amputate*, may give one player a Lunar Strong Save instead.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Killing/Protective
- Human""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["doctor"])
        await where.send("__**Doctor**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_dodomeki(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*She seemed to have come out of nowhere, frequenting the temple upon the hill. The unusually long sleeves of her robe were strange, and the frail hands which somehow emerged from the ends never failed to unnerve whoever noticed them. But none knew that under the light of the moon, the robe would come off. Hundreds of eyes, wrapped round thickly veined forearms, would open into the windows of the soul.*
**Actions:**
*Eyes On You* - Every other night, may choose a player. The Dodomeki learns the names of all of the actions that player used that night.
*Inescapable Gaze* - Once per game, at night, can choose to be told every players' targets for all their actions that night.
*All-Seeing* - Once per game, at night, may choose to be told the list of roles that were present at the beginning of the game, excluding Neutral roles.
**Abilities:**
- Is told all players who targeted them during the night at the end of the night.
- May only use one action per night.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Investigative
- Unearthly
- Unique
- Achievable""",colour=0xff2323)
        embed.set_thumbnail(url=icons["dodomeki"])
        await where.send("__**Dodomeki**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_drunk(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Ugghhhh... Dang, what happened last night? Where am I? Who am I? Ah, I'm sure it'll come to me eventually...*
**Abilities:**
- Gains an Active Standard Save at the start of every night.
- At the start of NIGHT 3, a random Achievable role is chosen. The Drunk becomes that role.
- If they die before NIGHT 3, they gain the Spectre modifier.
**Objectives:**
- None
**Tags:**
- Neutral
- Chaos
- Human
- Unique""",colour=0xffffff)
        embed.set_thumbnail(url=icons["drunk"])
        await where.send("__**Drunk**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_emissary(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Relinquish* - At night, may commit suicide. The Harbinger gains a Queued Powerful Save. 
*Venerate* - Twice per game, at night, may give the Harbinger either a Queued Standard Save or an Active Powerful save. 
**Abilities:**
- Learns the identity of the Harbinger upon becoming an Emissary.
- Cannot change role, objective or alignment by any means.
- If killed by any means other than *Relinquish*, the Harbinger gains an Active Standard Save.
- If twinned whilst becoming an Emissary, the Twin also becomes an Emissary. If twinned with the Harbinger, this does not apply. 
- This role cannot be achieved by the effect of Drunk, unless there is a Harbinger present. 
- Does not need to be eliminated for the Harbinger's objective to be fulfilled.
**Objectives:**
- Have the Harbinger complete their objective.
**Tags:**
- Neutral
- Protective/Support
- Human
- Faction: *Prophets*
- Achievable""",colour=0xd5ff77)
        embed.set_thumbnail(url=icons["emissary"])
        await where.send("__**Emissary**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_fate(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Create Spinster* - Every night, may choose one player. If that player is Good, they become the Spinster and join a private channel with the Fate. After this succeeds, the action may not be used again.
*Create Inevitable* - After turning a player into the Spinster, every night, may choose one player. If that player is Evil, they become the Inevitable and join a private channel with the Fate and Spinster.
*Measure Lifespan* - Once per game, after the Spinster uses *Spin Destiny*, the Fate must choose which night (after the current night) that the Herald must die upon. If the Herald is alive at the start of the day after this night, the Spinster, Fate and Inevitable will all commit Suicide.
**Abilities:**
- While the Spinster and Inevitable are alive, gains a Lunar Powerful Save at the start of each night.
**Objectives:**
- Change a player into the Herald and have at least one member of the Witches survive until all other roles have been eliminated.
**Tags:**
- Neutral
- Chaos/Support
- Unearthly
- Factions: *Coven, Witches*
- Unique""",colour=0xe897ff)
        embed.set_thumbnail(url=icons["fate"])
        await where.send("__**Fate**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_feral(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Abilities:**
- Starts the game with a Queued Strong Save.
- For objectives purposes, act as if this player was a Wolf.
- When targeted with *Investigate*, this player appears to be an Evil Werewolf.
**Tags:**
- Modifier""",colour=0xff5000)
        embed.set_thumbnail(url=icons["feral"])
        await where.send("__**Feral**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_geneticist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Experiment* - Every night, while not in a Twins chat, can choose any 2 players to become Twins. The Geneticist joins the private channel created for these twins, and leaves it if both twins die. If the twins are required to choose an alignment between them, the Geneticist chooses for them.
**Abilities:**
- The Twin modifier cannot be applied to the Geneticist.
- Is told the identity of all players with the Twin modifier at the start of the game, however not which player they are twinned with.
- Does not need to be killed to fulfill the objective of any player whom they are in a twins private channel with.
**Objectives:**
- Survive until the end of the game.
**Tags:**
- Neutral
- Chaos/Support
- Human
- Unique""",colour=0x9900ff)
        embed.set_thumbnail(url=icons["geneticist"])
        await where.send("__**Geneticist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_gladiator(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*The clang of steel, the smell of blood and the inescapable roar of the masses. Two enter, one makes it out alive. Only the people can save you now.*
**Actions:**
*Challenge* - Every three nights, may challenge another player. The next day, so long as the Gladiator is still alive, the only players that can be voted to be Lynched are the Gladiator and their target. The Lynching is an Unstoppable Attack rather than a Standard one.
**Abilities:**
- If the Gladiator is Mayor or Deputy, they may use *Challenge* every two days instead of every three.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Counteractive/Killing
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["gladiator"])
        await where.send("__**Gladiator**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_glazier(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*It was his finest creation yet. A delicate coat of glass fixed on the finest layer of silver, a bronze, ornately-carved frame wrapping itself around the smoothed edge, and of course, just a pinch of infused magic.*
**Actions:**
*Reflect* - 3 times per game, at night, can choose to reflect all actions for the night. That night, all actions that target the Glazier are targeted instead at the player who used the action. If the Glazier is targeted by the Wolves' attack, a Wolf is randomly selected to be targeted instead. An exception is made for Suicides; the Glazier still commits Suicide if an effect would cause them to. 
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Counteractive
- Human""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["glazier"])
        await where.send("__**Glazier**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_glitch(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Temporal Accelerator* - Once per game, at night, the day after this action is used is skipped, meaning that there are two nights taken consecutively. 
*Virus* - Every night, may select a player. Until that player's death, any action that player makes has a randomised target other than the Glitch. This action cannot be used until that player is dead. 
**Abilities:**
- If an even number of actions target the Glitch in any given night, the players performing said actions now each target a random other player targeting the Glitch.
- All saves the Glitch receives become Active, regardless of their previous state.
**Objectives:**
- Be the last player alive or finish the game with no living players.
**Tags:**
- Neutral
- Chaos
- Ethereal
- Unique""",colour=0xd5ff77)
        embed.set_thumbnail(url=icons["glitch"])
        await where.send("__**Glitch**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_guide(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*We'd met under some... unusual circumstances, but it's my duty to teach the page my ways - after all, I'm the only one of my kind around here.*
**Abilities:**
- See Page ('*w.roles_page*').
- Can only be applied to a Neutral role.
**Tags:**
- Faction: *School*
- Modifier
- Achievable""",colour=0xffffff)
        embed.set_thumbnail(url=icons["guide"])
        await where.send("__**Guide**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_hacker(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*That's the problem with today's society. Everything's **digital**. Any idiot with a computer and a bit of luck is able to steal thousands from your wallet, without ever having to nab a single coin. I mean, seriously, could you imagine that? Some virgin in his mother's basement could - oh, I don't know - deprogram a direwolf, steal precious intel on his cohorts, tell the entire city every last secret they have in their paws... all with a laptop and a few clicks of a mouse.*
**Actions:**
*Hack* - Every night, may choose another player and flip a coin until they get tails. The Hacker is told that player’s alignment, and for every heads, the target of one of their previous actions, starting from their latest action. If an action has multiple targets, the Hacker is told all targets. The Hacker is not told when these actions were used, just the order in which they were leading up to the present.
*Deprogram* - Once per game, may choose one player. If that player has changed role, alignment or modifiers since the start of the game, they become what they were at the beginning of the game.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Investigative/Support
- Human
- Unique
- Achievable.""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["hacker"])
        await where.send("__**Hacker**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_hangman(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Behind the black veil, nobody truly knows what twisted thoughts are swimming through the dark void of his psyche. All we know is that the poor soul who incurred his wrath better start running.*
**Abilities:**
- Is given the name of a randomly determined Good player to be their Prey at the start of the game.
- If their Prey is killed at night, another Prey is randomly generated from the remaining Good players. If there are no Good players remaining, the Hangman commits Suicide.
- Any Lynching against their Prey is an Unstoppable Attack rather than a Standard Attack.
**Objectives:**
- Live to see their Prey be lynched by the town. The Hangman still wins if their Prey is resurrected by any means.
**Tags:**
- Neutral
- Chaos/Counteractive
- Human
- Unique""",colour=0xbcbcbc)
        embed.set_thumbnail(url=icons["hangman"])
        await where.send("__**Hangman**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_harbinger(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*War* - Every night, may select two players. Those players target each other with an attack equal to the strength of the last save they received. If a selected player doesn't have a save, they use a Standard Attack. 
*Famine* - Every night, may choose to make all actions that would give a player a save the night this action is used automatically fail. 
*Pestilence* - Every night, may select a player. Any player that player targets with an action and any player who targets that player with an action is targeted with a Standard Attack. The Harbinger is immune to any attacks that would occur as a result of this. 
*Death* - Every night, may choose to make a random player be targeted with an Unstoppable Attack. If there are more Good roles than Evil roles, this player is a randomly selected Good player. If there are more Evil roles than Good roles, this player is a randomly selected Evil player. 
*End of Days* - All players commit suicide. This action can only be used if *War*, *Famine*, *Pestilence* and *Death* have been used at any point in this game. If any player is alive at the start of the day after this action is used, they become an Emissary. 
**Abilities:**
- Cannot use more than one action per night.
- The Harbinger's presence is announced at the start of the game. 
- If targeted with *Investigate*, the player who targeted them cannot speak the during following day. If they have any uses of *Publish*, they lose them.
- If any effect would cause their alignment to change, the effect fails and the player whose role caused the effect becomes an Emissary. 
- Cannot have any Modifiers applied to them at the start of a game. 
- If revived, by any means, they may use *End of Days* as if all conditions had been fulfilled.
**Objectives:**
- Finish the game with no living players.
**Tags:**
- Neutral
- Unearthly
- Chaos/Killing
- Faction: *Prophets*
- Unique""",colour=0xd5ff77)
        embed.set_thumbnail(url=icons["harbinger"])
        await where.send("__**Harbinger**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_heir(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Heritage* - During NIGHT 1, must choose a player to be their Loved One. This action may be used whenever the Heir does not have a Loved One. The Heir is told their Loved One's role.
*Contact* - Every night, may send a message to their Loved One. Their Loved One is told that this is a Whisper.
*Disown* - Once per game, may cause their current Loved One to lose that status.
*Smother* - Starts the game with no uses of this action. At night, may choose a player to target with a Standard Attack.
**Abilities:**
- If their Loved One dies, the Heir gains a Queued Save for each Attack their Loved One has dealt with any of their actions or abilities since becoming their Loved One, of equal strength to those attacks and in the same order, and on the next night gains an amount of uses of *Smother* equal to the amount of Saves that have been given by any of the Loved One's actions or abilities since they became a Loved One.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Killing
- Human
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["heir"])
        await where.send("__**Heir**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_herald(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Ruin* - Must choose a player to target with an Unstoppable Attack every night. If the Herald does not choose a player, then a player is randomly chosen. If a player is randomly chosen, then that player may not be the Spinster, the Fate or the Inevitable. The Herald is told which player was randomly chosen.
**Abilities:**
- Gains an Active Standard Save at the start of every day.
- Does not need to be eliminated to fulfill any other roles' Objectives, excluding roles in the Coven faction.
**Objectives:**
- Survive to see the Spinster, Fate and Inevitable die.
**Tags:**
- Neutral
- Chaos/Killing
- Arcane
- Unique
- Achievable""",colour=0xe897ff)
        embed.set_thumbnail(url=icons["herald"])
        await where.send("__**Herald**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_hermit(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*I remember a young man. The young man left his home in the slums of New Marais. The young man climbed mountains, saved villages, walked through warzones and saw foreign lands. The young man lived a life of passion and adventure. That young man is not me. I have his name, I have his eyes but I do not share his fire. One day, the young man died and I walked away in his place, with a goal not to travel but to find a final resting place, lay down and complete the journey. It appears I have only one destination left.*
**Actions:**
*Uncover* - Every night, chooses one player. All of that player's actions for that night fail. At the start of the next day, it is announced that the Hermit has uncovered the [their role]. The chosen player's name and alignment are not stated. From that point onwards, when the chosen player is targeted with *Investigate*, they appear to be a random role of the opposite alignment to them, unless they are Neutral in which case they will appear as their own role.
**Abilities:**
- When their objective is fulfilled, the Hermit commits Suicide. The announcement of their death in this instance will instead say that they have 'continued on their journey', and their role is revealed as per usual.
**Objectives:**
- Live to a point when all living players other than the Hermit have been targeted with *Uncover*.
**Tags:**
- Neutral
- Investigative/Counteractive
- Human
- Unique""",colour=0x00f6ff)
        embed.set_thumbnail(url=icons["hermit"])
        await where.send("__**Hermit**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_hitman(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Terminate* - Every night, may target any player with a Standard Attack.
*Neutralise* - Three times per game, while not using *Terminate*, may choose a player. That player loses all their Standard and Strong saves.
**Abilities:** 
- At the start of NIGHT 1, a random player, other than the Hitman, becomes the Hitman's Client. The Hitman is told this player's identity and the Client is told that they have become such.
- The Client, during that night, chooses a role. They must choose again if this role is not present in the game. The Hitman is informed of the Client's choice. All players with the role chosen by the Client become Targets.
- If all Targets die by means other than an attack from the Hitman, or the Client is killed, a new Client is chosen and new Targets are set during the following night. 
- After a Target is killed by the Hitman, the Hitman gains a Strong save, and a new Client is chosen who chooses a new role.
**Objectives:**
- Kill an amount of Targets by the end of the game equal to a quarter of the amount of players, rounding down. 
**Tags:**
- Neutral
- Killing
- Human""",colour=0xbcbcbc)
        embed.set_thumbnail(url=icons["hitman"])
        await where.send("__**Hitman**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_hooligan(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*There are good men. There are heroes, there are angels, there are saints and there are paragons. But there are bad men. Men who'll crack your skull open with knuckledusters if you look at them the wrong way. Men who'll make blood pour from your mouth like the first plague of Egypt. Men who'll gladly take your money and your woman without a second thought, safe in the knowledge that you'll do absolutely fucking nothing about it. And make no mistake, I am a very, very bad man.*
**Actions:**
*Threaten* - Every night, may choose one player. For each Attack that targets that player, the Hooligan targets them with another of equal strength. The Hooligan is told how many attacks they targeted the player with, if any.
*Bully* - Every other night, may choose a player. This player cannot be the same player targeted by *Threaten*. All of this player’s Active and Lunar saves are removed.
*Etch* - Once per game, may have two real words or players’ names sent to the Wolves chat. The Wolves are told that this is from a Hooligan. The Hooligan is told if no Wolves are alive.
**Abilities:**
- Is told the identity of the Direwolf at the start of the game.
- If they are Lynched, even if Saved, on the following night *Maul* is a Powerful Attack rather than a Strong Attack.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Killing/Support
- Human""",colour=0xff2323)
        embed.set_thumbnail(url=icons["hooligan"])
        await where.send("__**Hooligan**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_hunter(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*With a hare roasting over an open flame and a bullet in the chamber, his eyes scan every trunk, every leaf, every passing grain of dirt. Another wolf infestation? These mutts should know that these are* his *woods. And if they want to take it from him? They'll have to rip his throat out first.*
**Actions:**
*Shoot* - If attacked or lynched, is given the opportunity to target any player with a Standard Attack. This Attack is instead Powerful if the target is a non-Human. This still takes effect if they are Saved.
*Martyr* - Once per game, at Night, can choose to make all actions that Attack target them instead of the chosen target. Attacks from *Shoot* are unnaffected by this action.
**Abilities:**
- Starts the game with a Queued Strong Save.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Counteractive/Killing
- Human""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["hunter"])
        await where.send("__**Hunter**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_inevitable(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Catalyse Doom* - Once per game, on the night that the Fate chose using *Measure Lifespan*, the Inevitable may target any player, causing them to Commit Suicide.
**Abilities:**
- While the Spinster and Fate are alive, gains a Lunar Powerful Save at the start of each night.
**Objectives:**
- Change a player into the Herald and have at least one member of the Witches survive until all other roles have been eliminated.
**Tags:**
- Neutral
- Killing
- Unearthly
- Factions: *Coven, Witches*
- Unique
- Achievable""",colour=0xe897ff)
        embed.set_thumbnail(url=icons["inevitable"])
        await where.send("__**Inevitable**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_inventor(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Being top of the class is not enough. Having twenty-seven Ph.Ds under your belt is not enough. Having an IQ exceeding double the human possible total is not enough. Being a revolutionary, once-in-a-lifetime genius, academic and philosopher is not enough. Being the most intelligent being in the universe is not enough. To hold true power, you must first be able to demonstrate it.*
**Actions:**
*Doomsday Device* - Every night, may choose to activate their doomsday device. This targets all players targeting the Inventor with any action and the Inventor themselves with an Unstoppable Attack. If this Attack results in the deaths of two or more other players, the Inventor is Saved from all Attacks that night including the Attack from the doomsday device. On the night that *Doomsday Device* is used, the Inventor may not change role or alignment, though may gain or lose modifiers.
**Abilities:**
- If targeted with *Invite*, becomes a Tardis Engineer.
- If targeted with *Infect*, becomes a Cyberhound.
- If targeted with *Investigate*, becomes a Hacker.
- If any of the above abilities are activated in the same night as one another, their affects are nullified and the Inventor uses *Doomsday Device*.
- If targeted by *Haunt*, removes the player who targeted them's ability to use *Haunt* and does not commit Suicide.
**Objectives:**
- Be the last player alive, or finish the game with no living players.
**Tags:**
- Neutral
- Chaos/Killing
- Human
- Unique""",colour=0xff9400)
        embed.set_thumbnail(url=icons["inventor"])
        await where.send("__**Inventor**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_jailor(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Jail* - May jail one player every night. None of that player's actions that night take effect, and the player does not count as targeting anybody, and no actions that target that player take effect (if an action has multiple targets including the jailed player, it still affects the other players providing it does not need to affect the jailed player to do so). If the jailed player is targeted with a Powerful or stronger Attack, the Jailor is targeted instead. The jailed player still commits Suicide if an action would cause them to.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Counteractive/Protective
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["jailor"])
        await where.send("__**Jailor**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_jester(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Look at the King, ladies and gentlemen! Look how silly he is with his crown and sceptre! Wouldn't it be funny if I threw this pie at his face? Wouldn't that be embarrassing? Wouldn't it be kooky if I tied his laces together or put a whoopee cushion under his chair? Wouldn't that be wacky? Hey, wouldn't it be fun if I slit his whore of a wife's fucking throat? Wouldn't it be nutty if I sacrificed all of his subjects to the voices in my own deranged fucking head? How about if I tortured him psychologically? If I made him my bitch?! If I fucked him in the head until the only way out was the blade of a knife? Wouldn't that be fun?!*
**Actions:**
*Haunt* - After dying from being Lynched, every night, the Jester chooses one player who voted against them in the Lynching to haunt. This player commits suicide on that night.
**Abilities:**
- If targeted with *Investigate*, then their identity is revealed to every Witch in the game.
- If killed by a Lynching, gains the Spectre modifier.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Chaos/Killing
- Ethereal""",colour=0xff2323)
        embed.set_thumbnail(url=icons["jester"])
        await where.send("__**Jester**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_knight(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*From the day I was knighted, I've followed my vows. To stand up for the common folk and to be their shield against danger. I promised that I would seek out evil and destroy it in whatever form it may be. Even now, in these dark and troubled times, I will not falter or back down. I will be a beacon of hope for the hopeless and the downtrodden, and for all creatures of the night - beware my blade.*
**Actions:**
*Strike* - Every night, can choose one player to target with a Strong Attack. If they are Saved, a coin is flipped, and on the result of a heads that player's alignment changes to the same as the Knight's if it was not already. The Knight is not told the result of the coin flip.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Killing/Support
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["knight"])
        await where.send("__**Knight**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_kresnik(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Pulse Check* - Once per game, at night, may choose to recieve a list of all Evil non-Human roles currently present in the game. The Kresnik is not told the number of each role present.
*Transform* - Once every two days, may choose to transform. At the beginning of the next night, the Kresnik's role changes to a random Good role. At the beginning of the following day, the Kresnik changes back to a Kresnik, providing that their role has not been changed by means other than this action since this action was used.
*Silver Blade* - Every night, may target any player with a Standard Attack. If the target is a Vampire, Cyberhound, Bloodhound, Cultist or Warlock, this Attack is Powerful rather than Standard.
**Abilities:**
- If the Kresnik would become a Vampire due to any action, both the Kresnik and the player using the action (randomly chosen in the case of multiple) commit Suicide.
- The Kresnik is twice as likely to appear in a game where any player is a Vampire.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Investigative/Killing
- Arcane
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["kresnik"])
        await where.send("__**Kresnik**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_mage(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Upon the peak of the village's mountain, there is always an old man practising the cryptic arts. Those daring enough to climb the mountain will always be greeted with a soothing cup of tea and a few surprising tricks.  Rumour has it that every few thousand years, when the cosmic order is in balance, he may descend back to the people he has watched over for eras. Unfortunately, the world he has returned to is now one of war and anarchy. It appears he may have to utilise his magic once more to rid the village of this evil...*
**Actions:**
*Switch* - Every night, may choose two players. The Mage learns if those players have the same alignment or not. For that night, all actions other than *Switch* that target the first player instead target the second player and vice-versa. If two Mages choose any of the same players to target with *Switch*, both of these actions fail.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Chaos/Investigative
- Arcane""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["mage"])
        await where.send("__**Mage**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_maid(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*When I came to this place, I thought it'd be the start of a new life for me. I came to assist my fellow man and offer my services to get by. But now? It's a city of pain, hatred and suffering; brother turning on brother to fight an enemy that has as much of a right to exist as the rest of us do. Well, I've had enough of this. I'm going to lift up my voice so that they'll put down their guns and we can all make it a better town for our children.*
**Actions:**
*Scrub* - Once per game, at night, may choose a player. If that player gains any saves during that night, they are targeted with two Standard attacks.
*Tidy Up* - Once per game, at night, may choose a player. If that player is targeted with any attack that night, regardless of if that attack is saved against, they commit Suicide.
*Spring Cleaning* - Once per game, at night, the following night, the player given the secondmost amount of votes in the Lynch the previous day commits Suicide (the Maid can choose which player in the event of any relevant ties).
**Abilities:**
- Cannot change alignment or objective by any means, unless they also change role. If an effect would cause the Maid to change their alignment or objective without also changing their role, it fails.
- If killed, all players who have a condition that would allow them to become an Achievable role in their abilities automatically have that condition count as being fulfilled. In the event that they have multiple, one is randomly chosen.
- Does not need to be eliminated to fulfill any player's objectives.
**Objectives:**
- Have every player alive at the start of DAY 4 (not including themselves) be in the Winning Players. Any player who commits Suicide after the start of DAY 4 does not count to this. If the game ends before DAY 4, the Maid loses.
**Tags:**
- Neutral
- Chaos/Killing
- Human
- Unique""",colour=0xff9bc4)
        embed.set_thumbnail(url=icons["maid"])
        await where.send("__**Maid**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_medium(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*The corpses pile up as a lone tear rolls down her cheek. They try dragging her away from her precious graveyard. "Your friends are buried," they say, "it's time to move on." It's not true - she's sure of it. She may be alone, but she can still hear their voices.*
**Actions:**
*Seance* - Once per game, once dead, may choose a living player to speak to for the night.
**Abilities:**
- Can speak in the #dead channel while alive and is permitted to repeat anything the dead have said.
- If targeted with *Investigate*, then their identity is revealed to every Witch in the game.
- If targeted by *Haunt*, removes the player who targeted them's ability to use *Haunt* and does not commit Suicide.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Support
- Arcane""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["medium"])
        await where.send("__**Medium**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_merchant(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Discount* - Every night, may take any action from their stock and gain access to it for the rest of the game. They may also use the gained action during the day/night that they used this action. This action is however removed from their stock.
*Advertise* - Every night, may choose any action in their stock. At the start of the following day, providing this action is still present in the Merchant's stock, it is announced that this action is in the Merchant's stock.
*Check* - At any time, may check the contents of their stock.
**Abilities:**
- Cannot change alignment or objective by any means, unless they also change role. If an effect would cause the Merchant to change their alignment or objective without also changing their role, it fails.
- Has a stock of actions that begins the game empty.
- All the actions of any player to die from a Lynching are added to the Merchant's stock.
- Their presence, but not their identity, is announced at the start of the game.
- All players other than the Merchant gain the action to once per game, at night, whilst the Merchant is alive, visit the Merchant. This action cannot be used if they do not have any other actions. They are told the contents of the Merchant's stock and must choose one of their actions (which still has uses) to lose in order to gain an action of their choice from the Merchant's stock. This action may not be used on the night on which they trade it away. If one Wolf player trades in *Maul* or *Pack Offensive*, all Wolves lose the action.
- Any player who visits the Merchant when there are no actions in their stock commits suicide that night, and any player who dies on the same night that they visit the Merchant's has all their actions added to the Merchant's stock.
- If two players visit the Merchant on the same night and both want to trade for the same action, neither gets the action but both lose the action they planned to trade.
- The Merchant is told when any player visits them, their identity and what actions they lost and gained.
- The Merchant's stock is updated at the start of every day.
**Objectives:**
- Have an amount of actions in their stock that is at least the amount of players at the start of the game at any time.
**Tags:**
- Neutral
- Chaos/Support
- Human
- Unique""",colour=0xe0be00)
        embed.set_thumbnail(url=icons["merchant"])
        await where.send("__**Merchant**__",embed=embed)
        
    @commands.command(pass_context=True)
    async def roles_minstrel(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Fingers eloquently dancing to the command of his master, the Minstrel plays a melody of despair. Whether it's the arsonist filling his canister of oil or the medium crying out to her imaginary friends, one thing's for certain - somebody's going to die tonight.*
**Abilities:**
- See Bard (‘*w.roles_bard*’).
**Objectives:**
- Survive alongside the Bard at the end of the game.
**Tags:**
- Faction: *Troupe*
- Modifier
- Achievable""",colour=0xff0098)
        embed.set_thumbnail(url=icons["minstrel"])
        await where.send("__**Minstrel**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_morty(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*O-o-oh, jeez, Rick, y-y-you threw me into a portal and now I'm... I'm in a town with wolves and... and... oh, Rick, I'm looking around this place and I'm starting to w-work up some anxiety about this whole thing.*
**Actions:**
*Brainwave* - If the player this Modifier is attached to is not a member of a faction, once per game, at night, they may choose any role and alignment to appear as if targeted with *Investigate*.
**Abilities:**
- If the player this Modifier is attached to is a member of a faction other than Good and Evil, the other members of their faction appear as a random Good Human role (generated seperately each time) when targeted with *Investigate* rather than their actual role. The Morty, however, appears as their actual role when investigated.
- If this player votes in an election or a lynching during the day, their actions may not be used during the following night.
**Tags:**
- Modifier""",colour=0xfffa00)
        embed.set_thumbnail(url=icons["morty"])
        await where.send("__**Morty**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_multipleagent(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*My watch is a nice piece of jewellery. Always loved it. The silver rim reminds me of the scope I used to kill our last mayor. I got paid quite well for that. Second-best assignment I've had since taking down a terrorist threat. I used the money to buy this watch. It wasn't much - my watch is just cheap garbage. Always hated it.*
**Actions:**
*Loyalty* - Every night, while there are two or more other players of their alignment alive (unless the Multiple Agent is Neutral), must choose a player (choosing a random player if offline). Gains the objectives and alignment of that player until the start of the next night. May not choose a player whom they have already chosen.
*Heal* - May give one player an Active Standard Save every night. This Save only takes effect if the target is of the same alignment as the Multiple Agent. If there are two or less other players of their alignment alive, this Save is Powerful rather than Standard.
**Abilities:**
- If they die, they keep their assumed objective and alignment.
- When investigated, they appear as a random non-unique role of the alignment of the player investigating them.
- If they target Good players three nights in a row with *Loyalty*, they become a Spy.
- If they target Evil players three nights in a row with *Loyalty*, they become a Backstabber.
**Objectives:**
- None
**Tags:**
- Neutral
- Chaos/Protective
- Human""",colour=0x00ff85)
        embed.set_thumbnail(url=icons["multipleagent"])
        await where.send("__**Multiple Agent**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_noir(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Just another case. It's not the same when it's your seventeenth year on the job, countless partners dead and countless criminals caught. Alls I know is I'm gonna do what I always do. I'm gonna catch every one of these lowlife fucks and make them pay. After all, it's just another case.*
**Actions:**
*Interrogate* - At night, chooses a player and guesses any category. They learn that player's categories and if they guessed correctly that player is targeted with a Standard Attack. If that player survives, the following day any Lynch against them is a Powerful Attack rather than a Standard Attack. All rules referring to *Investigate* also act on *Interrogate*, other than those in the Seer's role description.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Investigative/Killing
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["noir"])
        await where.send("__**Noir**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_page(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Imitate* - At night, can flip a coin. On a heads, they may use one of the Guide's actions of their choice, providing it can be used at that time. For actions with limited uses, they count their uses of an action seperately from the Guide.
**Abilities:**
- Talks to the Guide in a private channel.
- If the Page is in the game, a random other player with a Neutral role gains the Guide modifier.
- Does not need to be eliminated to fulfil any Neutral role's objectives.
- On the Guide's death, they gain the Guide's role.
**Objectives:**
- Identical to the Guide.
**Tags:**
- Neutral
- Support
- Human
- Faction: *School*
- Unique""",colour=0xffffff)
        embed.set_thumbnail(url=icons["page"])
        await where.send("__**Page**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_paladin(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*There once was a man who rode on horseback into our town, warning of a darkness that could never be quenched. He wore a glimmering ivory suit of armour and spoke with a voice that has seen an infinite number of years and lived to tell of them dozens of times over. His helmet's visor is able to be seen through but no man has ever had the hubris to believe themselves worthy of such an experience. It is said that those who gaze directly at his unmasked countenance will see the very eyes of the Lord staring back at them.*
**Actions:**
*Enlist* - Twice per game, may choose one player to force to guard another player of their choice. The latter player may not be the Paladin. The former player may not make any actions that night and any Attacks targeting the second player instead target the former. If any effect would cause the second player to commit Suicide, the former player instead commits Suicide.
*Bless* - Once per game, may target a different player. All of this player's actions that rules for *Investigate* apply to may be used twice that night, targeting different players.
**Objectives:**
- If an Attack is targeted towards an Evil role due to *Enlist*, the Paladin gains another use of *Enlist*. Only one use of *Enlist* may be gained by this method per night.
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Counteractive/Protective
- Arcane
- Unique
- Achievable""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["paladin"])
        await where.send("__**Paladin**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_philanthropist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Purify* - Once per game, at night, may choose a player. That player become a random Human role with the identical alignment to their previous role.
*Defend* - Once per game, at night, may cause all attacks targeting Human players to be weakened by one level (and to fail if they are Standard) for the duration of the night.
**Abilities:**
- At the start of every night, is told the identity of a random Human player.
- If they vote against a non-Human in a Lynching, the Attack against that player from the Lynching is Strong rather than Standard.
- Gains a Lunar Strong Save at the start of every night. This Save only affects Attacks from non-Humans.
**Objectives:**
- Have the game end with all living players as Human.
**Tags:**
- Neutral
- Counteractive/Support
- Human
- Unique""",colour=0xff9bc4)
        embed.set_thumbnail(url=icons["philanthropist"])
        await where.send("__**Philanthropist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_pixie(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Often found pestering those sleeping in the day. This talkative spirit flitters between the people, jumping from one choice to the next and deciding things out of pure luck. Maybe that’s how they ended up here, in this luckless town.*
**Actions:**
*Flip* - Told whenever they are being targeted by any action, including a Lynching. They are given the title of the action and asked if they want to try and flip one of their pennies to be unaffected by this action. On a heads, they are unaffected. May only flip once per action. If an action would not take effect by another means, the Pixie is not informed of it.
*Identify* - At night, may flip a penny and target any player to be told that player's alignment on a heads.
**Abilities:**
- At the start of the game, has an amount of pennies equal to half the total amount of players rounded down.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Counteractive/Investigative
- Unearthly""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["pixie"])
        await where.send("__**Pixie**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_politician(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*“Our great democracies still tend to think that a stupid man is more likely to be honest than a clever man, and our politicians take advantage of this prejudice by pretending to be even more stupid than nature made them.” - Bertrand Russell*
**Actions:**
*Rig* - If the Politician is Mayor or Deputy, once per game they can change the result of the Lynching. The Game Master announces the change and the new lynchee but not the Politician's identity.
*Regicide* - If the Politician is not Mayor or Deputy, once per game, at night, they can hang the Mayor, targeting them with an Unstoppable Attack. For all rules purposes, this Attack counts as a Lynching. The day after this action is used, the Attack from a Lynching is a Powerful Attack rather than a Standard Attack.
**Abilities:**
- Gains a Lunar Powerful Save at the start of every night.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Killing/Support
- Human
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["politician"])
        await where.send("__**Politician**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_poltergeist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*You can find many creatures of the night, but they are all nothing compared to it. With its long, slender fingers controlling every piece on the board, it is the unparalleled monarch of twilight as it swarms the chambers of every man and beast to cross it, lacing the tight noose around our throats in the gallows of our nightmares; our deaths a morsel for it to devour and our souls a trophy for its triumph. You aren't afraid of the dark, are you?*
**Actions:**
*Redirect* - Every night, can choose two players; one to redirect and one for the first player to redirect towards. All of the former player's actions that have targets used that night have their first target changed to the second player. The first player is not aware of this. The Poltergeist learns the first player’s role and alignment, in the same fashion as a Seer's *Investigate*. All rules referring to *Investigate* also act on *Redirect*, other than those in the Seer's role description. If two Poltergeists choose the same player as the first player, that player's actions fail and hence target nobody.
**Abilties**
- If two Poltergeists attempt to redirect each other, their actions fail and they both die and gain the Spectre modifier.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Chaos/Investigative
- Ethereal""",colour=0xff2323)
        embed.set_thumbnail(url=icons["poltergeist"])
        await where.send("__**Poltergeist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_poser(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Aw, you kids these days with your Snapchat and your Pokeymans and your John Green books and your insatiable lust to be "aesthetic". Y'see, I'm not like most adults. I'm cool. I'm only 38 and I signed up for a Tumblr account last night. I'm no old-timer. I love playing these Zelda games too - he's the coolest little elf boy. I get you. I'm cool, right? C'mon, tell me how cool I am.*
**Actions:**
*Pose* - Every night, chooses another player. One of that players actions is randomly selected and the Poser uses it as if it was their own action. Actions involving Attacks may only be selected if none exist that do not. Any action that is limited-use is freely usable for the purpose of this action. If the action requires a choice to be made by the player using it, such as a target, the Poser is given the minimum information needed when presented with this choice.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Support
- Human""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["poser"])
        await where.send("__**Poser**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_priest(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*As your teacher, I bid you, say it with me- Children of the Lord! The great devotion shall not be swayed, we shall be exalted! We shall see the rise of our one true saviour and live to see the day this world is cured of its sickness!*
**Actions:**
*Convert* - Once per game, can choose one player to convert to Good. In the event that this player is already Good, the Priest may not try again.
*Sacrifice* - Once per game, at night, can choose two players, one of whom is already dead. The dead player is revived as a random non-Unique Good role, and the living player commits Suicide.
*Purify* - Once per game, can remove all Lunar and Active Saves for Evil roles.
**Abilities:**
- The presence of the Priest is revealed at the start of the game, but not their identity.
- If the Priest is present, the Cultist must also be present.
- At the start of NIGHT 5, becomes a Paladin.
- If alignment is changed to Evil, becomes a Cultist.
- If any Cultist becomes a Priest, becomes a Cultist.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Counteractive/Support
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["priest"])
        await where.send("__**Priest**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_prince(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Praise* - Every night, may target any player other than themselves, who they have not already used this action on. Any limited-use actions that player may have are put in the state they were in at the beginning of the game.
**Abilities:**
- If killed by any means other than Suicide, the day after their death is skipped, meaning that there are two nights taken consecutively.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Support
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["prince"])
        await where.send("__**Prince**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_psychic(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Predict* - Every night, may choose any player and guess the name of any action. If the target player has an action of that name, the Psychic gains one use of that action. If the action is limited use, the target player loses a use of the action. If the target player does not have an action of that name, they are told that a Psychic attempted to predict their actions. If a Psychic successfully predicts *Infect*, they become a Cyberhound.
*Vessel* - Every night, if they do not use *Predict*, the Psychic may choose any player and choose any action that they have gained a use of through *Predict*. The chosen player gains a use of this action and the Psychic loses it.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Chaos/Support
- Arcane
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["psychic"])
        await where.send("__**Psychic**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_researcher(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*The laptop screen reflected off his lenses as he scanned each and every pixel of the monitor's display. It was now 3:15am but he was not deterred, not even slightly. His right hand's index finger scrolled intensely through the files on his computer. He was going to find it and he was not going to be distracted by whether that pungent aroma was his own sweat or the half-eaten ramen on his desk. Even if it meant he would have to rip apart this entire goddamn town, he was going to find these wolves.*
**Actions:**
*Research* - At night, can choose a player to observe. The Researcher is told all players that targeted the target player (in the event that the Wolves target them, the Researcher is only told that the Direwolf did, however if the Direwolf is dead then all Wolves are shown to target them). On the night that the Researcher used this action, they are not affected by any saves.
**Abilities**
- Gains a Lunar Standard Save at the start of every night.
- If they target a player with *Research* and every living player other than the Researcher and the target player appear in the results, the Researcher becomes a Hacker.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Investigative
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["researcher"])
        await where.send("__**Researcher**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_rogue(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*The fire in her eyes could warm the cool winter breeze. Finally, she had returned back to her own cut of paradise - where the pockets ran deep and the toys came out to play. Except this time, there was something different. An invading force had the people subdued and fearful. Paranoia caused everyone to lock their doors and hide their wallets. Somebody had taken her village. Somebody was going to pay.*
**Actions:**
*Steal* - Every night, may choose two players. All of the first player's Saves are removed and given to the second player. For each Save the first player had, the Rogue gains an identical Save.
*Donate* - Every night, may be told all the saves they have, and choose one Save to give to a player of their choice. This Save is removed from the Rogue.
**Abilities:**
- All Attacks targeting the Rogue are increased in strength by two levels to a maximum of Unstoppable.
- If they become Evil, they become a Dodomeki.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Counteractive/Protective
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["rogue"])
        await where.send("__**Rogue**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_rojinbi(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*He was quiet. We barely knew him, just a guy who strolled into the town one day and was found the next day in their home, with a couple of pills in one hand and a bottle of gin in the other. He's dead now, I guess. I just wish we could've known him better. He always carried himself with grace, his walk commanded respect and his posture showed humility. But, behind his eyes, there was always such a fire.*
**Abilities:**
- Commits Suicide on NIGHT 1, and appears to be a random Good Human role when dead. They are given the names of three players, randomly chosen; one Good, one Evil and one Neutral (providing there is another Neutral in the game; otherwise only two names are given). At the start of DAY 3, they are resurrected. They gain the role, alignment and modifiers of one of the players whose names they were given. They also gain all the Saves that player has at the moment the Rōjinbi is resurrected. If the player has died before that point, the Rōjinbi is still resurrected, however they gain no Saves. The player is decided using the following method: If the Direwolf is alive, then Evil. Otherwise, if the Seer is alive, then Good. If neither are alive, then Neutral (unless the Rōjinbi did not recieve the name of a Neutral player, in which case Good).
**Objectives:**
- None
**Tags:**
- Neutral
- Chaos
- Ethereal
- Unique""",colour=0xffffff)
        embed.set_thumbnail(url=icons["rojinbi"])
        await where.send("__**Rōjinbi**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_romantic(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*You try to treat your beloved well, of course, but all the clichés in the world won't be able to save them from the mayor's vote, a wolf's claws, or the blade of a knight. It's time to take action now, or else your love might die forever, your burning passion sent up in flames.*
**Actions:**
*Affection* - Every night, flips a coin. On the result of a heads, may give a Queued Strong Save to a player of their choice other than themselves.
*Distraction* - Once per game, during the day, if their Crush is going to be voted to be Lynched, they will be given the chance to change the lynchee to the second most voted player (choosing from the tied players in the event of a draw). The Game Master announces the change and the new lynchee but not the Romantic's identity.
**Abilities:**
- Is given the name and alignment of a randomly determined player to be their Crush at the start of the game.
- If their Crush is killed, they commit Suicide on the next night.
**Objectives:**
- Have their Crush be alive at the end of the game.
**Tags:**
- Neutral
- Protective
- Human
- Unique""",colour=0xbcbcbc)
        embed.set_thumbnail(url=icons["romantic"])
        await where.send("__**Romantic**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_santa(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Gift* - Every night, can give any player other than themselves a present. They recieve the present the next night. If during the day between these nights, the targeted player votes against a player of their own alignment in the Lynching, they are told that they have recieved a lump of coal. For that night, they gain the ability to target any player with a Powerful Attack. Santa is immune to this Attack. Otherwise, the player is told that they have recieved a candy cane, and that player and Santa both recieve a Queued Standard Save.
*Premium* - Every other night, may use *Gift* twice rather than once, however may not use *Gift* on the following night.
**Abilities:**
- If any effect would cause them to commit Suicide, they can choose to instead be targeted with a Powerful Attack.
**Objectives:**
- Have all other living players have received a present at the point of your death, or all other living players have received a present at the end of the game if you are still alive.**Tags:**
- Neutral
- Support
- Unearthly
- Unique""",colour=0xff9bc4)
        embed.set_thumbnail(url=icons["santa"])
        await where.send("__**Santa**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_scarecrow(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*There's something dark in this town. I can feel it in my bones, and it's everywhere. Even in my fields, something's different. Every time I wake at morning, something's changed, something's not how it was the night before. It gives me the creeps. At least I've my scarecrows watching over me.*
**Actions:**
*Curse* - Every night, selects one player. If that player dies during that night or the following day, they gain the Spectre modifier. Cannot choose the same player twice in a row.
**Abilities:**
- Gains an Active Unstoppable Save at the start of each day.
- Does not need to be eliminated to fulfil any Good role's objectives.
**Objectives:**
- Become a Spectre.
- Survive until the end of the game.
**Tags:**
- Neutral
- Chaos/Support
- Ethereal
- Unique""",colour=0xb7ffe8)
        embed.set_thumbnail(url=icons["scarecrow"])
        await where.send("__**Scarecrow**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_seer(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Her silence, well, that's the worst part of it. She doesn't raise her voice, she doesn't cry out, it's just her deathly silence. Her silver pupils scan the room and they'll lock onto you. And she then she just points. There are no words, no anger, no sorrow - only the stare. And as you're being dragged away to the gallows, her apathy is unwavering. No smirks, no grins, just the cold and unfeeling gaze. And then, as the rope is being tightened around your neck, her silence is the last thing you'll ever hear.*
**Actions:**
*Investigate* - Every night, may choose one player to investigate, and is told that player’s role and alignment, but not any Modifiers.
*Publish* - Once per game, at night, or upon recieving the results of *Investigate*, the Seer can choose to anonymously announce the results of a previous investigation publicly to all players at the start of the next day.
**Abilities:**
- Whenever they get a result of Evil on a player whom they have not previously targeted with *Investigate*, they gain a Queued Strong Save.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Investigative
- Arcane""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["seer"])
        await where.send("__**Seer**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_sentinel(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Shield* - Every night, may choose a Player. That night, all Attacks targeting the Player instead target the Sentinel.
*Parry* - Once per game, at night, when not using Thrust, can choose to give themselves a Lunar Powerful Save. If the Save takes effect, they gain a Queued Powerful Save.
*Thrust* - Once per game, at night, when not using Parry, can choose to give themselves a Lunar Powerful Save. If the Save takes effect, they target the player targeting them with a Strong Attack.
**Abilities:**
- Starts the game with three Queued Powerful Saves.
- Is told whenever they gain or lose a save, and what type it is.
- If an effect would cause them to lose all their saves, they instead lose only one.
**Objectives:**
- Successfully use up three Saves through using Shield.
**Tags:**
- Neutral
- Protective
- Unearthly""",colour=0x00f6ff)
        embed.set_thumbnail(url=icons["sentinel"])
        await where.send("__**Sentinel**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_sharpshooter(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Scope* - Every night, may choose one player to scope, and is told that player’s role and alignment, but not any Modifiers. The Save that player gained most recently is removed. All rules referring to *Investigate* also act on *Scope*, other than those in the Seer's role description.
*Snipe* - Once per night, can choose any player and guess their role. If they guess the player's role correctly, that player is targeted with a Strong Attack. If the chosen player survives this attack, they lose their weakest save. Cannot be used in the same night as Scope. Cannot target the same player twice in a row. This action's target cannot be changed from the Sharpshooter's original choice by any other effect.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Investigative/Killing
- Human
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["sharpshooter"])
        await where.send("__**Sharpshooter**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_shifter(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*A dark presence darts around the townsfolk. Its flickering form gradually corrupts and dissolves the body's soul as it passes through - who knows what chaotic influence brought it into existance, or what force could ever take it out.*
**Actions:**
*Shift* - Once per game, select another player. The Shifter receives that player’s role, alignment, objectives and any tags or modifiers, while that player loses their role, alignment, objectives and tags or modifiers to become a Shifter. Queued Saves are not transferred in either of these role changes. If the target of this action has an Achievable role, the action fails. Achievable modifiers do not make any difference.
**Abilities:**
- If a Seer targets a Shifter with *Investigate*, the Seer immediately commits Suicide.
- If a Shifter targets another Shifter with *Shift*, they both immediately commit Suicide. Any player the other Shifter has targeted does not change role.
- If a player spends three nights in total as a Shifter (these do not need to be consecutive), they become a Souleater.
**Objectives:**
- None
**Tags:**
- Neutral
- Chaos
- Ethereal""",colour=0xd5ff77)
        embed.set_thumbnail(url=icons["shifter"])
        await where.send("__**Shifter**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_shinigami(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Naïve children. You're all so petulant, so mortal. Don't you realise that you don't want to play this game with me? You can't run from me, you can't hide from me, you can't defeat me yet you seem so insistent on trying. You think this is your game but I haven't had my turn. You think you hold all the cards until you realise you've got nothing but a Dead Man's Hand.*
**Actions:**
*Channel Death* - Targets one player each night. If any of that player's actions or abilities would cause any player to gain a Save that night, the player who would gain the save is instead targeted with an Attack of equal strength. If a player dies from this effect, it is stated that a Shinigami killed them, and the Shinigami gains the Save the dead player would have received.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Counteractive/Killing
- Unearthly
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["shinigami"])
        await where.send("__**Shinigami**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_slasher(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Slaughter* - Every night, may choose one player to target with  a strong attack. On the night that the Slasher uses this action, any player who targets the Slasher with an attack will be targeted with a standard attack three nights later.
*Mask* - Once per game, at night, when not using *Slaughter*, may choose to use their mask. On the following day, if the Slasher is voted to be lynched, the lynch is changed to the second most voted player (randomly chosen in the event of a tie). It is announced that a Politician has used *Rig*.
*Legacy* - Once per game, only during NIGHT 1, the Slasher chooses a player. In the event of the Slasher's death at any point after this action is used, the chosen player becomes a Slasher.
**Abilities:**
- At the start of NIGHT 1, the Slasher gains two uses of *Mask*.
**Objectives:**
- Be the last player alive, or finish the game with no living players.
**Tags:**
- Neutral
- Chaos/Killing
- Unearthly
- Unique""",colour=0xff9400)
        embed.set_thumbnail(url=icons["slasher"])
        await where.send("__**Slasher**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_souleater(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Wake from your sleep. Free yourself of your skin. Rid yourself of these mortal shackles. Open your eyes. Come to me, my brother, and we shall walk to the promised land together. Today, we escape.*
**Actions:**
*Absorb* - Every two nights, can choose one player to gain the Soulless modifier.
*Evocation* - At any time, may choose any Soulless player and write a message which is given to them anonymously.
*Consume* - At any time, once per day or night, can choose one Soulless player to force to commit Suicide. This player can not have gained the Soulless modifier in the previous or same night.
**Abilities:**
- Gains a Lunar Standard Save at the start of every night.
- If targeted with *Investigate*, the player who targeted them gains the Soulless modifier.
- If Souleater gains the Soulless modifier by any means, all players including the Souleater lose the modifier.
- Becomes a Spectre if killed by a Soulless player.
**Objectives:**
- Be the last player alive, or finish the game with no living players.
**Tags:**
- Neutral
- Chaos/Killing
- Ethereal
- Achievable""",colour=0xd5ff77)
        embed.set_thumbnail(url=icons["souleater"])
        await where.send("__**Souleater**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_soulless(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Abilities:**
- See Souleater ('*w.roles_souleater*').
**Tags:**
- Modifier
- Achievable""",colour=0xd5ff77)
        embed.set_thumbnail(url=icons["soulless"])
        await where.send("__**Soulless**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_spectre(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Whether your heart is full of gold or ice, whether your lungs are full of nitrogen or ectoplasm, whether your hand holds a stick or a sceptre, there are four words that shall forever echo in the hearts of men, gods and beasts. Four words that cross the divine border and unite kings and pawns. A mantra that can resist shimmering fangs and slashing blades: **I Will Not Die**.*
**Abilities:**
- This modifier may only be applied to a dead player. If a player with the Spectre modifier is resurrected they lose the modifier and do not regain it if they die again. If a player gains the Spectre modifier by any means when alive, they die, but keep the modifier.
- Players with this modifier may use their actions and abilities as if they were living players. They may target living or dead players, however these actions only take effect on dead players if they also have the Spectre modifier.
- If Attacked by another Spectre and cannot Save against the Attack, the player loses the Spectre modifier and is not resurrected.
- Players with the Spectre modifier may only speak in the #dead chat like ordinary dead players, unless they are a Medium. Mediums with the Spectre modifier may vote in elections and lynchings.
- A Shifter with the Spectre modifier is resurrected if they switch roles with a living player, however their target does not retain the Spectre modifier and dies, unless they were dead and already had the modifier.
**Objectives:**
- Players with the Spectre modifier still pursue their objectives, however they do not count as living.
**Tags:**
- Modifier
- Achievable""",colour=0xb7ffe8)
        embed.set_thumbnail(url=icons["spectre"])
        await where.send("__**Spectre**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_speedster(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Supercharge* - Twice per game, at night, may choose to make all their actions act as if they were at the start of the night instead of at the end, hence acting before all effects used that night. This cannot be used on two consecutive nights. The day after this action is used, the Speedster cannot speak or vote.
*Godspeed* - Once per game, at night, may choose to cause the following day to last a maximum time of five minutes, or three minutes if the gamemode is Quickfire. The day after this action is used, the Speedster cannot speak or vote.
**Tags:**
- Modifier""",colour=0x80659a)
        embed.set_thumbnail(url=icons["speedster"])
        await where.send("__**Speedster**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_spider(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*The web of pain and sin it weaves will often go unnoticed. Whilst we're busy fighting wolves, gods and demons, it makes its way into our consciences, threading its little fears in there. It'll lace its hands around the bodies of the dead, breathing wicked life into these cold lungs like the cruel seductress it truly is, the dark mother of all of us... I mean, them. Oh, shit, I wasn't meant to say that, was I? You won't tell anybody, will you? Nah, she'll make sure you don't.*
**Actions:**
*Thread* - Once per game, at night, can use their Thread and choose any dead player. The #dead chat is given the chance to vote collectively on which dead player is to be revived, and the player chosen by the Spider gains an extra vote, and wins all ties. The player revived as a result of this action gains a Queued Powerful Save.
*Web* - This action has three charges. At night, can choose to activate their Web and choose an amount of charges to use. This action may not be used once all charges are depleted. All players who target them that night have all their actions fail that night, and for an amount of subsequent nights equal to one less than the amount of charges used.
**Abilties:**
- If killed by Wolves, becomes a Spectre.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Counteractive/Support
- Unearthly
- Unique""",colour=0xff2323)
        embed.set_thumbnail(url=icons["spider"])
        await where.send("__**Spider**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_spinster(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Spin Destiny* - Once per game, if the Spinster, Fate and Inevitable are all alive or Spectres, may choose any dead player to resurrect. This player becomes a Herald.
**Abilities:**
- While the Fate and Inevitable are alive, gains a Lunar Powerful Save at the start of each night.
**Objectives:**
- Change a player into the Herald and have at least one member of the Witches survive until all other roles have been eliminated.
**Tags:**
- Neutral
- Support
- Unearthly
- Factions: *Coven, Witches*
- Unique
- Achievable""",colour=0xe897ff)
        embed.set_thumbnail(url=icons["spinster"])
        await where.send("__**Spinster**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_spy(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""**Actions:**
*Infiltrate* - Every night, can target any player. The spy is told any Modifiers that player has, and the names of all of the Private Channels that they are in.
*Surveillance* - Once per game, at night, may choose to recieve the amount of Good, Neutral and Evil players currently alive. A random one of the numbers given will differ from the actual value by one.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Investigative
- Human""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["spy"])
        await where.send("__**Spy**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_standuser(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Standing over his opponent, the man looks down in contempt at him, a pitiful wreck asking for forgiveness. "Good grief." A shimmering muscular figure materialises, fists laden with gold, hair waving in the cold wind. "There's a reason you lost." In a swift motion, he traces a finger along the rim of his cap. "You pissed me off."*
**Actions:**
*Battle Cry* - Once per game, after using any action, may use that action immediately again without expending a use, even if they have no uses remaining. If an action used using *Battle Cry* would usually use up anything from a limited pool, it does not. If this action is used on an action used by a faction, if each member of the faction were to do something individually from the action only the Stand User gains an additional use of this.
*Stand Arrow* - Upon death, may choose to flip a coin. On a heads, a player of their choice gains the Stand User modifier.
*Clash* - Once per game, can choose to target any player with a Powerful Attack. Players are only affected by this attack if they have the Stand User modifier. If the chosen player dies as a result of this attack, this player gains another use of *Battle Cry*.
**Abilities:**
- If any Stand User exists in a game, at least one other player must also have the Stand User modifier.
- If uses *Battle Cry* on the same night as any other player uses *Battle Cry* (and neither action fails), commits Suicide.
- If targeted with *Clash* by a player who they use *Clash* on during the same night, commits Suicide.
- If targeted with *Stand Arrow*, gains a Queued Unstoppable Save, a use of *Clash* and a use of *Battle Cry*.
**Objectives:**
- Kill another Stand User through *Clash*, or have a player who became a Stand User due to this player's use of *Stand Arrow* complete this objective.
**Tags:**
- Modifier""",colour=0x80659a)
        embed.set_thumbnail(url=icons["standuser"])
        await where.send("__**Stand User**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_survivalist(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*A million miles from home, in some castaway village of savages violently fucking and killing anything that moves. Each breath is a battle against the odds, each step is another potential landmine, each confrontation is a test of willpower where only the bravest can survive. But me? I don't just survive. I thrive. I live. And, if you dare cross me, I'll make sure you can't say the same.*
**Actions:**
*Bulletproof Vest* - Three times per game, at night, may choose to gain an Active Unstoppable Save.
*Paranoia* - Once per game, at night, may choose to cause all players targeting the Survivalist to have their action fail and to be instead targeted with a Standard Attack.
**Abilities:**
- If any effect would cause them to commit Suicide, it fails.
- Is told the identity of any other Survivalists in the game.
- Does not need to be killed to fulfill any other role's objectives.
**Objectives:**
- Survive until the end of the game.
**Tags:**
- Neutral
- Counteractive
- Human""",colour=0x00ff85)
        embed.set_thumbnail(url=icons["survivalist"])
        await where.send("__**Survivalist**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_sylph(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Death is an inevitability - the end of all things. In time, all shall bow before it. There is no man, beast or god who can resist the seductive allure of the reaper's scythe and there is nothing to ever come back from it. We must all concede inevitably - we have no say in if we die, but we do have a say in how. Whether in a blaze of glory or a wave of the blood of our enemies, we must all accept that there's no magical guardian out there to save us from it. Such a fantasy would be... ridiculous.*
**Actions:**
*Revitalise* - Once per game, at night, may choose any dead player to resurrect.
**Abilities:**
- Gains the Spectre modifier on death.
- Gains a Lunar Standard Save at the start of every night.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Support
- Ethereal
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["sylph"])
        await where.send("__**Sylph**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_tardisengineer(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Sure, it works the ship like a charm, but that aberration never stops groaning in its robotic tone. I hate to think about what remains of the young man's consciousness. A jumble of wires, mechanics and Cyberman parts - I really wonder what kind of drugs I was on when I decided to make this thing. I also really wonder if the TARDIS saved their planet of origin so I can get some more.*
**Actions:**
*Activate TARDIS* - Once per game, during the day, can choose to activate the TARDIS. At that same point in the next day (based around elections and lynchings), the whole town is told that time has been undone and the game goes back to the point when the TARDIS was activated. Any uses of actions and kills after that point are undone, however all knowledge gained remains known. The game continues from the TARDIS activation point. If the TARDIS Engineer’s role changes before time is undone, this action still takes effect.
**Abilities:**
- If they lose the Companion modifier, they become an Inventor, however they keep the alignment and objective they had as a TARDIS Engineer.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Protective/Support
- Human
- Faction: *Tardis*
- Unique
- Achievable""",colour=0x204eff)
        embed.set_thumbnail(url=icons["tardisengineer"])
        await where.send("__**TARDIS Engineer**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_thief(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*She knows this place. She knows the drunk who couldn't protect his wallet if his life depended on it. She knows the old lady who leaves her window open so God can watch over her better. She knows the kid who forgets to lock the door whenever he goes to school. Easy pickings.*
**Actions:**
*Steal* - Once every 3 nights, can choose any player. If that player is Good or Evil, one of their actions is randomly chosen. The Thief gains access to that action for the rest of the game, and that player may not use that action for the rest of the game. Both the target player and the Thief are told this. There is no effect if the target of this action is Neutral. If the target was Neutral, the Thief may try again on the following night.
**Abilities:**
- If they become Evil, they become a Dodomeki.
- Upon death or changing role, all actions taken using *Steal* are returned to the players they were stolen from, even if those players' roles have changed since the action was stolen.
- When using *Visit Merchant*, the Thief does not lose an action.
**Objectives:**
- Be the last player alive, or finish the game with no living players.
**Tags:**
- Neutral
- Chaos/Counteractive
- Human
- Unique""",colour=0xe0be00)
        embed.set_thumbnail(url=icons["thief"])
        await where.send("__**Thief**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_timelord(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Not much is known about him. A quirky stranger with a multicoloured scarf, a massive pair of ears and a bowtie just showed up one day and told me to trust him. I think he's lying... it would explain the quick heartbeat.*
**Actions:**
*Invite* - Once per game (regaining a use if the action fails), at night, may choose another player to gain the Companion modifer. This Companion joins the Time Lord’s channel. After the Time Lord regenerates, the Companion loses their Companion modifier. They also lose the modifier if they die or their alignment changes. If a player who already has the Companion modifier is targeted with *Invite*, or a player is targeted with *Invite* by two Time Lords of the same alignment on the same night, they become a TARDIS Engineer. If two Time Lords of different alignments target the same player with *Invite*, both actions fail, however the use of *Invite* is still used up.
*Sonic* - Once per game, may use their sonic device to retrieve a list of roles. The amount of roles given will be equal to the amount of players and at least half of the list, rounding up, will be present in the game. Which roles are chosen is randomly determined.
**Abilities:**
- Starts the game with a Queued Unstoppable Save called a regeneration. When this Save is used, the Time Lord’s alignment changes to Good or Evil, whichever of the two has less living players not including the Time Lord. If they are equal in size, the Time Lord changes to the opposite alignment. The Time Lord gains another use of *Invite*. In addition, the town is told that a Time Lord has regenerated, and their alignment after the regeneration.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated (If Good).
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated (If Evil).
**Tags:**
- Good
- Investigative/Support
- Unearthly
- Faction: *Tardis*""",colour=0x204eff)
        embed.set_thumbnail(url=icons["timelord"])
        await where.send("__**Time Lord**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_twin(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Two souls, eternally bonded. Our veins may pump different blood and our backgrounds may be different, but you will forever be my brother, in health and in sickness, in poverty and in richness, in peace and in war, in life and in death.*
**Abilities:**
- This Modifier is always applied to a pair of players.
- The Twins may speak in a shared channel with one another at any time.
- Upon becoming Twins, choose together the alignment and objectives of one of them to be applied to the other. If one’s alignment and objectives change, the other’s change too to be the same. If one's objectives change to 'be the last player alive', then it instead becomes 'have yourself and your Twin be the last players alive'.
- If one Twin is in the winning players, the other Twin is also.
- If one Twin dies by any means, the other commits Suicide the next night (this counts as taking an action).
- If one Twin is resurrected, the other is also resurrected.
- If one Twin gains the Spectre modifier, so does the other.
- This Modifier may not be applied to a Priest or a Cultist.
**Tags:**
- Modifier""",colour=0x9900ff)
        embed.set_thumbnail(url=icons["twin"])
        await where.send("__**Twin**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_understudy(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Grief - the very worst of all human emotions. Grief can turn a brave hero into a desperate villain. Grief can throw the strongest man into a deepening spiral of emotional paralysis. Grief can make you throw out all you know - your items, your friends, even the clothes on your back. Grief can change you, make you become something you were never meant to be. Small changes at first - new haircut, new outfit, new speech patterns - until you look in the mirror and see all that you lost. Grief can break a man. Grief can make a man.*
**Actions:**
*Imitate* - Once per game, may become the role of a dead player of their choice.
**Abilities:**
- Starts the game with a Queued Powerful Save which is lost when the Understudy uses *Imitate*.
**Objectives:**
- None
**Tags:**
- Neutral
- Chaos/Support
- Human
- Unique""",colour=0xffffff)
        embed.set_thumbnail(url=icons["understudy"])
        await where.send("__**Understudy**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_vampire(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*Never sleep again. Never dream again. Make more room for nightmares, like the one you're having right now, where my claws are creating crimson crevaces in your dainty white skin, where my eyes pierce into whatever's left of your soul as your eyes beg the question of "why?", as my fangs explore and explode with delight at the taste of your almost-human blood. You blink and pinch yourself awake but there's one problem: it was never a nightmare in the first place.*
**Actions:**
*Fangs* - Every two nights, all Vampires together may target any player. That player loses all of their saves. If that player had no saves, they become a Vampire. If the player targeted had also been targeted with Infect that night, was a Werewolf or had the Feral modifier, they become a Bloodhound rather than a Vampire.
*Stalk* - Once per game, at night, may choose to learn the identity of a random Wolf. 
**Abilities:**
- All Vampires and Bloodhounds in the game may speak in a collective private channel with one another. They may still speak in this channel after death.
- Whenever any player (other than one who was already a Vampire) becomes a Vampire or a Bloodhound, all Vampires and Bloodhounds other than that player gain a Queued Standard Save.
- If targeted by any effect that would cause an alignment change without changing the Vampire's role, commits Suicide.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Support
- Unearthly
- Faction: *Vampiric*
- Unique""",colour=0x9b0029)
        embed.set_thumbnail(url=icons["vampire"])
        await where.send("__**Vampire**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_warlock(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*The inky black fingers of the warlock are always wrapped firmly around his sceptre, his instrument of destruction. His muscular arms, both densely tattooed with sigils and spells written in an ancient script, had long, grey veins running up towards and around his neck, strangling him like a cobra. The village has never heard him speak, merely mutter incantations under his breath. There's an aura of fear about him, nobody speaks directly to him - there is no man foolhardy or brave enough. Some say he sold his soul to the devil eons ago. Few disagree.*
**Actions:**
*Damn* - Twice per game, at night, may choose a player to damn. The damned player and all players targeting them (if targeted by Wolves a random Wolf is chosen) apart from the Warlock are targeted with a Powerful Attack.
*Hell's Gate* - Once per game, may target one player. All actions that player makes on the night this action is used fails if they specifically target a Priest, Paladin, Cultist or Warlock.
**Abilities:**
- For each Good Investigative role they kill using *Damn*, the Warlock gains another use of *Damn*. Only one use of *Damn* may be gained by this method per night.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Chaos/Killing
- Arcane
- Unique
- Achievable""",colour=0xff2323)
        embed.set_thumbnail(url=icons["warlock"])
        await where.send("__**Warlock**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_werewolf(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*You think you can tell us what to do? You think you have any power over us? We are an army. We are a brotherhood. You humans can't stand a chance against us. We run this town now, bitch.*
**Actions:** 
*Maul* - Discuss with other Wolves in a private channel who to Strong Attack during the night.
*Pack Offensive* - Once per game, at night, not before NIGHT 3, instead of using *Maul*, the Wolves may choose to each individually target any player with a Standard Attack.
**Abilities:**
- May still speak in the Wolf channel when dead.
**Objectives:**
- Have at least one Evil role survive until all Good and Neutral roles have been eliminated.
**Tags:**
- Evil
- Killing
- Wolf
- Faction: *Wolves*""",colour=0xff5000)
        embed.set_thumbnail(url=icons["werewolf"])
        await where.send("__**Werewolf**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_whisperer(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*There is truly nothing as powerful and versatile as words. Three words can stand for love, six can topple a government, fourteen can show hate, a few thousand can give you a career. How many do you reckon it'd take to end a pack of wolves?*
**Actions:**
*Whisper* - Every night, chooses one role and write a message to be sent to that role. The Whisperer is told if the role is in the game or not, but if it is not in the game the Whisperer may not use this action again. The message is sent to all players with that role. Modifiers cannot be selected as targets for this action.
**Abilities**
- Gains the Spectre modifier on death if they die by any cause other than Suicide or Lynching.
**Objectives:**
- Have at least one Good role survive until all Evil and Neutral roles have been eliminated.
**Tags:**
- Good
- Investigative/Support
- Arcane
- Unique""",colour=0x5dff00)
        embed.set_thumbnail(url=icons["whisperer"])
        await where.send("__**Whisperer**__",embed=embed)

    @commands.command(pass_context=True)
    async def roles_witch(self, ctx, where = None):
        if where == None:
            where = ctx.message.channel
        embed=discord.Embed(description="""*A being of neither light nor evil, yet more destructive than both. A seductress who'll turn brother against brother and kill their entire family. A vampire who lusts for blood yet bares no fangs. A sycophant, dedicated not to malice, but to chaos. She lies in wait, her primal instinct to worship her primordial deities and protect the sisterhood - something she'll do at all costs.*
**Actions:**
*Poison* - Target one player with a Standard Attack every night. If a player is targeted with *Poison* and *Heal* on the same night by two different players, they become a Witch.
*Heal* - May give one player an Active Standard Save every night. If a player is targeted with *Poison* and *Heal* on the same night by two different players, they become a Witch.
**Abilities:**
- If the Medium is present and they are killed with *Poison*, every Witch becomes Evil and replaces their objective with ‘Have at least one Evil role survive until all Good and Neutral roles have been eliminated.’
- If the Jester is present and they are killed with *Poison*, every Witch becomes Good and replaces their objective with ‘Have at least one Good role survive until all Evil and Neutral roles have been eliminated.’
**Objectives:**
- Have at least one member of the Witches survive until all other roles have been eliminated.
**Tags:**
- Neutral
- Killing/Protective
- Unearthly
- Faction: *Witches*""",colour=0xd800ff)
        embed.set_thumbnail(url=icons["witch"])
        await where.send("__**Witch**__",embed=embed)

def setup(client):
    client.add_cog(RoleDescriptions(client))
