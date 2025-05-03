import discord, os, json, requests

api_string = "https://discord.com/api/guilds/"
coborbier_key = os.getenv('DISCORD_API_COBORBIER_KEY')

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('dew it'):
            await nasty_dunk(self, message)


async def nasty_dunk(client, message, pre_path="coborbier"):
    guild = discord.Client.get_guild(client, message.guild.id)
    for category in guild.by_category():
        for channel in category[1]:
            if channel.type != discord.ChannelType.text:
                continue
            category_path = pre_path + "/" + category[0].name + "/" + channel.name
            try:
                os.makedirs(category_path)
            except:
                pass
            messages = [message async for message in channel.history()]
            for message in messages:
                for attachment in message.attachments:
                    await attachment.save(fp=category_path + "/" + attachment.filename)



                

        


    # print(api_response)


# https://discord.com/api/v10/
# https://discord.com/api/v10/guilds/1366926543758295081




# dew it
# # take args for a path
# # get guild name
# # create directory named guild name

# # for every category in guild name
# # # create sub-folder in guild name directory

# # # for every channel in category
# # # # create sub-folder in category directory named channel name

# # # # for every image and link in channel
# # # # # put channel/link into channel directory


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(coborbier_key)