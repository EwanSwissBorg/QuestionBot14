from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
import dotenv
import os   

dotenv.load_dotenv()

# Define conversation states
(
    PROJECT_NAME,
    TOKEN_TICKER,
) = range(2)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Gm! I'm the BorgPad Curator Bot. I'll help you create a professional data room "
        "for your project. I'll ask you a series of questions to gather all the necessary "
        "information. Let's start with your basic Project Information.\n\n"
    )
    return await project_name(update, context)

async def project_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What is your project name? 🏷️"
    )
    return PROJECT_NAME  # Retourner l'état pour attendre la réponse de l'utilisateur

async def handle_project_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['project_name'] = update.message.text  # Enregistrer le nom du projet
    return await token_ticker(update, context)  # Passer à l'étape suivante

async def token_ticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What is the ticker of the token you're raising funds for? 💰"
    )
    return TOKEN_TICKER  # Retourner l'état pour attendre la réponse de l'utilisateur

async def handle_token_ticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['token_ticker'] = update.message.text  # Enregistrer le ticker du token
    return await summary(update, context)  # Appeler le résumé après avoir collecté toutes les informations

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Display a summary of all collected information"""
    user_data = context.user_data
    
    summary_text = "📋 Project Summary:\n\n"
    
    if 'project_name' in user_data:
        summary_text += f"🏷️ Project Name: {user_data['project_name']}\n"
    
    if 'token_ticker' in user_data:
        summary_text += f"💰 Token Ticker: {user_data['token_ticker']}\n"
    
    if not any(key in user_data for key in ['project_name', 'token_ticker']):
        summary_text = "No information collected yet. Please start the conversation with /start"
    
    await update.message.reply_text(summary_text)

def main():
    print("Starting bot...")
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Create conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PROJECT_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_project_name)],
            TOKEN_TICKER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_token_ticker)],
        },
        fallbacks=[],
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("summary", summary))
    
    app.run_polling()

if __name__ == '__main__':
    main()