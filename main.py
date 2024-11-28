import telebot

bot = telebot.TeleBot('8099407242:AAHV0VtZ1rfhj0k8omT6SaFrtT-NTDIuSKU')
 
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Я – ваш кулинарный помощник. Какой рецепт вы хотите сегодня попробовать?', parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Идеи для завтрака':
        bot.send_message(message.chat.id,
                         'Ищете идеи для завтрака? Попробуйте омлет с овощами и сыром – быстро и вкусно!',
                         parse_mode='Markdown')
    if message.text == 'Какие специи лучше всего подходят для рыбы?':
        bot.send_message(message.chat.id, 'Попробуйте использовать лимонный сок, укроп, чеснок и черный перец.',
                         parse_mode='Markdown')
    if message.text == 'Хочу рецепт десерта, чтобы порадовать семью':
        bot.send_message(message.chat.id,
                         'Попробуйте испечь шоколадный торт! Он станет отличным десертом.Вот один из рецептов: [Шоколадный торт](https://example.com/chocolate-cake)',
                         parse_mode='Markdown')
    if message.text == 'Поделись рецептом простого ужина':
        bot.send_message(message.chat.id,
                    'Попробуйте приготовить пасту с томатным соусом! Это быстро и вкусно. Советую попробовать этот рецепт: [Паста с томатным соусом](https://example.com/pasta-tomato-sauce)',
                    parse_mode='Markdown')
bot.infinity_polling()