import os
import discord
from discord.ext import commands
import datetime
import asyncio
# discord-py-slash-commands
from discord_slash import SlashCommand, SlashContext, ComponentContext
from discord_slash.utils.manage_components import wait_for_component, \
    create_select, create_select_option, create_actionrow, create_button
from discord_slash.utils.manage_commands import create_option, create_choice, \
    create_permission
from discord_slash.model import SlashCommandPermissionType, ButtonStyle



TOKEN = os.environ.get('TOKEN')
GUILD_IDS = [914676420595310612]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)


@slash.slash(name="Smart-Contract-Generator",
             description="Auto generates smart contract",
             guild_ids=GUILD_IDS)
async def _gif(ctx: SlashContext):
    await ctx.send(content="https://github.com/smartcontractkit")

@slash.slash(name="sucuk",
             description="Spawn Sucuk Agaci",
             guild_ids=GUILD_IDS)
async def _gif(ctx: SlashContext):
    await ctx.send(content="https://pbs.twimg.com/profile_images/787701009216901126/nKVyZKgy_400x400.jpg")

@slash.slash(name="carlosmatos",
             description="hey hey heeeyyy",
             guild_ids=GUILD_IDS)
async def _gif(ctx: SlashContext):
    await ctx.send(content="https://twitter.com/i/status/1451027079911325698")

@slash.slash(name="wen",
             description="wen?",
             guild_ids=GUILD_IDS)
async def _gif(ctx: SlashContext):
    await ctx.send(content="https://res.cloudinary.com/teepublic/image/private/s--9PYBAibh--/t_Resized%20Artwork/c_fit,g_north_west,h_954,w_954/co_484849,e_outline:48/co_484849,e_outline:inner_fill:48/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1619653430/production/designs/21464394_0.jpg")


@slash.slash(name="Ege-Duran",
             description="summon",
             guild_ids=GUILD_IDS)
async def _ege(ctx: SlashContext):
    await ctx.send(content="https://instagram.fsaw2-1.fna.fbcdn.net/v/t51.2885-19/s150x150/261207102_446501896867286_4956233610293696672_n.jpg?_nc_ht=instagram.fsaw2-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=-HKvukx8JEQAX9gcZai&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT97_I-Oqs-eEED0MZUsusFJp1j62WCkZNLLrf2ES_zvCQ&oe=61D534DA&_nc_sid=7bff83")

bot.run(TOKEN)
