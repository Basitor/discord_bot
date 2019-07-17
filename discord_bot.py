import discord
from configs import TOKEN, channel_id, guild_id, test_channel
import asyncio
from bot_helpers.messages import Messages

client = discord.Client()


class Vars:

    def __init__(self):
        self.channel = client.get_channel(channel_id)
        self.test_channel = client.get_channel(test_channel)
        self.user_name_for_troll = ""
        self.counter = 0
        self.who_used_troll = ""

    def user_for_troll(self):
        return discord.utils.get(self.channel.members, name=self.user_name_for_troll)

    def user_who_used(self):
        return discord.utils.get(self.channel.members, name=self.who_used_troll)


@client.event
async def on_message(message):
    channel = bot_vars.test_channel

    if message.author.name != client.user.name:

        if message.content.startswith(f'{client.user.mention} help'):
            await channel.send(Messages.help_message())

        if message.content.startswith(f'{client.user.mention} разберись за меня с'):
            if not bot_vars.user_name_for_troll:
                bot_vars.user_name_for_troll = message.content.split(f'{client.user.mention} разберись за меня с ')[-1]
                if bot_vars.user_for_troll():
                    bot_vars.counter = 5
                    bot_vars.who_used_troll = message.author.name
                    await channel.send(Messages.now_trolling(user=bot_vars.user_for_troll().mention,
                                                             author=message.author.name))
                else:
                    await channel.send(Messages.cant_find_user(bot_vars.user_name_for_troll))
                    if bot_vars.user_name_for_troll[0] == "@":
                        await channel.send(Messages.wrong_troll_name_format())
                    bot_vars.user_name_for_troll = ""
                return
            else:
                await channel.send(Messages.trolling_already(user=bot_vars.user_name_for_troll,
                                                             author=bot_vars.who_used_troll))
                return

        if message.content.startswith(f'{client.user.mention} харош с него') and \
                message.author.name == bot_vars.who_used_troll:
            await channel.send(Messages.enough_for_you(bot_vars.user_for_troll().mention))
            bot_vars.user_name_for_troll = ""
            bot_vars.who_used_troll = ""

        if message.author.name == bot_vars.user_name_for_troll:
            if bot_vars.counter >= 1:
                await channel.send(Messages.troll_message(bot_vars.user_for_troll().mention))
            bot_vars.counter -= 1
            if bot_vars.counter == 0:
                await asyncio.sleep(1)
                await channel.send(f"{Messages.enough_for_you(bot_vars.user_for_troll().mention)}\n"
                                   f"{Messages.are_author_satisfied(bot_vars.user_who_used().mention)}")
                bot_vars.user_name_for_troll = ""
                bot_vars.who_used_troll = ""


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    global bot_vars
    bot_vars = Vars()

client.run(TOKEN)
