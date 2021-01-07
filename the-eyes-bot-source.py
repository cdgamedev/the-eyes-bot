#imports
import os
import discord

# token and client info
with open('token.txt', 'r') as file:
    TOKEN = file.read()
client = discord.Client()

# client event on ready
@client.event
async def on_ready():
    # log that the bot has connected
    print(f'{client.user} has connected to Discord!')

    # store the game activity
    _activity = discord.Activity(name='my DMs \N{EYES}', type=discord.ActivityType.watching)

    # store the status
    _status = discord.Status.online

    # set the prescense
    await client.change_presence(status=_status, activity=_activity)
    
# client event on message
@client.event
async def on_message(msg):
    # get the content of the message all as lowercase
    content = msg.content.lower()

    # if the eyes emoji is in the message or the bot is mentioned
    if '\N{EYES}' in content or client.user.mentioned_in(msg):
        # add the eyes reaction
        await msg.add_reaction('\N{EYES}')
        # if in a DM
        if not msg.guild:
            # if the message isn't from itself
            if msg.author.id != 769211890407833610:
                # reply with eyes
                await msg.reply('\N{EYES}')
    # if in DM and eyes emoji /bot not mentioned 
    elif not msg.guild:
        # if the bot isn't itself and hasn't been called a good bot
        if msg.author.id != 769211890407833610 and 'good bot' not in content:
            # send a reply
            await msg.reply('Try sending me \N{EYES}')

    # if the author is bot maker and the bot is mentioned
    if msg.author.id == 175635927954227200 and client.user.mentioned_in(msg) and not content[0] == "!":
        # if 'good bot' is in the message
        if 'good bot' in content or 'best bot' in content:
            # send a reply
            await msg.reply("I know mother, you raised me well \N{EYES}")
        # if 'love you more' is in the message
        elif 'love you more' in content:
            # send a reply
            await msg.reply("No, I love you more mother \N{EYES}")
        # if 'love you' is in the message
        elif 'love you' in content:
            # send a reply
            await msg.reply("I love you too mother \N{EYES}")
        # if 'bad bot' is in the message
        elif 'bad bot' in content:
            # send a reply
            await msg.reply("How can you lie to your child like that mOtHeR?! \N{EYES}")
    # else if the bot is mentioned
    elif client.user.mentioned_in(msg):
        # if 'good bot' is in the message
        if ('good bot' in content or 'best bot' in content):
            # send a reply
            await msg.reply("Thank you. Good human <3 \N{EYES}")
            await msg.author.send("\N{EYES} Thanks for calling me a good bot! \N{EYES}\n\nIf you'd like me on your server, add me here: https://top.gg/bot/769211890407833610")
        # if 'bad bot' is in the message
        elif 'bad bot' in content:
            # send a reply
            await msg.reply("BaD HuMaN! \N{LOUDLY CRYING FACE}")

# client event message edits
@client.event
async def on_message_edit(before, after):
    # if eyes or the bot is pinged in message add the reaction
    if ('\N{EYES}' in after.content or client.user.mentioned_in(after)):
        await after.add_reaction('\N{EYES}')
    # if eyes isn't mentioned or the bot isn't pinged in message remove the reaction
    else:
        await after.remove_reaction('\N{EYES}', client.user)

# run the client using the token
client.run(TOKEN)