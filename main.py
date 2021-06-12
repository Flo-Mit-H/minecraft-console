import json

import discord
import mcrcon

client = discord.Client()
config = json.load(open("config.json"))


@client.event
async def on_ready():
    print(f"Bot logged in as User {client.user.name}#{client.user.discriminator}")
    await client.change_presence(activity=discord.Game(f"{config['rich-presence']}"), status=discord.Status.online)


@client.event
async def on_message(message):
    if message.channel.id == config["console-channel"]:
        if not message.author.bot:
            if message.content.startswith(config["prefix"]):
                command = message.content[len(config["prefix"]):]
                with mcrcon.MCRcon(host=config["server-host"], password=config["server-password"], port=config["server-port"]) as server:
                    server.connect()
                    feedback = server.command(command)
                    feedback = feedback.replace("§0", "")\
                        .replace("§1", "")\
                        .replace("§2", "")\
                        .replace("§3", "")\
                        .replace("§4", "")\
                        .replace("§5", "")\
                        .replace("§6", "")\
                        .replace("§7", "")\
                        .replace("§8", "")\
                        .replace("§9", "")\
                        .replace("§a", "")\
                        .replace("§b", "")\
                        .replace("§c", "")\
                        .replace("§d", "")\
                        .replace("§e", "")\
                        .replace("§f", "")
                    await message.channel.send(f"```{feedback}```")


client.run(open("token.txt", "r"))
