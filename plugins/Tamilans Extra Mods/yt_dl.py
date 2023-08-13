from pyrogram import Client, filters
from pyrogram.types import Message
import os
import requests
import wget
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

app = Client("6075536616:AAHhCHPr5fmqhCdxVK2CUEciOxzMi7gFUs8")

def get_text(message: Message) -> str:
    return " ".join(message.command[1:]) if len(message.command) > 1 else ""

@app.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    user_name = message.from_user.first_name
    query = get_text(message)
    m = await message.reply(f"Searching for '{query}'...")

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"

        ydl_opts = {
            "format": "bestaudio[ext=m4a]",
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        caption = f"Downloaded from [YouTube]({link})"
        await message.reply_audio(
            audio_file,
            caption=caption,
            title=info_dict.get("title", "")[:40],
            performer="[Harsha]",
        )
        
        await m.delete()
        os.remove(audio_file)
    except Exception as e:
        await m.edit("Failed to process the request.")
        print(str(e))

@app.on_message(filters.command(["video", "mp4"]) & filters.private)
async def vsong(client, message):
    urlissed = get_text(message)
    m = await message.reply(f"Finding video for '{urlissed}'...")

    try:
        search = SearchVideos(urlissed, offset=1, mode="dict", max_results=1)
        mi = search.result()
        mio = mi["search_result"]
        mo = mio[0]["link"]
        kekme = f"https://img.youtube.com/vi/{mio[0]['id']}/hqdefault.jpg"
        thumb_file = f"thumb{mio[0]['id']}.jpg"
        wget.download(kekme, thumb_file)

        opts = {
            "format": "best",
            "outtmpl": f"{mio[0]['id']}.mp4",
        }
        with YoutubeDL(opts) as ydl:
            ydl.download([mo])

        caption = f"Downloaded from [YouTube]({mo})"
        await message.reply_video(
            f"{mio[0]['id']}.mp4",
            caption=caption,
        )

        await m.delete()
        os.remove(f"{mio[0]['id']}.mp4")
        os.remove(thumb_file)
    except Exception as e:
        await m.edit("Failed to process the request.")
        print(str(e))

app.run()
