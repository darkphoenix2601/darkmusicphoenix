from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import filters


@Client.on_message(filters.command('start'))
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
https://telegra.ph/file/1bac7eac76a16f64d8afb.jpg
𝕴 𝖑𝖊𝖙 𝖞𝖔𝖚 𝖕𝖑𝖆𝖞 𝖒𝖚𝖘𝖎𝖈 𝖎𝖓 𝖞𝖔𝖚𝖗 𝖌𝖗𝖔𝖚𝖕'𝖘 𝖛𝖔𝖎𝖈𝖊 𝖈𝖍𝖆𝖙 😉
•𝕮𝖚𝖗𝖗𝖊𝖓𝖙𝖑𝖞 𝕴 𝖆𝖒 𝖚𝖓𝖉𝖊𝖗 𝖆 𝖕𝖗𝖎𝖛𝖆𝖙𝖊 𝖛𝖈 𝖒𝖚𝖘𝖎𝖈 𝖕𝖑𝖆𝖞𝖊𝖗 ⏩
•𝕿𝖔 𝖆𝖉𝖉 𝖒𝖊 𝖙𝖆𝖐𝖊 𝖕𝖊𝖗𝖒𝖎𝖘𝖘𝖎𝖔𝖓 𝖋𝖗𝖔𝖒 [𝕺𝖜𝖓𝖊𝖗](https://t.me/akshi_s_ashu)
•𝕿ԋҽ ƈσɱɱαɳԃʂ 𝕴 ƈυɾɾҽɳƚʅყ ʂυρρσɾƚ αɾҽ:
⚜️ /play-Tσ ʂҽαɾƈԋ ʂσɳɠ ϝɾσɱ ყσυƚυႦҽ αɳԃ ρʅαყ ԃιɾҽƈƚʅყ
⚜️/pause - Pαυʂҽ Vσιƈҽ Cԋαƚ Mυʂιƈ.
⚜️ /resume - Rҽʂυɱҽ Vσιƈҽ Cԋαƚ Mυʂιƈ.
⚜️ /skip - Sƙιρʂ ƚԋҽ ƈυɾɾҽɳƚ Mυʂιƈ Pʅαყιɳɠ Iɳ Vσιƈҽ Cԋαƚ.
⚜️ /stop - Cʅҽαɾʂ Tԋҽ Qυҽυҽ αʂ ɯҽʅʅ αʂ ҽɳԃʂ Vσιƈҽ Cԋαƚ Mυʂιƈ.
⚜️ /song (ʂσɳɠ ɳαɱҽ) - Tσ ʂҽαɾƈԋ ʂσɳɠ αɳԃ ʂҽɳԃ ʂσɳɠ ԃιɾҽƈƚʅყ.
⚜️ /fplay (ɾҽρʅყ ƚσ αυԃισ σɾ ʅιɳƙ) - Pʅαყʂ ƚԋҽ ɾҽρʅιҽԃ αυԃισ ϝιʅҽ σɾ YσυTυႦҽ ʋιԃҽσ ƚԋɾσυɠԋ ʅιɳƙ. 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group 💬", url="https://t.me/phoenix_music_suport"
                    ),
                    InlineKeyboardButton(
                        "Channel 📣", url="https://t.me/phoenix_music_new"
                    ),
                    InlineKeyboardButton(
                        "Owner 👑", url="https://t.me/akshi_s_ashu"
                    ),
                ], 
                [
                    InlineKeyboardButton(
                        "About 🔥", url="https://telegra.ph/Doreamon-Bot-09-10"   
                    )
                ]
            ]
        )
    )

from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os

# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.command(['song']))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply(f"**🔎 Searching For** `{query}`")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[MÚSÎC ẞø†]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**Found Literary Noting. Please Try Another Song or Use Correct Spelling!**')
            return
    except Exception as e:
        m.edit(
            "**Enter Song Name with Command!**"
        )
        print(str(e))
        return
    m.edit(f"🔥 **Uploading Song**  `{query}` !")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🏷 <b>Title:</b> <a href="{link}">{title}</a>\n⏳ <b>Duration:</b> <code>{duration}</code>\n👀 <b>Views:</b> <code>{views}</code>\n'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
        message.delete()
    except Exception as e:
        m.edit('**An Error Occured. Please Report This To [SUPORT GROUP](https://t.me/phoenix_music_suport) !!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
