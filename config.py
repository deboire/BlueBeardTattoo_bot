"""
Модуль для настройки Telegram-бота.
"""
import os
import telebot

# Переменные окружения
TOKEN = os.getenv('TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID', 848208221))

# Проверка, что токен получен
if TOKEN is None:
    raise ValueError("Переменная TOKEN не найдена! Добавьте её в Railway Variables.")

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)
