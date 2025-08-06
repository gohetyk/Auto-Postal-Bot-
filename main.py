
import asyncio
from pyrogram import Client, filters
from pyrogram.idle import idle

API_ID = 26587770
API_HASH = "5db34c3d45b6d91aa18a85f13205a8c6"
BOT_TOKEN = "8234371535:AAGq5CrO1faPEpLbsOTwB5cu7LEr4VR_1QM"

app = Client("autobot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

groups = set()

@app.on_message(filters.group)
async def save_groups(client, message):
    groups.add(message.chat.id)

async def auto_send():
    while True:
        for group_id in groups:
            try:
                await app.send_message(group_id, "📢 پیام خودکار از طرف ربات!")
            except Exception as e:
                print(f"خطا در ارسال به {group_id}: {e}")
        await asyncio.sleep(3600)

async def main():
    await app.start()
    print("🤖 ربات فعال شد")
    asyncio.create_task(auto_send())
    await idle()
    await app.stop()

asyncio.run(main())
