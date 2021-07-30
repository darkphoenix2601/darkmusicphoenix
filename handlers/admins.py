from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text(f"**{BN} :-** 🙄 Nothing is playing My boss is saying!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🤐 Paused by MR. RØBØT!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing by MR. RØBØT'
    ):
        await message.reply_text(f"**{BN} :-** 🙄 Nothing is paused told by @backup_pista123!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🥳 Resumed by MR. RØBØT!")


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** 🙄 Nothing is streaming my boss!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(f"**{BN} :-** ❌ Stopped streaming Dear!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** 🙄 Nothing is playing to skip hehe don't make fools!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file_path"]
            )

        await message.reply_text(f"**{BN} :-** 😬 Skipped the current song fools!")
        
        
@Client.on_message(command("current") & other_filters)
@errors
@authorized_users_only
async def show_current_playing_time(client, m: Message):

    start_time = mp.start_time

    playlist = mp.playlist

    if not start_time:

        reply = await m.reply_text(f"{emoji.PLAY_BUTTON} unknown")

        await _delay_delete_messages((reply, m), DELETE_DELAY)

        return

    utcnow = datetime.utcnow().replace(microsecond=0)

    if mp.msg.get('current') is not None:

        await mp.msg['current'].delete()

    mp.msg['current'] = await playlist[0].reply_text(

        f"{emoji.PLAY_BUTTON}  {utcnow - start_time} / "

        f"{timedelta(seconds=playlist[0].audio.duration)}",

        disable_notification=True

    )

    await m.delete()

