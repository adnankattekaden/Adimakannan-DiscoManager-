import datetime
import discord
from decouple import config

intents = discord.Intents(
    guilds=True,
    members=True,
    bans=True,
    emojis=True,
    voice_states=True,
    messages=True,
    reactions=True,
    message_content=True,
)
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    guild_id = 1234567890  # Replace with your guild ID
    channel_id = 1234567890  # Replace with your channel ID

    guild = client.get_guild(guild_id)
    channel = guild.get_channel(channel_id)

    after_date = datetime.datetime(2022, 6, 2)
    before_date = datetime.datetime(2022, 6, 5)

    count = 0
    async for message in channel.history(limit=None, after=after_date, before=before_date):
        print(message.content)


client.run(config('token'))