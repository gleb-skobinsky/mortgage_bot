import re
from telegram import Bot, Update
from telegram.ext import Updater,CommandHandler, MessageHandler, filters
from telegram.utils.request import Request
from telegram.ext.filters import Filters
from allennlp.predictors.predictor import Predictor
from absa_bert.predictors.sentence_classifier_predictor import SentenceClassifierPredictor
from allennlp.models.archival import load_archive
from allennlp.data.dataset_readers.dataset_reader import DatasetReader
import os
from datetime import datetime
from filtering import get_text_from_label

pwd="[TELEGRAM_BOT_PASSWORD]"

archive = load_archive("mortgage_model.tar.gz")
model = archive.model
dataset_reader_params = archive.config["dataset_reader"]
dataset_reader = DatasetReader.from_params(dataset_reader_params)
predictor = SentenceClassifierPredictor(model, dataset_reader)

def start(update, context):
    update.message.reply_text('Привет! Здесь ты можешь узнать ставку по ипотеке в Сбербанке.')

def get_time(update,context):
    print(update.message.text)
    now=datetime.now()
    dt_string=now.strftime("%d/%m/%Y_%H:%M:%S")
    update.message.reply_text(f"Current Time is : {dt_string}")

def echo(update, context):
    text = update.message.text
    if "нов" in text.lower() or "перв" in text.lower() or "застрой" in text.lower():
        # Из-за перекоса в обучающих данных модель
        # никогда не выбирает новостройку, если текст не начинается
        # со слов "ставка" или "стоимость"
        text = "Ставка и взнос " + text
    probs = predictor.predict(sentence=text)
    probab_list = probs['probs']
    label = int(probab_list.index(max(probab_list)))
    response = get_text_from_label(label, text)
    update.message.reply_text(response)

def main():
    req=Request(connect_timeout=0.5)
    my_bot=Bot(token=pwd,request=req)
    updater=Updater(bot=my_bot,use_context=True)
    dp=updater.dispatcher
    cmd=[("gettime","get the current date time in string format")]
    start_cmd=[("start","Начало общения с ботом")]
    my_bot.set_my_commands(cmd)
    my_bot.set_my_commands(start_cmd)
    dp.add_handler(CommandHandler("gettime",get_time))
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(filters = Filters.all, callback=echo))
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
