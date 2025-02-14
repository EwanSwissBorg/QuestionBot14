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
    TOTAL_SUPPLY,
    INITIAL_SUPPLY,
    TARGET_FDV,
    LIQUIDITY_DISTRIBUTION
) = range(14)

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
    return await total_supply(update, context)

async def total_supply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your total supply? 💰"
    )
    return TOTAL_SUPPLY

def is_valid_supply(supply: str) -> bool:
    """Vérifie si la supply est un chiffre"""
    return supply.isdigit()

async def handle_total_supply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    supply = update.message.text  # Récupérer la supply de l'utilisateur
    if is_valid_supply(supply):  # Vérifier si la supply est valide
        context.user_data['total_supply'] = supply  # Enregistrer la supply
        return await initial_supply(update, context)  # Appeler le résumé après avoir collecté toutes les informations
    else:
        await update.message.reply_text(
            "Invalid supply format. Please try again.\n"
            "Format: chiffres\n"
        )
        return TOTAL_SUPPLY  # Rester dans l'état TOTAL_SUPPLY pour redemander la supply

async def initial_supply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your initial supply? 💰"
    )
    return INITIAL_SUPPLY

def is_valid_initial_supply(supply: str, total_supply: str) -> bool:
    """Vérifie si la supply initiale est un chiffre inférieur à la supply totale"""
    return supply.isdigit() and int(supply) < int(total_supply)

async def handle_initial_supply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    supply = update.message.text  # Récupérer la supply initiale de l'utilisateur
    if is_valid_initial_supply(supply, context.user_data['total_supply']):  # Vérifier si la supply initiale est valide
        context.user_data['initial_supply'] = supply  # Enregistrer la supply initiale
        return await target_fdv(update, context)  # Appeler le résumé après avoir collecté toutes les informations
    else:
        await update.message.reply_text(
            "Invalid initial supply format. Please try again.\n"
            "Format: chiffres\n"
            "Initial supply must be less than total supply\n"
        )
        return INITIAL_SUPPLY  # Rester dans l'état INITIAL_SUPPLY pour redemander la supply initiale

async def target_fdv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "What's your target FDV? 💰"
    )
    return TARGET_FDV

def is_valid_target_fdv(fdv: str) -> bool:
    """Vérifie si le FDV est un chiffre"""
    return fdv.isdigit()    

async def handle_target_fdv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    fdv = update.message.text  # Récupérer le FDV de l'utilisateur
    if is_valid_target_fdv(fdv):  # Vérifier si le FDV est valide
        context.user_data['target_fdv'] = fdv  # Enregistrer le FDV
        return await liquidity_distribution(update, context)  # Appeler le résumé après avoir collecté toutes les informations
    else:
        await update.message.reply_text(
            "Invalid target FDV format. Please try again.\n"
            "Format: chiffres\n"
        )
        return TARGET_FDV  # Rester dans l'état TARGET_FDV pour redemander le FDV

async def liquidity_distribution(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Please list each category with its percentage using this format: \"XX% - Category Name\".\n"
        "Don't forget to include the percent for your initial liquidity pool that will be burned!\n\n"
        "Example:\n"
        "15% - Team\n"
        "69% - Community\n"
        "1% - Advisors & Angels\n"
        "10% - Marketing\n"
        "5% - LBP\n\n"
        "Total need to be: 100%"
    )
    return LIQUIDITY_DISTRIBUTION  # Retourner l'état pour attendre la réponse de l'utilisateur


def is_valid_distribution(distribution: str) -> bool:
    """Vérifie si la distribution est valide et totalise 100%."""
    lines = distribution.strip().split('\n')
    total_percentage = 0
    for line in lines:
        parts = line.split('-')
        if len(parts) != 2:
            return False  # Format incorrect
        try:
            percentage = int(parts[0].strip().replace('%', ''))
            total_percentage += percentage
        except ValueError:
            return False  # Non numérique
    return total_percentage == 100  # Vérifier si le total est 100%


async def handle_liquidity_distribution(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    distribution = update.message.text  # Récupérer la réponse de l'utilisateur
    if is_valid_distribution(distribution):  # Vérifier si le format est valide
        context.user_data['liquidity_distribution'] = distribution  # Enregistrer la distribution
        await update.message.reply_text("Thank you for providing the liquidity distribution details! Let's summarize your project.")
        return await summary(update, context)  # Appeler le résumé après avoir collecté toutes les informations
    else:
        await update.message.reply_text(
            "Invalid format. Please ensure that the total percentage is 100% and follow the format: \"XX% - Category Name\"."
        )
        return LIQUIDITY_DISTRIBUTION  # Rester dans l'état LIQUIDITY_DISTRIBUTION pour redemander la distribution


async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = context.user_data
    summary_text = "📋 Project Summary:\n\n"
    
    summary_text += f"Project Name: {user_data['project_name']}\n"
    summary_text += f"Token Ticker: {user_data['token_ticker']}\n"
    summary_text += f"Project Description: {user_data['project_description']}\n"
    summary_text += f"Main Problem: {user_data['main_problem']}\n"
    summary_text += f"Solution: {user_data['solution']}\n"
    summary_text += f"Technology Work: {user_data['technology_work']}\n"
    summary_text += f"Target Market: {user_data['target_market']}\n"
    summary_text += f"Growth Strategy: {user_data['growth_strategy']}\n"
    summary_text += f"Competitors: {user_data['competitors']}\n"
    summary_text += f"Key Differentiators: {user_data['key_differentiators']}\n"
    summary_text += f"Total Supply: {user_data['total_supply']}\n"
    summary_text += f"Initial Supply: {user_data['initial_supply']}\n"
    summary_text += f"Target FDV: {user_data['target_fdv']}\n"
    summary_text += f"Liquidity Distribution: {user_data['liquidity_distribution']}\n"
    
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
            TOTAL_SUPPLY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_total_supply)],
            INITIAL_SUPPLY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_initial_supply)],
            TARGET_FDV: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_target_fdv)],
            LIQUIDITY_DISTRIBUTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_liquidity_distribution)],
        },
        fallbacks=[],
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("summary", summary))
    
    app.run_polling()

if __name__ == '__main__':
    main()