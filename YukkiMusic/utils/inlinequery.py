#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause Stream",
            description=f"Jeda pemutaran saat ini pada obrolan grup.",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume Stream",
            description=f"Melanjutkan pemutaran saat ini pada obrolan grup.",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Mute Stream",
            description=f"Membisukan pemutaran saat ini pada obrolan grup.",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Unmute Stream",
            description=f"Membunyikan pemutaran saat ini pada obrolan grup.",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="Skip Stream",
            description=f"Lewati ke trek berikutnya. | Untuk nomor trek tertentu: /skip [number] ",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End Stream",
            description="Menghentikan pemutaran yang sedang berlangsung pada obrolan grup..",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Shuffle Stream",
            description="Acak daftar trek yang antri.",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Seek Stream",
            description="Cari aliran yang sedang berlangsung dengan durasi tertentu.",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="Loop Stream",
            description="Putar musik yang sedang diputar. | Usage: /loop [enable|disable]",
            thumb_url="https://graph.org/file/c012d72d5a73c36df493a.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
