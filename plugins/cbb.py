from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"<b>Premium Benefits & Perks\nDirect Channel Links, No Ad Links\nSpecial Access In Events\n\nPricing Rates\n3 Months - INR 349\n6 Months - INR 579\n12 Month - INR 1049\n\nWant To Buy?\nPay Using Crypto\nSend Screenshot to @Amex_Fushiguro\n\nWe Have Limited Seats For Premium Users</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Amex_Fushiguro"),
                        InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Ecchi_Network")
                    ],
                    [
                        InlineKeyboardButton("H-Aɴɪᴍᴇ", url="https://t.me/+L1hVwV950xUxNDcx"),
                        InlineKeyboardButton("ᴊᴀᴠ ʟɪᴠᴇ ᴀᴄᴛɪᴏɴ", url="https://t.me/+b0mMjTTqCphiZmY1")
                    ],
                    [
                        InlineKeyboardButton("ʜᴀɴɪᴍᴇ&ʜ*ɴᴛᴀɪ", url="https://t.me/+L1hVwV950xUxNDcx"),
                        InlineKeyboardButton("🔒ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass