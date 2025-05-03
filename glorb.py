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
            nasty_dunk(message)


def nasty_dunk(message, pre_path="coborbier"):
    guild_id = message.guild.id
    print(api_string + str(guild_id))

    tinto = {"Authorization": f"Bot {coborbier_key}"}
    print(tinto)

    api_response = requests.get(api_string + str(guild_id) + "/channels", headers=tinto)
    if api_response.status_code != 200:
        return
    response_data = api_response.json()
    api_response.close()
    for channel in response_data:
        if channel.type != 0:
            continue
        for message in channel.history()


    print(api_response)


# https://discord.com/api/v10/
# https://discord.com/api/v10/guilds/




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