async def effect(message):
    orig_text = message
    msg = await bot.send_message(message.chat.id, 'I')
    sl(0.05)
    tbp = orig_text[:1]
    for x in orig_text[1:]:
        await bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f'{tbp}|')
        sl(0.05)
        tbp += x
        await bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=tbp)
