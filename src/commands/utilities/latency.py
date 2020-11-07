import discord
from discord.ext import commands
import time

class Latency(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def latency(self, ctx):
        prior, message = time.monotonic(), await ctx.send(f'Calculating Latency...')
        await message.edit(content=f'Client Latency is `{int((time.monotonic() - prior) * 1000)}ms` :ping_pong:')

def setup(client):
    client.add_cog(Latency(client))
