import logging

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, CallbackQueryHandler

# Habilitando o log do bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

SETORES, SUPORTEPROBLEMAS = range(2)

SIM, NAO = range(2)

SUPORTE, REDES, SISTEMAS, PRODATA = range(4)

PCNAOLIGA, PCSEMINTERNET, PCNAOIMPRIME, NOBREAKNAOLIGA = range(4)

#O comando /start começa a sequência de conversas com o BOT.
def start(update: Update, context: CallbackContext) -> int:
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
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Olá! Me chamo JorgeTron, sou o BOT de suporte da Agência de Tecnologia da Informação do Município de Palmas.'
        '\nDe qual desses setores você precisa de ajuda?',
        reply_markup = reply_markup,
    )

    return SETORES


def suporte(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [
            InlineKeyboardButton("Computador não está ligando", callback_data=str(PCNAOLIGA)),
            InlineKeyboardButton("Computador está sem internet", callback_data=str(PCSEMINTERNET)),
        ],
        [
            InlineKeyboardButton("Computador não está imprimindo", callback_data=str(PCNAOIMPRIME)),
            InlineKeyboardButton("Nobreak não está ligando", callback_data=str(NOBREAKNAOLIGA)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.answer()
    update.callback_query.edit_message_text('Dentre esse problemas mais comuns, por qual deles você está passando?',
        reply_markup = reply_markup 
    )

    return SUPORTEPROBLEMAS


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


# def botoes(update: Update) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Sim", callback_data=str(SIM)),
            InlineKeyboardButton("Não", callback_data=str(NAO)),
        ]
    ]
    global botoes_confirmacao
    botoes_confirmacao = InlineKeyboardMarkup(keyboard)
    global texto_confirmacao
    texto_confirmacao = 'Algumas dessas instruções ajudaram você com seu problema?'


def pc_nao_liga(update: Update, context: CallbackContext) -> int:

    update.callback_query.answer()
    update.callback_query.edit_message_text(
        '1º Solução - Cabos desconectados'
        '\na. Veja se o cabo de força que fica na parte de trás do seu computador está conectado, caso não esteja, conecte-o.' 
        '\nb. Veja se o cabo de força que sai do seu computador está conectado na tomada ou no Nobreak, caso não esteja, conecte-o.'
        '\n'
        '\n2º Solução - Nobreak desligado'
        '\na. Pode ser que apenas o seu nobreak, caso utilize um, esteja desligado. Nesse caso apenas o ligue novamente.'
        '\n'
        '\n3º Solução - Monitor desligado ou mal conectado'
        '\na. Muitas vezes podemos achar que o computador desligou, quando na verdade foi apenas nosso monitor, cheque os cabos do monitor, ou eles podem estar mal encaixados ou apenas desconectados.'
    )

    keyboard = [
        [
            InlineKeyboardButton("Sim", callback_data=str(SIM)),
            InlineKeyboardButton("Não", callback_data=str(NAO)),
        ]
    ]
    botoes_confirmacao = InlineKeyboardMarkup(keyboard)
    texto_confirmacao = 'Algumas dessas instruções ajudaram você com seu problema?'

    update.callback_query.edit_message_text(text=texto_confirmacao, reply_markup=botoes_confirmacao)

    return 

def pc_sem_internet(update: Update, context: CallbackContext) -> int:
    

    return 1


def pc_nao_imprime(update: Update, context: CallbackContext) -> int:
    

    return 1


def nobreak_nao_liga(update: Update, context: CallbackContext) -> int:
    

    return 1

    
# COnfigurando o BOT.
def main():
    # Informando o token do BOT.
    updater = Updater("1898930367:AAH8hXpxZYEuEOt-d0guZ8UU2DG3Ook8jkk")

    # Criando a variável dispatcher para melhor envio das mensagens para o BOT.
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SETORES: [
                CallbackQueryHandler(
                    suporte, pattern='^' + str(SUPORTE) + '$'),
                CallbackQueryHandler(
                    redes, pattern='^' + str(REDES) + '$'),
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
