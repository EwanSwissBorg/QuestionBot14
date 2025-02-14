from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
import dotenv
import os   
import re  # Assurez-vous d'importer le module re pour les expressions régulières

dotenv.load_dotenv()

# Define conversation states
(
    PROJECT_NAME,
    TOKEN_TICKER,
    PROJECT_DESCRIPTION,
    MAIN_PROBLEM,
    SOLUTION,
    TECHNOLOGY_WORK,
    TARGET_MARKET,
    GROWTH_STRATEGY,
    COMPETITORS,
    KEY_DIFFERENTIATORS,
) = range(10)

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
        "What's your token ticker? Format: $XXXXX (maximum 5 long)\n"
        " • Examples: $BTC, $SOL, $MATES\n"
        " • Note: Only UPPERCASE letters A-Z are allowed after the $ symbol"
    )
    return TOKEN_TICKER  # Retourner l'état pour attendre la réponse de l'utilisateur

def is_valid_ticker(ticker: str) -> bool:
    """Vérifie si le ticker est valide selon les critères spécifiés."""
    pattern = r'^\$[A-Z]{1,5}$'  # Format: $XXXXX avec 1 à 5 lettres majuscules
    return re.match(pattern, ticker) is not None

async def handle_token_ticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ticker = update.message.text  # Récupérer le ticker de l'utilisateur
    if is_valid_ticker(ticker):  # Vérifier si le ticker est valide
        context.user_data['token_ticker'] = ticker  # Enregistrer le ticker du token
        return await project_description(update, context)  # Appeler le résumé après avoir collecté toutes les informations
    else:
        await update.message.reply_text(
            "Invalid ticker format. Please try again.\n"
            "Format: $XXXXX (maximum 5 long)\n"
            " • Examples: $BTC, $SOL, $MATES\n"
            " • Note: Only UPPERCASE letters A-Z are allowed after the $ symbol"
        )
        return TOKEN_TICKER  # Rester dans l'état TOKEN_TICKER pour redemander le ticker

async def project_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your project description? 📝"
    )
    return PROJECT_DESCRIPTION

async def handle_project_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['project_description'] = update.message.text
    return await main_problem(update, context)

async def main_problem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your main problem? 🤔"
    )
    return MAIN_PROBLEM

async def handle_main_problem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['main_problem'] = update.message.text
    return await solution(update, context)

async def solution(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your solution? 💡"
    )
    return SOLUTION

async def handle_solution(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['solution'] = update.message.text
    return await technology_work(update, context)

async def technology_work(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your technology work? 💻"
    )
    return TECHNOLOGY_WORK

async def handle_technology_work(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['technology_work'] = update.message.text
    return await target_market(update, context)

async def target_market(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your target market? 🎯"
    )
    return TARGET_MARKET

async def handle_target_market(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['target_market'] = update.message.text
    return await growth_strategy(update, context)   

async def growth_strategy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your growth strategy? 🚀"
    )
    return GROWTH_STRATEGY

async def handle_growth_strategy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['growth_strategy'] = update.message.text
    return await competitors(update, context)

async def competitors(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your competitors? 🤖"
    )
    return COMPETITORS

async def handle_competitors(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['competitors'] = update.message.text
    return await key_differentiators(update, context)

async def key_differentiators(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your key differentiators? 🔑"
    )
    return KEY_DIFFERENTIATORS

async def handle_key_differentiators(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['key_differentiators'] = update.message.text
    return await summary(update, context)

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Display a summary of all collected information"""
    user_data = context.user_data
    
    summary_text = "📋 Project Summary:\n\n"
    
    if 'project_name' in user_data:
        summary_text += f"🏷️ Project Name: {user_data['project_name']}\n"
    
    if 'token_ticker' in user_data:
        summary_text += f"💰 Token Ticker: {user_data['token_ticker']}\n"
    
    if 'project_description' in user_data:
        summary_text += f"📝 Project Description: {user_data['project_description']}\n"
    
    if 'main_problem' in user_data:
        summary_text += f"🤔 Main Problem: {user_data['main_problem']}\n"
    
    if 'solution' in user_data:
        summary_text += f"💡 Solution: {user_data['solution']}\n"
    
    if 'technology_work' in user_data:
        summary_text += f"💻 Technology Work: {user_data['technology_work']}\n"
    
    if 'target_market' in user_data:
        summary_text += f"🎯 Target Market: {user_data['target_market']}\n"
    
    if 'growth_strategy' in user_data:
        summary_text += f"🚀 Growth Strategy: {user_data['growth_strategy']}\n"
    
    if 'competitors' in user_data:
        summary_text += f"🤖 Competitors: {user_data['competitors']}\n"
    
    if 'key_differentiators' in user_data:
        summary_text += f"🔑 Key Differentiators: {user_data['key_differentiators']}\n"
    
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
            PROJECT_DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_project_description)],
            MAIN_PROBLEM: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_main_problem)],
            SOLUTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_solution)],
            TECHNOLOGY_WORK: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_technology_work)],
            TARGET_MARKET: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_target_market)],
            GROWTH_STRATEGY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_growth_strategy)],
            COMPETITORS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_competitors)],
            KEY_DIFFERENTIATORS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_key_differentiators)],
        },
        fallbacks=[],
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("summary", summary))
    
    app.run_polling()

if __name__ == '__main__':
    main()