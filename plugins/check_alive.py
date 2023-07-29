import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("Pʀᴇss 👉 /movies Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\nPʀᴇss 👉 /series Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Sᴇʀɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\n\nPʀᴇss 👉 /tutorial Fᴏʀ Tᴜᴛᴏʀɪᴀʟ Aʙᴏᴜᴛ Hᴏᴡ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Fʀᴏᴍ Mᴇ 🤗")

@Client.on_message(filters.command("credits", CMD))
async def credits(_, message):
    await message.reply_text("Tʜɪs Is Cᴏᴅᴇᴅ Bʏ @CSAdmin69_bot/n/Tʜᴀɴᴋs Tᴏ Eᴠᴀ Mᴀʀɪᴇ ﹝ ʙᴀsᴇ ᴄᴏᴅᴇ ")

@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ɪɴ ᴛʜᴇ ʙᴏᴛ ᴏʀ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴀᴠᴀᴛᴀʀ: ᴛʜᴇ ᴡᴀʏ ᴏғ ᴡᴀᴛᴇʀ\n\n🚯 ᴅᴏɴᴛ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs 🤧 ➠ ':(ᴅᴏɴᴛ ᴍᴇɴᴛɪᴏɴ ʟᴀɴɢᴜᴀɢᴇ ʙᴇsɪᴅᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ,ᴀɴᴅ ᴛʜᴇᴀᴛʀᴇ prints ᴀʀᴇ ɴᴏᴛ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴏᴜʀ ʙᴏᴛ)\n\nᴄᴏᴅᴇᴅ ʙʏ HARSHA")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴍᴏɴᴇʏ ʜᴇɪsᴛ S01E01\n\n🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(Money Heist season 1,ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢᴀ sᴇᴀsᴏɴ ᴀɴᴅ ᴇᴘɪsᴏᴅᴇ ᴍᴇɴᴛɪᴏɴ ᴄʜᴇʏᴀɴᴅɪ ғᴏʀ ʙᴇᴛᴛᴇʀ ʀᴇsᴜʟᴛ ʟɪᴋᴇ ᴀʙᴏᴠᴇ ғᴏʀᴍᴀᴛ)\n\nᴄᴏᴅᴇᴅ ʙʏ HARSHA")

@Client.on_message(filters.command("download", CMD))
async def tutorial(_, message):
    await message.reply_text("Fɪʀsᴛ Cʟɪᴄᴋ Tʜɪs Lɪɴᴋ 👉 https://t.me/cstutorialvideo/n/n Aғᴛᴇʀ Watching Tʜᴇ Vɪᴅᴇᴏ Sᴇɴᴅ Aɴʏ Mᴏᴠɪᴇs / Sᴇʀɪᴇs Nᴀᴍᴇ Wɪᴛʜ Cᴏrrᴇᴄᴛ Sᴩᴇʟʟɪɴɢ Aɴᴅ I Wɪʟʟ Sᴇɴᴅ Tʜᴇ Fɪʟᴇ Lɪɴᴋ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nCᴏʀʀᴇᴄᴛ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Mᴇᴛʜᴏᴅ 👉 /movies\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nCᴏʀʀᴇᴄᴛ Sᴇʀɪᴇs Rᴇǫᴜᴇsᴛɪɴɢ Mᴇᴛʜᴏᴅ 👉 /series")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")
