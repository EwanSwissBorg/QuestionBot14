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
    LIQUIDITY_DISTRIBUTION,
    VESTING_SCHEDULE,
    PROJECT_ROADMAP,
    TEAM_INFORMATION,
    ESSENTIAL_LINKS,
) = range(18)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message:  # Check if update.message is not None
        await update.message.reply_text(
            "Gm! I'm the BorgPad Curator Bot. I'll help you create a professional data room "
            "for your project. I'll ask you a series of questions to gather all the necessary "
            "information. Let's start with your basic Project Information.\n\n"
        )
    else:
        # Handle the case where update.message is None
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Gm! I'm the BorgPad Curator Bot. I'll help you create a professional data room for your project. Let's start with your basic Project Information.")
    
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
        return await vesting_schedule(update, context)  # Appeler le résumé après avoir collecté toutes les informations
    else:
        await update.message.reply_text(
            "Invalid format. Please ensure that the total percentage is 100% and follow the format: \"XX% - Category Name\"."
        )
        return LIQUIDITY_DISTRIBUTION  # Rester dans l'état LIQUIDITY_DISTRIBUTION pour redemander la distribution

async def vesting_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Vesting Schedule\n"
        "For each category above, specify:\n"
        " • Cliff period (locked period before first unlock)\n"
        " • Initial unlock percentage (TGE unlock)\n"
        " • Vesting duration and details\n\n"
        "Example:\n"
        "Team (20%):\n"
        " • - 3 month cliff\n"
        " • - No initial unlock\n"
        " • - 12 months linear vesting\n\n"
        "Community (69%):\n"
        " • - 0 cliff\n"
        " • - 10% unlock at TGE\n"
        " • - 6 months linear vesting\n\n"
        "Let's start with the categories you provided earlier."
    )
    return VESTING_SCHEDULE  # Retourner l'état pour attendre la réponse de l'utilisateur

def is_valid_vesting_schedule(schedule: str) -> bool:
    """Vérifie si le calendrier de vesting est au format correct."""
    lines = schedule.strip().split('\n')
    if len(lines) < 3:  # S'assurer qu'il y a au moins 3 lignes
        return False
    for line in lines:
        if not line.strip():  # Vérifier les lignes vides
            return False
    return True  # Si toutes les lignes sont valides

async def handle_vesting_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    schedule = update.message.text  # Récupérer le calendrier de vesting de l'utilisateur
    if is_valid_vesting_schedule(schedule):  # Vérifier si le calendrier de vesting est valide
        context.user_data['vesting_schedule'] = schedule  # Enregistrer le calendrier de vesting
        return await project_roadmap(update, context)  # Appeler le résumé après avoir collecté toutes les informations
    else:
        await update.message.reply_text(
            "Invalid format. Please ensure that the vesting schedule is in the correct format."
        )
        return VESTING_SCHEDULE  # Rester dans l'état VESTING_SCHEDULE pour redemander le calendrier de vesting

async def project_roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Project Roadmap & Team\n"
        "Please outline your quarterly roadmap for the next 6-12 months. For each of the two quarters, list 2-3 key objectives in bullet points.\n\n"
        "Example:\n"
        "Q1:\n"
        " • Launch the MVP (Minimum Viable Product)\n"
        " • Acquire first 100 users\n"
        "\n"
        "Q2:\n"
        " • Expand marketing efforts to increase user base by 50%\n"
        " • Implement user feedback to improve product features"
    )
    return PROJECT_ROADMAP  # Return the state to wait for the user's response

   
def is_valid_roadmap(roadmap: str) -> bool:
    """Check if the roadmap is formatted correctly for two quarters."""
    # TODO: Implement the logic to check if the roadmap is formatted correctly for two quarters.
    return True  # If all lines are valid

