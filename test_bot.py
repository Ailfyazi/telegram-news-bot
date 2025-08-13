#!/usr/bin/env python3
"""
تست سریع ربات - برای بررسی اینکه همه چی درست کار میکنه
"""

import asyncio
from telegram import Bot

# اطلاعات ربات شما
BOT_TOKEN = "8425355916:AAGc6-zek0min7lTD4qg4OHly5pdTw15cZI"
CHANNEL_ID = "@ne77i"

async def test_bot():
    """تست ربات"""
    try:
        print("🤖 شروع تست ربات...")
        
        # ساخت ربات
        bot = Bot(token=BOT_TOKEN)
        
        # تست 1: بررسی ربات
        print("1️⃣ بررسی ربات...")
        me = await bot.get_me()
        print(f"✅ ربات فعال است: @{me.username}")
        
        # تست 2: بررسی دسترسی کانال
        print("2️⃣ بررسی دسترسی کانال...")
        chat = await bot.get_chat(CHANNEL_ID)
        print(f"✅ کانال پیدا شد: {chat.title}")
        
        # تست 3: ارسال پیام تست
        print("3️⃣ ارسال پیام تست...")
        test_message = """
🧪 **پیام تست ربات خبری**

سلام! این یک پیام تست است.
ربات خبری شما آماده کار است! 🎉

📅 زمان تست: اکنون
🤖 ربات: فعال
📢 کانال: متصل

➖➖➖➖➖➖➖➖➖➖

*این پیام از سیستم خودکار ارسال شده*
        """.strip()
        
        message = await bot.send_message(
            chat_id=CHANNEL_ID,
            text=test_message,
            parse_mode='Markdown'
        )
        
        print(f"✅ پیام ارسال شد: ID {message.message_id}")
        print(f"🔗 لینک کانال: https://t.me/ne77i")
        
        print("\n🎉 تست کامل شد! همه چی درست کار میکنه")
        
    except Exception as e:
        print(f"❌ خطا در تست: {e}")
        print("\n🔍 بررسی کنید:")
        print("- آیا ربات ادمین کانال هست?")
        print("- آیا دسترسی 'Post Messages' فعال هست?")
        print("- آیا توکن ربات درست هست?")

if __name__ == "__main__":
    asyncio.run(test_bot())
