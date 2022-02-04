# (c) @AbirHasan2005

from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await m.reply_text("Hi,\n\n"
                       "ɪ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴍᴇᴅɪᴀ ғᴀsᴛᴇʀ ᴛʜᴀɴ ᴏᴛʜᴇʀ ʙᴏᴛs!\n"
                       "sᴘᴇᴇᴅ ᴅᴇᴘᴇɴᴅs ᴏɴ ʏᴏᴜ ᴍᴇᴅɪᴀ sɪᴢᴇ.\n\n"
                       "ᴊᴜsᴛ sᴇɴs ᴍᴇ ᴀ ғɪʟᴇ ᴀɴᴅ ʀᴇᴘʟʏ /rename ᴄᴏᴍᴍᴀɴᴅ.",
                       reply_markup=types.InlineKeyboardMarkup([[
                           types.InlineKeyboardButton("sʜᴏᴡ sᴇᴛᴛɪɴɢs",
                                                      callback_data="showSettings")
                                                      
                       ]]))

                       


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await m.reply_text("ɪ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴍᴇᴅɪᴀ ғᴀsᴛᴇʀ ᴛʜᴀɴ ᴏᴛʜᴇʀ ʙᴏᴛs!\n"
                       "sᴘᴇᴇᴅ ᴅᴇᴘᴇɴᴅs ᴏɴ ʏᴏᴜ ᴍᴇᴅɪᴀ sɪᴢᴇ.\n\n"
                       "ᴊᴜsᴛ sᴇɴs ᴍᴇ ᴀ ғɪʟᴇ ᴀɴᴅ ʀᴇᴘʟʏ /rename ᴄᴏᴍᴍᴀɴᴅ\n\n"
                       "ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ʀᴇᴘʟʏ /set_thumbnail ᴛᴏ ᴀɴʏ ᴘʜᴏᴛᴏ\n\n"
                       "ᴛᴏ sᴇᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟɪᴄᴋ /show_thumbnail",
                       reply_markup=types.InlineKeyboardMarkup([[
                           types.InlineKeyboardButton("Show Settings",
                                                      callback_data="showSettings")
                       ]]))
