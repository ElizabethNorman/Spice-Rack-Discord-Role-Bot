"""
This program is a simple discord bot that applies roles to users that react to the bot's 'role message' with the
corresponding emoji of that role. The bot's 'role message' is constructed by a command by the author designated
with their ID in the .env file.
Elizabeth Norman, August 7th, 2022, @spicedboi
"""


import os
import roles
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()


token = os.getenv('DISCORD_TOKEN')
channelID = os.getenv('CHANNEL_ID')
authorID = os.getenv('AUTHOR_ID')


client = commands.Bot('.')


@client.event
async def on_reaction_add(reaction, user):
    # adds the role to the user if they used a relevant emoji
    if user == client.user:
        return
    if role_message == reaction.message:
        for role in roles.roles:
            if reaction.emoji == role.emoji:
                r = reaction.message.guild.get_role(role.discord_id)
                await user.add_roles(r)


def build_message():
    # creates the message to communicate to the server users which emoji corresponds with what role
    bot_message = ""
    for role in roles.roles:
        bot_message += "React with " + role.emoji + " for " + role.role_description + "\n"
    return bot_message


@client.command()
async def message(ctx):
    # this command will post the role message if the author is the designated one provided
    global role_message
    if str(ctx.author.id) == authorID:
        channel = await client.fetch_channel(channelID)
        role_message = await channel.send(build_message())
        for role in roles.roles:
            emoji = role.emoji
            await role_message.add_reaction(emoji)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(token)
