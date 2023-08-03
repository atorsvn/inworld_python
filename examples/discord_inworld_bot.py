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

# Create a new Intents object with default settings
# These settings include tracking of messages, reactions, etc.
intents = discord.Intents.default()
# Enable tracking of message content
intents.message_content = True

# Initialize the Bot object with the "!" command prefix
# and the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Create an InWorldChat object with the specified key, secret, and scene
chat_app = inworld_chat.InWorldChat(CONFIG["inworld-key"], CONFIG["inworld-secret"], CONFIG["inworld-scene"])

# Set up the InWorldChat object
chat_app.setup()

@bot.command(name=CONFIG["bot-command"])
async def inworld_command(ctx, *, query):
    """
    The message content is then sent as a reply in Discord.

    :param ctx: context object provided by discord.py, contains message details
    :param query: message content to send as chat
    """
    # Send a chat message using the InWorldChat object
    # The message content, author name, channel ID, and author ID are provided as arguments
    out = chat_app.chat(query, str(ctx.author), str(ctx.channel.id), str(ctx.author.id))
    # Reply in Discord with the chat output
    await ctx.reply(out)

@bot.event
async def on_ready():
    """
    This function is run when the bot has connected to Discord and is ready.
    """
    print('Bot is ready')

# Run the bot with the specified token
bot.run(CONFIG["bot-token"])
