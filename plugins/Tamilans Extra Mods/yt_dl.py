import os, requests, asyncio, math, time, wget
from pyrogram import filters, Client
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

@Client.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    query = ' '.join(message.command[1:])
    m = await message.reply(f"**Searching for your song...!\n{query}**")

    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(query, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        caption = "**Downloaded by [YourBotName](t.me/YourBotUsername)**"
        duration = info_dict.get("duration", 0)
        performer = "Artist Name"  # Replace with the actual artist name

        await message.reply_audio(
            audio_file,
            caption=caption,
            quote=False,
            title=info_dict.get("title", "Unknown Title"),
            duration=duration,
            performer=performer
        )

        await m.delete()
    except Exception as e:
        await m.edit("**🚫 ERROR 🚫**")
        print(e)
    try:
        os.remove(audio_file)
    except Exception as e:
        print(e)

@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    query = ' '.join(message.command[1:])
    pablo = await message.reply(f"**Finding your video** `{query}`")

    search = SearchVideos(query, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"

    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }

    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
    except Exception as e:
        return await pablo.edit_text(f"**Download Failed**\n**Error:** `{str(e)}`")

    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Title:** [{thum}]({mo})\n**Requested By:** {message.from_user.mention}"

    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=kekme,
        caption=capy,
        supports_streaming=True,
        reply_to_message_id=message.message_id
    )
    await pablo.delete()
