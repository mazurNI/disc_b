import discord
from discord.ext import commands
import openai
import random
from random import randint
import requests

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все при
bot = commands.Bot(intents=intents, command_prefix='*')

@bot.command
async def on_ready():
    print(f'We have logged in as {bot.user}')

# @bot.command()
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('$hello'):
#         await message.channel.send("Hi!")
#     elif message.content.startswith('$bye'):
#         await message.channel.send("\\U0001f642")
#     else:
#         await message.channel.send(message.content)

@bot.command()
async def mem(ctx):
    with open('mem2.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я {bot.user}!')

@bot.command()
async def revers(ctx, word):
    word_revers = ''
    for letter in word[::-1]:
        word_revers = word_revers + letter

    await ctx.send(word_revers)

@bot.command()
async def help_(ctx):
    """Функция возвращает список выполняемых ботом команд"""
    await ctx.send('Воспользуйтесь очень важной подсказкой:\n'
                   '*hello - приветствие бота\n'
                   '*revers <произвольное слово> - вывод слова в обратной последовательности\n'
                   '*mem - вывод картинки с мемом\n'
                   '*dice - выдает случайно число от 1 до 6\n')
    
@bot.command()
async def dice(ctx):
    await ctx.send('Выпадает цифра...')
    await ctx.send(randint(1,6))

@bot.command()
async def trash(ctx):
    await ctx.send('Разделять сбор мусора и сортировать его\n'
                   '----------------\n'
                   'Высокие штрафы:\n'
                   'Австрия — 7 тысяч рублей;\n'
                   'Австралия — 400 тысяч рублей;\n'
                   'Ирландия — 400 тысяч рублей и 12 месяцев тюрьмы;\n'
                   'Великобритания — 7 тысяч рублей;\n'
                   'Швейцария — 20 тысяч рублей;\n'
                   'Сингапур — 40 тысяч рублей и тюремное заключение;\n'
                   'Япония — 5 миллионов рублей и 5 лет тюрьмы.\n'
                   '----------------\n'
                   'Современный подход к переработке\n'
                   '----------------\n'
                   'Просто соблюдайте чистоту и старайтесь не выкидывать мусор мимо корзины)\n'
                   '-----------------------------НЕ МУСОРИ😎🗑️-------------------------------\n')

bot.run("MTEyNDcyMzQ5NTEwOTEzNjQxNQ.GrzRV8.kGp_IfKZhFI3-Y9QirHeb-rFSfR5SvH5tPYcHY")