async def handle_project_roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    roadmap = update.message.text  # Retrieve the user's response
    if is_valid_roadmap(roadmap):  # Check if the format is valid
        context.user_data['project_roadmap'] = roadmap  # Store the roadmap
        await update.message.reply_text("Thank you for providing the project roadmap! Let's summarize your project.")
        return await team_information(update, context)  # Call the summary after collecting all information
    else:
        await update.message.reply_text(
            "Invalid format. Please ensure you outline your quarterly roadmap correctly."
            "Example:\n"
            "Q1:\n"
            " • Launch the MVP (Minimum Viable Product)\n"
            " • Acquire first 100 users\n"
            "Q2:\n"
            " • Expand marketing efforts to increase user base by 50%\n"
            " • Implement user feedback to improve product features"
        )
        return PROJECT_ROADMAP  # Stay in the PROJECT_ROADMAP state to ask again

async def team_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Team Information\n"
        "For each key team member, provide:\n"
        " • Name and position\n"
        " • LinkedIn link (if available)\n"
        " • X/Twitter link (if available)\n\n"
        "Example:\n"
        "1. John Doe - CEO\n"
        "   LinkedIn: https://linkedin.com/in/johndoe\n"
        "   Twitter: https://twitter.com/johndoe\n\n"
        "2. Jane Smith - CTO\n"
        "   LinkedIn: https://linkedin.com/in/janesmith\n"
        "   Twitter: https://twitter.com/janesmith"
    )
    return TEAM_INFORMATION  # Return the state to wait for the user's response

def is_valid_team_info(team_info: str) -> bool:
    """Check if the team information is formatted correctly."""
    # TODO: Implement the logic to check if the team information is formatted correctly.
    return True  # If all lines are valid

async def handle_team_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    team_info = update.message.text  # Retrieve the user's response
    if is_valid_team_info(team_info):  # Check if the format is valid
        context.user_data['team_information'] = team_info  # Store the team information
        await update.message.reply_text("Thank you for providing the team information! Now let's move on to essential links.")
        return await essential_links(update, context)  # Call the essential links function
    else:
        await update.message.reply_text(
            "Invalid format. Please ensure you provide the team information correctly."
        )
        return TEAM_INFORMATION  # Stay in the TEAM_INFORMATION state to ask again

async def essential_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Essential Links\n"
        "Please provide the following links:\n"
        " • Pitch deck URL 📑\n"
        " • Community chat (Telegram/Discord) 💬\n"
        " • Website URL 🌐\n\n"
        "If you want to add another important link, add:\n"
        "- Name_Link link\n\n"
        "Example:\n"
        " • Pitch deck: https://example.com/pitchdeck\n"
        " • Community chat: https://t.me/examplechat\n"
        " • Website: https://example.com\n"
        " • Important Link: GitHub: https://github.com/example"
    )
    return ESSENTIAL_LINKS  # Return the state to wait for the user's response

def is_valid_essential_links(links: str) -> bool:
    """Check if the essential links are formatted correctly."""
    # TODO: Implement the logic to check if the essential links are formatted correctly.
    return True  # If all lines are valid

async def handle_essential_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    links = update.message.text  # Retrieve the user's response
    if is_valid_essential_links(links):  # Check if the format is valid
        context.user_data['essential_links'] = links  # Store the essential links
        await update.message.reply_text("Thank you for providing the essential links! Let's summarize your project.")
        return await summary(update, context)  # Call the summary after collecting all information
    else:
        await update.message.reply_text(
            "Invalid format. Please ensure you provide the essential links correctly."
        )
        return ESSENTIAL_LINKS  # Stay in the ESSENTIAL_LINKS state to ask again


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
    summary_text += f"Vesting Schedule: {user_data['vesting_schedule']}\n"
    summary_text += f"Project Roadmap: {user_data['project_roadmap']}\n"
    summary_text += f"Team Information: {user_data['team_information']}\n"
    summary_text += f"Essential Links: {user_data['essential_links']}\n"

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
            VESTING_SCHEDULE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_vesting_schedule)],
            PROJECT_ROADMAP: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_project_roadmap)],
            TEAM_INFORMATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_team_information)],
            ESSENTIAL_LINKS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_essential_links)],
        },
        fallbacks=[],
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("summary", summary))
    
    app.run_polling()

if __name__ == '__main__':
    main()