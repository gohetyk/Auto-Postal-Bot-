
import asyncio
from pyrogram import Client, filters

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
                await app.send_message(group_id, "🔁 پیام تستی هر ۳۰ ثانیه")
            except Exception as e:
                print(f"خطا در ارسال به {group_id}: {e}")
        await asyncio.sleep(30)  # فقط 30 ثانیه برای تست

async def main():
    await app.start()
    print("🤖 ربات تستی فعال شد (هر 30 ثانیه پیام می‌فرسته)")
    asyncio.create_task(auto_send())
    while True:
        await asyncio.sleep(60)

import asyncio
asyncio.run(main())
