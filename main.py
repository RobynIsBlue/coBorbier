import discord, discord, os, json, requests

api_string = "https://discord.com/api/guilds/"

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('dew it'):
            nasty_dunk(message)


def nasty_dunk(message, pre_path="coborbier"):
    guild_id = message.guild.id
    # os.mkdir(pre_path)
    print(api_string + str(guild_id))
    api_response = requests.get(api_string +  str(guild_id))
    print(api_response)


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
client.run('MTM2Njg5OTY4NTY1ODMzMzI2Ng.Goo1tc.7aarn3FfoYLccxsV_JKG1WRTwUV4KWZm5r0GFE')