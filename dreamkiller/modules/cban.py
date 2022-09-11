import html
from typing import Optional
from telegram import (
    ParseMode,
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import CallbackContext, Filters, CommandHandler, run_async, CallbackQueryHandler
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html

from dreamkiller import (
    DEV_USERS,
    LOGGER,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
    dispatcher,
)
import dreamkiller.modules.sql.users_sql as sql
from dreamkiller.modules.disable import DisableAbleCommandHandler
from dreamkiller.modules.helper_funcs.chat_status import (
    user_admin_no_reply,
    bot_admin,
    can_restrict,
    connection_status,
    is_user_admin,
    is_user_ban_protected,
    is_user_in_chat,
    user_admin,
    user_can_ban,
    can_delete,
)
from dreamkiller.modules.helper_funcs.extraction import extract_user_and_text
from dreamkiller.modules.helper_funcs.string_handling import extract_time
from dreamkiller.modules.log_channel import gloggable, loggable
from dreamkiller.modules.helper_funcs.anonymous import user_admin, AdminPerms


UNBAN_IMG= "https://telegra.ph/file/b9af0c3c1a6cc8da18459.mp4"
BAN_IMG= "https://telegra.ph/file/023c328412eb339546230.mp4"

@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin(AdminPerms.CAN_RESTRICT_MEMBERS)
@loggable
def cban(update: Update, context: CallbackContext) -> Optional[str]: 
    chat = update.effective_chat  
    user = update.effective_user 
    message = update.effective_message 
    args = context.args
    bot = context.bot
    log_message = ""
    reason = ""
    if message.reply_to_message and message.reply_to_message.sender_chat:
        r = bot._request.post(bot.base_url + '/banChatSenderChat', {
            'sender_chat_id': message.reply_to_message.sender_chat.id,
            'chat_id': chat.id
        },
                              )
        if r:
            message.reply_video(BAN_IMG,caption="Channel {} was banned successfully from {}".format(
                html.escape(message.reply_to_message.sender_chat.title),
                html.escape(chat.title)
            ),
                parse_mode="html"
            )
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#BANNED\n"
                f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
                f"<b>Channel:</b> {mention_html(channel.id, html.escape(chat.title))} ({message.reply_to_message.sender_chat.id})"
            )
        else:
            message.reply_text("Failed to ban channel")
        return

    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise

        message.reply_text("Can't seem to find this person.")
        return log_message
    if user_id == context.bot.id:
        message.reply_text("Oh yeah, ban myself, noob!")
        return log_message

    if is_user_ban_protected(update, user_id, member) and user not in DEV_USERS:
        if user_id == OWNER_ID:
            message.reply_text("I'd never ban my owner.")
        elif user_id in DEV_USERS:
            message.reply_text("I can't act against our own.")
        elif user_id in DRAGONS:
            message.reply_text("My sudos are ban immune")
        elif user_id in DEMONS:
            message.reply_text("My support users are ban immune")
        elif user_id in TIGERS:
            message.reply_text("Sorry, He is Tiger Level Disaster.")
        elif user_id in WOLVES:
            message.reply_text("Neptunians are ban immune!")
        else:
            message.reply_text("This user has immunity and cannot be banned.")
        return log_message
    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#BANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(member.user.id, member.user.first_name)}"
    )
    if reason:
        log += "\n<b>Reason:</b> {}".format(reason)

    try:
        chat.ban_member(user_id)
        # context.bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        context.bot.sendMessage(
            chat.id,
            "{} was banned by {} in <b>{}</b>\n<b>Reason</b>: <code>{}</code>".format(
                mention_html(member.user.id, member.user.first_name), mention_html(user.id, user.first_name),
                message.chat.title, reason
            ),
            parse_mode=ParseMode.HTML,
        )
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            message.reply_text("Banned!", quote=False)
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception(
                "ERROR banning user %s in chat %s (%s) due to %s",
                user_id,
                chat.title,
                chat.id,
                excp.message,
            )
            message.reply_text("Well damn, I can't ban that user.")

    return ""
  
@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin(AdminPerms.CAN_RESTRICT_MEMBERS)
@loggable
def uncban(update: Update, context: CallbackContext) -> Optional[str]:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    log_message = ""
    bot, args = context.bot, context.args
    if message.reply_to_message and message.reply_to_message.sender_chat:
        r = bot.unban_chat_sender_chat(chat_id=chat.id, sender_chat_id=message.reply_to_message.sender_chat.id)
        if r:
            message.reply_video(UNBAN_IMG,caption="Channel {} was unbanned successfully from {}".format(
                html.escape(message.reply_to_message.sender_chat.title),
                html.escape(chat.title)
            ),
                parse_mode="html"
            )
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#UNCBANNED\n"
                f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
                f"<b>Channel:</b> {html.escape(message.reply_to_message.sender_chat.title)} ({message.reply_to_message.sender_chat.id})"
            )
        else:
            message.reply_text("Failed to unban channel")
        return
    user_id, reason = extract_user_and_text(message, args)
    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != 'User not found':
            raise
        message.reply_text("I can't seem to find this user.")
        return log_message
    if user_id == bot.id:
        message.reply_text("How would I unban myself if I wasn't here...?")
        return log_message

    if is_user_in_chat(chat, user_id):
        message.reply_text("Isn't this person already here??")
        return log_message

    chat.unban_member(user_id)
    bot.sendMessage(
        chat.id,
        "{} was unbanned by {} in <b>{}</b>\n<b>Reason</b>: <code>{}</code>".format(
            mention_html(member.user.id, member.user.first_name), mention_html(user.id, user.first_name),
            message.chat.title, reason
        ),
        parse_mode=ParseMode.HTML,
    )

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNCBANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(member.user.id, member.user.first_name)}"
    )
    if reason:
        log += f"\n<b>Reason:</b> {reason}"

    return log
    
    
UNCBAN_HANDLER = CommandHandler(["channelunban", "uncban"], uncban)
CBAN_HANDLER = CommandHandler(["cban", "channelban"], cban)
    
dispatcher.add_handler(UNCBAN_HANDLER)
dispatcher.add_handler(CBAN_HANDLER)
