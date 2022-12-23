from bot_config import dp, bot
from aiogram import types
import random

total = 150
player_action = 'компьютер'

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    print(message)
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                    f', ты написал мне "{message.text}", начинаем игру с конфетами: '
                                                      f'на столе лежит 150 конфет. Играют игрок против компьютера. '
                                                      f'Первый ход определяется жеребьёвкой. За один ход можно забрать '
                                                      f'не более чем 28 конфет. '
                                                      f'Все конфеты оппонента достаются сделавшему последний ход 🍬🍬🍬.'
                                                      f'Напиши команду "/go", если готов начать играть.')
    await bot.send_message(658776791, text=f'{message.from_user.first_name}'
                                                    f', ты написал мне "{message.text}"')

@dp.message_handler(commands=['go'])
async def start_bot(message: types.Message):
    print(message)
    global player_action
    global total
    total = 150
    possible_actions = ['компьютер', 'человек']
    player_action = random.choice(possible_actions)
    if player_action == 'компьютер':
        await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                          f', первый ход определяется жеребьёвкой, хожу я!')
        await bot.send_message(658776791, text=f'{message.from_user.first_name}'
                                                          f', первый ход определяется жеребьёвкой, хожу я!')
        m = total % 29
        if m == 0:
            m = random.choice(range(1, 29))
        total = total - m
        if total == 0:
            await bot.send_message(message.from_user.id, text=f'Я взял конфет: {m}. Я сделал последний ход, '
                                                              f'все конфеты достаются мне!')
            await bot.send_message(658776791, text=f'Я взял конфет: {m}. Я сделал последний ход, '
                                                              f'все конфеты достаются мне!')
        else:
            player_action = 'человек'
            await bot.send_message(message.from_user.id, text=f'Я взял конфет: {m}. Осталось конфет: {total}, твой ход')
            await bot.send_message(658776791, text=f'Я взял конфет: {m}. Осталось конфет: {total}, твой ход')

    else:
        await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                          f', первый ход твой!')
        await bot.send_message(658776791, text=f'{message.from_user.first_name}'
                                                          f', первый ход твой!')

@dp.message_handler()
async def anything(message: types.Message):
    global total
    global player_action
    if total > 0:
        if message.text.isdigit():
            if 0 == int(message.text):
                await message.reply(f'{message.from_user.first_name} ты не взял конфет, попробуй еще раз')
                await bot.send_message(658776791, f'{message.from_user.first_name}'
                                                             f' ты не взял конфет, попробуй еще раз')
            elif 0 < int(message.text) < 29 and total == int(message.text):
                total -= int(message.text)
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                             f' ты взял со стола {message.text} конфет. '
                                                             f'Конфет не осталось. Поздравляю с выигрышем!!! 🍬🍬🍬')
                await bot.send_message(658776791, f'{message.from_user.first_name}'
                                                             f' ты взял со стола {message.text} конфет. '
                                                             f'Конфет не осталось. Поздравляю с выигрышем!!! 🍬🍬🍬')
            elif 0 < int(message.text) < 29 and total > int(message.text):
                total -= int(message.text)
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                             f' взял со стола {message.text} конфет🍬. '
                                                             f'На столе осталось {total}🍬🍬🍬')
                await bot.send_message(658776791, f'{message.from_user.first_name}'
                                                             f' взял со стола {message.text} конфет🍬. '
                                                             f'На столе осталось {total}🍬🍬🍬')
                m = total % 29
                if m == 0:
                    m = random.choice(range(1, 29))
                total = total - m
                if total == 0:
                    await bot.send_message(message.from_user.id, text=f'Я взял конфет: {m}🍬. Я сделал последний ход, '
                                                                      f'все конфеты достаются мне!🍬🍬🍬')
                    await bot.send_message(658776791, text=f'Я взял конфет: {m}🍬. Я сделал последний ход, '
                                                           f'все конфеты достаются мне!🍬🍬🍬')
                else:
                    player_action = 'человек'
                    await bot.send_message(message.from_user.id,
                                           text=f'Я взял конфет: {m}🍬. Осталось конфет: {total}🍬🍬, твой ход')
                    await bot.send_message(658776791, text=f'Я взял конфет: {m}🍬. Осталось конфет: {total}🍬🍬, твой ход')
            else:
                await message.reply(f'{message.from_user.first_name} да ты жадина, не хочешь ли взять поменьше')
                await bot.send_message(658776791, f'{message.from_user.first_name} да ты жадина, '
                                                  f'не хочешь ли взять поменьше')
        else:
            await message.reply(f'{message.from_user.first_name} надо написать именно число, сколько конфет хочешь взять')
            await bot.send_message(658776791, f'{message.from_user.first_name} надо написать именно число, '
                                              f'сколько конфет хочешь взять')
    else:
        await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name} конфет больше нет! '
                                                          f'Напиши команду "/go", '
                                                          f'если готов начать играть. Я насыплю новую кучку  🍬🍬🍬'
                                                          f'Напиши команду "/start" и я повторю правила игры.')
        await bot.send_message(658776791, text=f'{message.from_user.first_name} конфет больше нет! '
                                                          f'Напиши команду "/go", '
                                                          f'если готов начать играть. Я насыплю новую кучку  🍬🍬🍬'
                                                          f'Напиши команду "/start" и я повторю правила игры.')
#
# while count != 0:
#     if player_action == user:
#         while True:
#             try:
#                 n = int(input('Сколько конфет возьмете? Введите число (не более 28 конфет): '))
#                 if n in range(1,29):
#                     break
#                 else:
#                     print('Ошибка! Требуется ввести число от 1 до 28!')
#             except:
#                 print('Ошибка! Требуется ввести целое число')
#         count = count - n
#         if count == 0:
#             print(f'ы взяли конфет: {n}. Вы сделали последний ход, все конфеты достаются вам!')
#         else:
#             player_action = 'компьютер'
#             print(f'Вы взяли конфет: {n}. Осталось конфет: {count}')
#             print(f'Ходит {player_action}')
#     else:
#         m = count%29
#         if m == 0:
#             m = random.choice(range(1,29))
#         count = count - m
#         if count == 0:
#             print(f'Компьютер взял конфет: {m}. Компьютер сделал последний ход, все конфеты достаются ему!')
#         else:
#             player_action = 'человек'
#             print(f'Компьютер взял конфет: {m}. Осталось конфет: {count}')
#             print(f'Ходит {player_action}')
#


