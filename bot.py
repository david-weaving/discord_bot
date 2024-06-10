import asyncio
import discord
import random
from discord.ext import commands, tasks
from itertools import cycle
import time
import random


#MTA2MTcyOTU2NDg3MjY3MTQwMg.GhNQC0.RzikgMs9IXk19u-Hrs5wEwZz3DuCFWgE5WDgc4
def run_discord_bot():
    TOKEN = 'MTA2MTcyOTU2NDg3MjY3MTQwMg.GhNQC0.RzikgMs9IXk19u-Hrs5wEwZz3DuCFWgE5WDgc4'
    client = discord.Client(intents=discord.Intents.all()) # HEADS UP: you might not need this line the bottom might do.
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    status_game = cycle(["with Jamison's feelings", "with the Commish's baton"])
    status_wa = cycle(["Jared through his window", "FNAF playthroughs", "two guys partake in a mutual relationship"])
    status_lis = cycle(["Britney Spears", "your non-stop whining", "James getting rolled by four Ramattras at once"])

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        change_status.start()
        post_moe.start()
        post_elmo.start()



    client.remove_command('help')

    @tasks.loop(hours=24)
    async def post_elmo():
        channel = client.get_channel(719451833759825971)
        await channel.send('https://tenor.com/view/elmo-juke-footworking-dance-gif-13971434')

    @tasks.loop(hours=24)
    async def post_moe():
        channel = client.get_channel(1022721260033146900)
        await channel.send('Daily reminder that <@623539408829677569> is a cool guy!')

    @tasks.loop(minutes=20)
    async def change_status():
        x = random.randint(0,2)
        if x == 0:
            await client.change_presence(activity=discord.Game(next(status_game)))
        if x == 1:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status_wa)))
        if x == 2:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=next(status_lis)))

    @client.event
    async def on_message(message):  # where messages seem to be comprehended

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said: '{user_message}' ({channel})")

        if message.author == client.user:
            return

        # -------------------------------------------
        user_message = message.content.lower()
        client_message = message.channel.send
        # -------------------------------------------
        if user_message == 'rock' or user_message == 'paper' or user_message == 'scissors':
            ro_ps = ['rock', 'paper', 'scissors']
            client_rps = ro_ps[random.randint(0, 2)]
            await client_message(client_rps)
            if (client_rps == 'rock' and user_message == 'scissors') or (client_rps == 'scissors' and user_message == 'paper') or (client_rps == 'paper' and user_message == 'rock'):
                await client_message('Wow, your ass really just lost a basic ass game to some discord bot.')
            if (client_rps == 'scissors' and user_message == 'rock') or (client_rps == 'paper' and user_message == 'scissors') or (client_rps == 'rock' and user_message == 'paper'):
                await client_message('You won, this game is dumb anyway, I dont care.')
            if (client_rps == 'scissors' and user_message == 'scissors') or (client_rps == 'paper' and user_message == 'paper') or (client_rps == 'rock' and user_message == 'rock'):
                await client_message('Tied.')

        if user_message == 'get him':
            await client_message('https://tenor.com/view/mike-wazowski-cursed-terror-moving-move-gif-16644513')

        if user_message == 'elmo':
            await client_message('https://tenor.com/view/elmo-juke-footworking-dance-gif-13971434')

        if message.author.id == 374249421342375946 and user_message == 'i am king':
            await client_message('KING CHARLES HAS SPOKEN! AWAIT HIS NEXT COMMAND')
        if message.author.id == 195525951864438785 and user_message == 'rock':
            await client_message('Rock on, Kyle')
        if message.author.id == 495040351187369994 and user_message == 'hi':
            await client_message('HI JARED! 😍')

        if message.author.id == 196464661435121674 and user_message == 'hi':
            await client_message('Oh, uh. Hey Matt.... 😐')
            await client_message('https://cdn.discordapp.com/attachments/639932575149850635/1061509979091259472/IMG_0998.JPG')

        if message.author.id == 331252516534747136 and user_message == 'hi':
            await client_message('HI QUEEN! 🤤')
            await client_message('https://amsterdamduckstore.com/wp-content/uploads/2021/10/Queen-Rubber-Duck-Front-Amsterdam-Duck-Store.jpg')

        if message.author.id == 374249421342375946 and user_message == 'hi':
            await client_message('HELLO MASTER, FORGIVE ME *bows*')

        await client.process_commands(message)

    @client.command()
    async def ping(ctx):
        await ctx.send(f'My latency: {round(client.latency * 1000)}ms')

    @client.command(aliases=['8ball', 'eightball', 'eight ball'])
    async def _8ball(ctx, *, question):
        e_ball = ['Yes', 'No', 'Maybe', 'Sure. Whatever. I guess.', 'Im not really listening but yeah yeah sure thing', 'LEAVE ME ALONE', 'How am I supposed to know?', 'I dont care, man', 'That was stupid', 'I cant tell, maybe ask some other time', 'Dont ask me right now', 'No way in hell', 'NOPE', 'Yeah, thats not going to work', 'You really just ask me that?', 'Oh yeah', '100%', 'YEEESSS']
        await ctx.send(f'You asked: {question}\nMy insight tells me: {random.choice(e_ball)}')

    @client.command(aliases=['commish', 'randal'])
    async def the_commish(ctx):
        x = random.randint(1, 10)
        array_commish = ['`Joker Commish`\nJoker Commish is a moderately powerful commish. He has the power to bring entire cities down with his relentless crime. Joker Commish will frequently force his thiccums to dress as batman and fight him in town square.', "`The Commish`\nThe Commish, the grandfather of all commishes and thiccums, the most powerful commish and head of the commish council. No one knows when he popped in to existence. It's said that he created all the other commishes out of boredom and could easily erase all of them out of existence with a single snap. No entity has ever been able to match his power. Legend has it that his baton is the key to defeating him.",
        "`Alien Commish`\nAlien Commish is exactly like the Commish except he's green because he's an alien. Alien Commish is extremely powerful, being the second strongest commish and holding a seat as one of the big three on the commish's council. If the Commish were to snap all the other commishes out of existence, Alien Commish would be able to withstand one snap, BUT NOT TWO.", "`ZRRRRG Commish`\nIt is unknown where ZRRRRG Commish lies on the power-scale. He teleports to where ever he likes and uses an eye beam to blast people. People hit with this blast become deformed and essentially brain dead. Once the damage is done, ZRRRG Commish teleports away.",
        "`Fat Commish`\nFat Commish in theory is an incredibly powerful commish, having almost the same powerlevel as the Commish. However, because he's fat, he's insecure about his weight and his insecurities hold him back, making him one of the weaker commishes.", "`Hell Commish`\nHell Commish oversees hell and is the fourth most powerful commish, right under Demon Commish. Hell Commish has a demformed face, with his right hand morphed in to a hammer and his left arm morphing down in to a spike. Hell Commish spends all his time wandering the scapes of hell, but he will occasionally roam outside of hell. If you're caught in his gaze, there's nothing that can be done, you're already marked for death.",
        "`The First Thiccums`\nHere, we have the first thiccums to the Commish. A 'Thiccums' is like a commish's (in most cases, also powerless) side-kick. Every commish gets to choose a thiccums as they like, and no commish is complete without them! As for the first thiccums, it is unknown whether or not he is still alive. The Commish is unpredictable and has killed thiccums for no reason and without hesitation before immediately choosing another one."]
        picture_commish =['https://cdn.discordapp.com/attachments/639932575149850635/1061508013699121182/292845_stellarian_burning-citytr4.jpg', 'https://cdn.discordapp.com/attachments/1061765084382248980/1062166794627977259/IMG_1033.GIF', 'https://cdn.discordapp.com/attachments/1061765084382248980/1062167162552324096/yFDthr.jpg', 'https://cdn.discordapp.com/attachments/1061765084382248980/1062167463783047261/pughrse.jpg', 'https://cdn.discordapp.com/attachments/1061765084382248980/1062167390462418944/reid-smith.jpg', 'https://cdn.discordapp.com/attachments/1061765084382248980/1062167080322990120/matt-hell344.jpg', 'https://cdn.discordapp.com/attachments/1061765084382248980/1062167619794391061/IMG_0432.GIF']
        if x == 5:
            await ctx.send('Look at you. Calling out for me with your little "!commish"')
        else:
            y = random.randint(0, 6)
            await ctx.send(picture_commish[y])
            await ctx.send(array_commish[y])

    @client.command(aliases=['game roll', 'gameroll', 'dicegame', 'dice game'])
    async def dice_game(ctx):
        user_roll = (random.randint(1, 6))
        bot_roll = (random.randint(1, 6))
        await ctx.send(f'You rolled: {user_roll}\nI rolled: {bot_roll}')
        if user_roll > bot_roll:
            await ctx.send('You win.')
        if user_roll < bot_roll:
            await ctx.send('Damn, you just lost to a bot.')
        if user_roll == bot_roll:
            await ctx.send('Tie.')

    @client.command()
    async def shit(ctx):
        await ctx.send('OH NO I SHIT MYSELF')


    @client.command(aliases=['rolldie', 'dice'])
    async def die_roll(ctx, *, user_response):
        x = int(user_response)
        await ctx.send("{:,}".format(random.randint(1, x)))

    @client.command(aliases=['ssp']) # ss stands for set status
    async def status_play(ctx, *, user_response):
        await client.change_presence(activity=discord.Game(user_response))
        await ctx.send(f"Status changed to Playing '{user_response}'")

    @client.command(aliases=['ssw'])
    async def status_watch(ctx, *, user_response):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=user_response))
        await ctx.send(f"Status changed to Watching '{user_response}'")

    @client.command(aliases=['ssl'])
    async def status_listen(ctx, *, user_response):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=user_response))
        await ctx.send(f"Status changed to Listening '{user_response}'")

    @client.command(aliases=['captainjohn', 'smith'])
    async def jamison(ctx):
        jam_resp = ['HI JAMISON', 'Jamiiiisoooon😩', 'GOOD HEAVENS', 'ONE DAY I WILL BE REAL AND JAMISON WILL BE MINE']
        await ctx.send(random.choice(jam_resp))

    @client.command()
    async def help(ctx):
        await ctx.send("`List of commands:\n!ping (shows bot ping)\n!8ball (ask a yes or no question for the bot's insight)\n!gameroll or !dicegame (Roll a dice 1-6 against the bot for the highest roll)\n!shit\n!rolldie [your number] or !dice [your number] (rolls a dice from 1 to whatever number you like)\n!ssp [status] (change's the bot's status to Playing [input])\n!ssw [status] (change's the bot's status to Watching [input])\n!ssl [status] (change's the bot's status to Listening [input])\n!blackjack or !21 (play blackjack against the bot)\n!integrals (math related problems with multiple choice)\n!updates (will show latest update as well as upcoming updates)\n\nEvent things to say:\n'rock' , 'paper' , 'scissors' (triggers a game of rock paper scissors against the bot)\n'elmo'\n'get him`")

    @client.command()
    async def updates(ctx):
        await ctx.send(f'`Update V1.7.1:\nGarydos Bot has been renamed to Elmo Bot.\nDaily Elmo has been retired, and Elmo Bot will take the roll of posting dancing elmo every day.\nAdded more status prompts to the bot (included "watching" and "listening to"), the bot will now cycle through prompts every 20 minutes, down from 2 hours.\nAdded a new event: "get him" can now be typed.\nFixed an incorrect integral question.\n\nComing in V1.7.2 (FINAL UPDATE BEFORE V1.8): More integrals questions with unique wrong answer results.\nComing in V1.8: Adding tensorflow to recgonize images.\nComing in V1.9: Better UI, more math prompts with unique wrong answer resaults.\nComing in V1.10: Black Jack overhaul.\nComing in V1.11: Data Base.`')

    @client.command(aliases=['blackjack', 'bj', '21'])
    async def black_jack(ctx):
        card_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9,
                     9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        random.shuffle(card_list)
        global response
        hit = "\u0332".join('hit')
        stand = "\u0332".join('stand')
        my_list = list()
        a = random.randint(0, 51)
        x = card_list[a]
        card_list.pop(a)
        b = random.randint(0, 50)
        y = card_list[b]
        card_list.pop(b)
        if x == 1:
            x = 11
        my_list.append(x)
        my_list.append(y)
        await ctx.send(f'`Your hand is: {x} and {y} for a total of {sum(my_list)}`')
        await ctx.send(f'`Would you like to {hit} or {stand}?`')
        try:
            response = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20)
        except asyncio.TimeoutError:
            await ctx.channel.send("I don't have all day, don't waste my time.")
        s = 49
        while response.content.lower() == 'hit' and sum(my_list) < 21:

            c = random.randint(0, s)
            s = s - 1
            z = card_list[c]
            if z + sum(my_list) < 11 and z == 1:
                z = 11
            my_list.append(z)
            card_list.pop(c)
            await ctx.send(f'`Your card is {z} and your hand is: {my_list} for a total of {sum(my_list)}`')
            if sum(my_list) >= 21:
                break
            if sum(my_list) < 21:
                await ctx.send(f'`Would you like to {hit} or {stand}?`')
                try:
                    response = await client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20)
                except asyncio.TimeoutError:
                    await ctx.channel.send("I don't have all day, don't waste my time.")
                    break
            if response.content.lower() == 'stand':
                break

        if sum(my_list) <= 21:
            await ctx.send('`Moving on to my cards...`')
            time.sleep(3)

        client_list = list()

        if sum(my_list) > 21:
            await ctx.send('HA LOSER YOU BUSTED')
        elif sum(my_list) <= 21:

            while sum(client_list) <= sum(my_list) and sum(client_list) < 21:
                c = random.randint(0, s)
                s = s - 1
                z = card_list[c]
                card_list.pop(c)
                if z + sum(client_list) < 11 and z == 1:
                    z = 11
                client_list.append(z)

            await ctx.send(f"`My hand is: {client_list} for a total of {sum(client_list)}`")
            if sum(client_list) == sum(my_list):
                await ctx.send("Huh, both at 21, we'll call this a draw")
            elif sum(client_list) > sum(my_list) and sum(client_list) <= 21:
                await ctx.send("HAH I WIN CRY ABOUT IT BOZO")
            elif sum(client_list) < sum(my_list) and sum(my_list) > 21:
                await ctx.send("HAH I WIN CRY ABOUT IT BOZO")
            elif sum(my_list) < sum(client_list) and sum(client_list) > 21:
                await ctx.send("Wow pat yourself on the back, such a big person beating a discord bot wow!")

    @client.command()
    async def integrals(ctx):

        global response
        integral_list = ['∫xdx', '∫cos(x)dx', 'd/dx[tan(x)]', 'lim(x->0) of 1/x', '∫sin(2x)', '∫y^5dy', '∫tanxdx', 'd/dx[1/2x^2]', '∫tan(x)sec^2(x)dx', '3 + 4','lim(x->∞) of cos(x)']
        integral_solutions = ['1/2x^2', 'sin(x)', 'sec^2(x)', '∞', '-1/2cos(2x)', '1/6y^6 + c', 'ln(|sec(x)|) + c', 'x', '1/2tan^2(x) + c', '7', 'DNE']
        integral_solutions_v2 = ['1/2x^2', 'sin(x)', 'sec^2(x)', '∞', '-1/2cos(2x)', '1/6y^6 + c', 'ln(|sec(x)|) + c', 'x', '1/2sec^2(x) + c', '7', 'DNE']
        a = random.randint(0, 10)
        x = 4
        c = 9 # this has to be 1 number below the amount of cells in the solution because we already pop one of the cells off, so if the array is 0 - 9, this value must be 8
        correct_answer = random.randint(1,4)
        integral_solutions.pop(a)
        while x != 0:

            b = random.randint(0, c)

            if x == 4:
                if correct_answer == 1:
                    A = integral_solutions_v2[a]
                else:
                    A = integral_solutions[b]
                    integral_solutions.pop(b)


            if x == 3:
                if correct_answer == 2:
                    B = integral_solutions_v2[a]
                else:
                    B = integral_solutions[b]
                    integral_solutions.pop(b)


            if x == 2:
                if correct_answer == 3:
                    C = integral_solutions_v2[a]
                else:
                    C = integral_solutions[b]
                    integral_solutions.pop(b)


            if x == 1:
                if correct_answer == 4:
                    D = integral_solutions_v2[a]
                else:
                    D = integral_solutions[b]
                    integral_solutions.pop(b)



            c = c - 1
            x = x - 1


        await ctx.send(f"`Solve: {integral_list[a]}\nChoose the answer:\nA) {A}\nB) {B}\nC) {C}\nD) {D}`")
        try:
            response = await client.wait_for("message",
                                             check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                             timeout=50)
        except asyncio.TimeoutError:
            await ctx.channel.send("Looks like you don't have what it takes.")


        if A == integral_solutions_v2[a]:
            answer = 'a'
        if B == integral_solutions_v2[a]:
            answer = 'b'
        if C == integral_solutions_v2[a]:
            answer = 'c'
        if D == integral_solutions_v2[a]:
            answer = 'd'

        if response.content.lower() == answer:
            await ctx.channel.send('Lucky guess, it was an easy question')
        else:
            if a == 0:
                await ctx.channel.send(f"`No way this dude doesn't know a basic anti-derivative 💀💀💀`")
                await ctx.channel.send("https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/integral-of-x-1637303564.png")
            if a == 3:
                await ctx.channel.send(f"`Really? You couldn't even get that right? Look at a fucking graph:`")
                await ctx.channel.send(
                    'https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/896/2016/11/02213907/CNX_Precalc_Figure_03_07_0012.jpg')
            else:
                await ctx.channel.send("HAHAHAHAHAHA YOU COULDN'T HAVE BEEN FURTHER FROM WRONG AHAHAHAHAH")




    client.run(TOKEN)



#THINGS TO ADD: COMMISH CODEX, HELP COMMAND, LOOK AT EMBEDS, RUSSIAN ROULETTE
