import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, CallbackQueryHandler

# Habilitando o log do bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

SETORES, SUPORTEPROBLEMAS = range(2)
SIM, NAO = range(2)
SUPORTE, REDES, SISTEMAS, PRODATA = range(4)
PCNAOLIGA, PCSEMINTERNET, PCSEMINTERNET2, PCNAOIMPRIME, NOBREAKNAOLIGA = range(5)

# O comando /start começa a sequência de conversas com o BOT.


def start(update, context):
    botoes = [
        [
            InlineKeyboardButton("Suporte", callback_data=str(SUPORTE)),
            InlineKeyboardButton("Redes", callback_data=str(REDES)),
        ],
        [
            InlineKeyboardButton("Sistemas", callback_data=str(SISTEMAS)),
            InlineKeyboardButton("Prodata", callback_data=str(PRODATA)),
        ]
    ]
    teclado = InlineKeyboardMarkup(botoes)

    update.message.reply_text(
        'Olá! Me chamo JorgeTron, sou o BOT de suporte da Agência de Tecnologia da Informação do Município de Palmas.'
        '\nDe qual desses setores você precisa de ajuda?',
        reply_markup=teclado,
    )

    return SETORES


def suporte(update: Update, context: CallbackContext) -> int:
    botoes = [
        [
            InlineKeyboardButton("Computador não está ligando",
            callback_data=str(PCNAOLIGA)),
            InlineKeyboardButton("Computador está sem internet",
            callback_data=str(PCSEMINTERNET)),
        ],
        [
            InlineKeyboardButton(
                "Computador não está imprimindo", callback_data=str(PCNAOIMPRIME)),
            InlineKeyboardButton("Nobreak não está ligando",
            callback_data=str(NOBREAKNAOLIGA)),
        ]
    ]
    teclado = InlineKeyboardMarkup(botoes)

    # update.callback_query.answer()
    update.callback_query.edit_message_text('Dentre esse problemas mais comuns, por qual deles você está passando?',
                                            reply_markup=teclado
                                            )

    return SUPORTEPROBLEMAS


# def redes(update: Update, context: CallbackContext) -> int:
    botoes = [
        [
            InlineKeyboardButton("Computador não está ligando",
            callback_data=str(PCNAOLIGA)),
            InlineKeyboardButton("Computador está sem internet",
            callback_data=str(PCSEMINTERNET)),
        ],
        [
            InlineKeyboardButton(
                "Computador não está imprimindo", callback_data=str(PCNAOIMPRIME)),
            InlineKeyboardButton("Nobreak não está ligando",
            callback_data=str(NOBREAKNAOLIGA)),
        ]
    ]
    teclado = InlineKeyboardMarkup(botoes)

    update.callback_query.edit_message_text(
        'Dentre esse problemas mais comuns, por qual deles você está passando?',
        reply_markup=teclado
    )

    return REDESPROBLEMAS


def sistemas(update: Update, context: CallbackContext) -> int:
    # Respondendo com o número de cada setor
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Para entrar em contato com o setor de sistemas, ligue para 3212-7224 e fale com a recepção')
    return ConversationHandler.END


def prodata(update: Update, context: CallbackContext) -> int:
    # Respondendo com o número de cada setor
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Para entrar em contato com o setor da prodata, ligue para 3212-7204 e fale com a recepção')
    return ConversationHandler.END


def pc_nao_liga(update: Update, context: CallbackContext) -> int:
    botoes = [
        [
            InlineKeyboardButton("Sim", callback_data=str(SIM)),
            InlineKeyboardButton("Não", callback_data=str(NAO)),
        ]
    ]
    teclado = InlineKeyboardMarkup(botoes)

    update.callback_query.edit_message_text(
        '1º Solução - Cabos desconectados ou mal conectados'
        '\na. Verifique se o cabo de forçã não está mal conectado'
        '\nb. Verifique se o cabo de força que está conectado, caso não esteja, conecte-o.'
        '\nc. Verifique se o cabo de força está conectado no nobreak ou na tomada, caso não esteja, conecte-o.'
        '\n'
        '\n2º Solução - Nobreak desligado'
        '\na. Caso esteja desligado, ligue-o novamente.'
        '\n'
        '\n3º Solução - Monitor desligado ou mal conectado'
        '\na. Cheque os cabos do monitor, eles podem estar mal encaixados ou apenas desconectados.'
        '\n'
        '\nAlgumas dessas soluções te ajudaram com seu problema?',
        reply_markup=teclado
    )

    return


def pc_sem_internet(update: Update, context: CallbackContext) -> int:
    botao = [
        [
            InlineKeyboardButton("Próximo", callback_data=str(PCSEMINTERNET2)),
        ]
    ]
    teclado = InlineKeyboardMarkup(botao)

    update.callback_query.edit_message_text(
        'Algumas dessas soluções te ajudaram com seu problema?'
        '\na. Verifique se o cabo de forçã não está mal conectado'
        '\nb. Verifique se o cabo de força que está conectado, caso não esteja, conecte-o.'
        '\nc. Verifique se o cabo de força está conectado no nobreak ou na tomada, caso não esteja, conecte-o.',
        reply_markup=teclado
    )

    return SUPORTEPROBLEMAS


def pc_sem_internet2(update: Update, context: CallbackContext) -> int:
    botoes = [
        [
            InlineKeyboardButton("Sim", callback_data=str(SIM)),
            InlineKeyboardButton("Não", callback_data=str(NAO)),
        ]
    ]
    teclado = InlineKeyboardMarkup(botoes)

    update.callback_query.edit_message_text(
        'Algumas dessas soluções te ajudaram com seu problema?',
        reply_markup=teclado
    )

    return 1


def pc_nao_imprime(update: Update, context: CallbackContext) -> int:

    return 1


def nobreak_nao_liga(update: Update, context: CallbackContext) -> int:

    return 1


# COnfigurando o BOT.
def main():
    # Informando o token do BOT.
    updater = Updater("1945206664:AAHrXgJKfePIlxG2hmNCNB-qnZp-eBkGM8g")

    # Criando a variável dispatcher para melhor envio das mensagens para o BOT.
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SETORES: [
                CallbackQueryHandler(
                    suporte, pattern='^' + str(SUPORTE) + '$'),
                # CallbackQueryHandler(
                # redes, pattern='^' + str(REDES) + '$'),
                CallbackQueryHandler(
                    sistemas, pattern='^' + str(SISTEMAS) + '$'),
                CallbackQueryHandler(
                    prodata, pattern='^' + str(PRODATA) + '$'),
            ],
            SUPORTEPROBLEMAS: [
                CallbackQueryHandler(
                    pc_nao_liga, pattern='^' + str(PCNAOLIGA) + '$'),
                CallbackQueryHandler(
                    pc_sem_internet, pattern='^' + str(PCSEMINTERNET) + '$'),
                CallbackQueryHandler(
                    pc_sem_internet2, pattern='^' + str(PCSEMINTERNET2) + '$'),
                CallbackQueryHandler(
                    pc_nao_imprime, pattern='^' + str(PCNAOIMPRIME) + '$'),
                CallbackQueryHandler(
                    nobreak_nao_liga, pattern='^' + str(NOBREAKNAOLIGA) + '$'),
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
