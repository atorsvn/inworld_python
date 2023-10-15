import discord
from discord.ext import commands
from inworld_python import inworld_chat

CONFIG = {
    "inworld-key" : "",
    "inworld-secret" : "",
    "inworld-scene" : "",
    "bot-token" : "",
    "bot-command" : ""
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

chat_app = inworld_chat.InWorldChat(CONFIG["inworld-key"], CONFIG["inworld-secret"], CONFIG["inworld-scene"])

chat_app.setup()

@bot.command(name=CONFIG["bot-command"])
async def inworld_command(ctx, *, query):
    """
    The message content is then sent as a reply in Discord.

    :param ctx: context object provided by discord.py, contains message details
    :param query: message content to send as chat
    """
    # Send a typing indicator
    async with ctx.typing():
        # Send a chat message using the InWorldChat object
        out = chat_app.chat(query, str(ctx.author), str(ctx.channel.id), str(ctx.author.id))
        # (Optional) If needed, you can add an artificial delay here, to simulate
        # the bot "typing". For example, to wait 2 seconds before replying, you can
        # uncomment the next line:
        # await asyncio.sleep(2)
    
        # Reply in Discord with the chat output
        await ctx.reply(out)

@bot.event
async def on_ready():
    """
    This function is run when the bot has connected to Discord and is ready.
    """
    print('Bot is ready')

bot.run(CONFIG["bot-token"])
