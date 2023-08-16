from pyrogram import filters, Client
from pyrogram.types import Message
import asyncio
import os
import requests
import wget
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

# Your bot initialization goes here (if applicable)

@Client.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    user_name = message.from_user.first_name
    query = ' '.join(message.command[1:])
    print(query)
    m = await message.reply(f"**Searching for your song...!\n{query}**")

    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        performer = f"[Harsha™]"
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
    except Exception as e:
        print(str(e))
        return await m.edit("**Nothing Found (Please check your song spelling or link)**")

    await m.edit("**Downloading your song...!**")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        cap = "**BY ›› [Harsha](http://t.me/CSadmin69_bot)**"
        dur_arr = duration.split(':')
        dur = sum(int(dur_arr[i]) * 60 ** i for i in range(len(dur_arr) - 1, -1, -1))
        await message.reply_audio(
            audio_file,
            caption=cap,
            quote=False,
            title=title,
            duration=dur,
            performer=performer,
            thumb=thumb_name
        )
        await m.delete()
    except Exception as e:
        await m.edit("**🚫 Error 🚫**")
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None

@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)
    pablo = await client.send_message(message.chat.id, f"**Finding Your Video** `{urlissed}`")
    if not urlissed:
        return await pablo.edit("Invalid Command Syntax!")

    search = SearchVideos(urlissed, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
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
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        return await pablo.edit_text(f"**Download Failed Please Try Again!** \n**Error :** `{str(e)}`")

    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""**Title:** [{thum}]({mo})\n**Requested by:** {message.from_user.mention}"""

    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        reply_to_message_id=message.id
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
