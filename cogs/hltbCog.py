import discord
from discord.ext import commands
from howlongtobeatpy import HowLongToBeat

import clients.hltbClientImpl as hltbClientImpl
import utils.discordUtils as discordUtils

class hltb_commands(commands.Cog):

    hltbClient: hltbClientImpl.hltb_hunter = hltbClientImpl.hltb_hunter()

    # Constructor to init hltb_commands
    # Inputs: bot (discord.Ext.bot)
    # Outputs: None 
    # Exceptions None 
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hltb(self, ctx, arg):
        result: dict[str, str] = self.hltbClient.search(arg)
        if result: 
            url: str = result.pop('HLTB Link')
            name: str = result.pop('Name')
            image: str = result.pop('Image')
            embed: discord.Embed = discordUtils.create_field_embed(result, f"How Long To Beat {name}", url)
            if url:
                discordUtils.set_embed_image(embed, image)
            await ctx.message.reply(embed=embed)
            return  
        else:
            await ctx.reply("No matches found for this game!")
        