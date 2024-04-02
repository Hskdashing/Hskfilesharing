from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for Bot Users
 ├ /start - Start the Bot
 ├ /about - About this Bot
 ├ /help - Help with Bot commands
 ├ /ping - Check if bot is alive
 └ /uptime - Check bot's status 
 
 ❏ Commands for Bot Admins
 ├ /logs - View bot logs
 ├ /setvar - Set variables using bot commands
 ├ /delvar - Delete variables using bot commands
 ├ /getvar - View specific variable using bot commands
 ├ /users - View bot users statistics
 ├ /batch - Create links for multiple files
 ├ /speedtest - Test bot server's speed
 └ /broadcast - Send broadcast message to bot users

👨‍💻 Developed by </b><a href='https://t.me/hskdashing/101'>@hskdashing</a>
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Help & Commands", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About Me", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:

@{} is a Telegram Bot for storing Posts or Files that can be Accessed through a Special Link.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://'>hsk v4</a>
"""
👨‍💻 Develoved by </b><a href='https://t.me/hskdashing/101'>@hskdashing</a>
"""
