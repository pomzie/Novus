from discord.ext import commands
import os
import json

if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)

    client = commands.Bot(command_prefix=config["prefixes"])

    for subdir, dirs, files in os.walk('./src'):
        for file in files:
            filepath = (os.path.relpath(
                os.path.join(subdir, file))).replace('/', '.')
            if filepath.endswith('.py') and file != os.path.basename(__file__):
                client.load_extension(filepath[:-3])
    client.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
