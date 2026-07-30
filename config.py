"""
Модуль для настройки Telegram-бота.
"""
import os
import telebot

TOKEN = os.getenv('8935702983:AAELaMVrcO0smlq5MtxBB3A2qfInfW_pxAo')
ADMIN_ID = int(os.getenv('ADMIN_ID', 848208221))
bot = telebot.TeleBot(TOKEN)
