import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8760734535:AAFvtYmVE5FRFeLS8y6_ixT_2bm_YInKH8k"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎰 Welcome to Cronos Gangsters!\n\n"
        "The baddest DEX on Cronos.\n\n"
        "🔗 Trade now: https://kingautomotive189a-spec.github.io/-cronosgangstersb/"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 $GANG price coming soon!")

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 Cronos Gangsters Links:\n\n"
        "DEX: https://kingautomotive189a-spec.github.io/-cronosgangstersb/\n"
        "Twitter: https://twitter.com/AhmadOm93837106\n"
        "Contract: 0x23E1D61FbA6Df8F61805059A5f52eFbb1f5613c7"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("links", links))
    app.run_polling()
