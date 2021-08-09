import logging

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, CallbackQueryHandler

# Habilitando o log do bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

CHOOSE = range(1)

SUPORTE, REDES, SISTEMAS, PRODATA = range(4)


def start(update: Update, context: CallbackContext) -> int:
    # Manda uma mensagem quando o comando /start é acionado.
    keyboard = [
        [
            InlineKeyboardButton("Suporte", callback_data=str(SUPORTE)),
            InlineKeyboardButton("Redes", callback_data=str(REDES)),
        ],
        [
            InlineKeyboardButton("Sistemas", callback_data=str(SISTEMAS)),
            InlineKeyboardButton("Prodata", callback_data=str(PRODATA)),
        ]
    ]
    markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Olá! Me chamo JorgeTron, sou o BOT de suporte da Agência de Tecnologia da Informação do Município de Palmas.'
        '\nDe qual desses setores você precisa de ajuda?',
        reply_markup=markup,
    )

    return CHOOSE


def suporte(update: Update, context: CallbackContext) -> int:
    # Respondendo com o número de cada setor
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Para entrar em contato com o setor do suporte, ligue para 3212-7211.")
    return ConversationHandler.END


def redes(update: Update, context: CallbackContext) -> int:
    # Respondendo com o número de cada setor
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Para entrar em contato com o setor de redes, ligue para 3212-7212 e fale com a recepção')
    return ConversationHandler.END


def sistemas(update: Update, context: CallbackContext) -> int:
    # Respondendo com o número de cada setor
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Para entrar em contato com o setor de sistemas, ligue para 3212-7224 e fale com a recepção')
    return ConversationHandler.END


def prodata(update: Update, context: CallbackContext) -> int:
    # Respondendo com o número de cada setor
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Para entrar em contato com o setor da prodata, ligue para 3212-7204 e fale com a recepção')
    return ConversationHandler.END


# COnfigurando o BOT.
def main():
    # Informando o token do BOT.
    updater = Updater("1898930367:AAH8hXpxZYEuEOt-d0guZ8UU2DG3Ook8jkk")

    # Criando a variável dispatcher para melhor envio das mensagens para o BOT.
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSE: [
                CallbackQueryHandler(
                    suporte, pattern='^' + str(SUPORTE) + '$'),
                CallbackQueryHandler(redes, pattern='^' + str(REDES) + '$'),
                CallbackQueryHandler(
                    sistemas, pattern='^' + str(SISTEMAS) + '$'),
                CallbackQueryHandler(
                    prodata, pattern='^' + str(PRODATA) + '$'),
            ]
        },
        fallbacks=[CommandHandler('start', start)]

    )

    # Comandos do que poderão ser utilizados com o bot.
    dispatcher.add_handler(conv_handler)

    # Iniciando o BOT.
    updater.start_polling()

    # O BOT irá rodar até utilizar as teclas Ctrl + C.
    updater.idle()

if __name__ == '__main__':
    main()
