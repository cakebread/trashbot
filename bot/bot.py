#!/usr/bin/env python3

import os
import time

import redis
from twitchio.ext import commands

LOG_FILE = "log.txt"
LOG_NAME = "record"

REDIS_CONN = redis.StrictRedis(
    host="redis", port=6379, db=0, charset="utf=8", decode_responses=True
)


class Bot(commands.Bot):
    def __init__(self):
        token = os.environ["TMI_TOKEN"]
        prefix = os.environ["BOT_PREFIX"]
        initial_channels = [os.environ["CHANNEL"]]
        super().__init__(token=token, prefix=prefix, initial_channels=initial_channels)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    async def event_message(self, ctx):
        "Runs every time a message is sent in chat."
        fh = open(LOG_FILE, "a")
        if ctx.echo:
            REDIS_CONN.rpush(LOG_NAME, f"TrashRoomBot: {ctx.content}")
            fh.write(f"TrashRoomBot: {ctx.content}\n")
            fh.close()
            return
        else:
            REDIS_CONN.rpush(LOG_NAME, f"{ctx.author.name}: {ctx.content}")
            fh.write(f"{ctx.author.name}: {ctx.content}\n")
            fh.close()

        if "trashy" in ctx.content.lower():
            await ctx.channel.send(f"Hey, @{ctx.author.name}, that's me!")
        elif "Trashy" in ctx.content.lower():
            await ctx.channel.send(f"Hey, @{ctx.author.name}, that's my name!")
        await self.handle_commands(ctx)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command()
    async def streams(self, ctx: commands.Context):
        streams = [
            "High quality - http://kxlu.streamguys1.com/kxlu-hi:",
            "OK quality - http://www.ednixon.com:8120/stream",
            "tunein.com - https://tunein.com/radio/KXLU-889-s26509/"
        ]
        #TODO asyncio loop
        await ctx.send(streams[0])
        time.sleep(2)
        await ctx.send(streams[1])
        time.sleep(2)
        await ctx.send(streams[2])

    @commands.command()
    async def help(self, ctx):
        await ctx.send("These are my commands:")
        time.sleep(2)
        await ctx.send(" !history - View chat log")
        time.sleep(2)
        await ctx.send(" !song - What song is playing?")
        time.sleep(2)
        await ctx.send(" !streams - Get list of KXLU listening streams")

    @commands.command()
    async def history(self, ctx):
        await ctx.send("Chat history is here https://trash.rocklosangeles.com/")

    @commands.command(name="stoners")
    async def stoners(self, ctx):
        title = open("travis.txt", "r").read()
        await ctx.send(title)

    @commands.command(name="song")
    async def song(self, ctx):
        title = open("song.txt", "r").read()
        print(title)
        if title.startswith("Unknown -"):
            title = "K-XLU is not sending song info to Spinitron at the moment."
        await ctx.send(title)


if __name__ == "__main__":
    bot = Bot()
    bot.run()
