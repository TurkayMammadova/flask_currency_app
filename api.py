from locale import currency
from app import app
from flask import Flask , request
import requests
from datetime import datetime, timedelta
from flask import jsonify
from models import CurrencyRate, Currency



@app.route("/ratebydate")
def get_rate_by_date():
    currency_list = []
    date = request.args.get("date")
    currencies = Currency.query.all()
    for currency in currencies:
        rate = CurrencyRate.query.filter_by(date=date, code=currency.code).first()
        currency_data= {
            'name' : currency.name,
            'code' : currency.code,
            'rate' : rate.rate
        }
        currency_list.append(currency_data)
    return currency_list


@app.route("/todayrates")
def get_today_rates():
    currency_list = []
    today = datetime.now().strftime("%d.%m.%Y")
    currencies = Currency.query.all()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(currencies)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for currency in currencies:
        today_rate = CurrencyRate.query.filter_by(date=today, code=currency.code).first()
        currency_data= {
            'name' : currency.name,
            'code' : currency.code,
            'rate' : today_rate.rate,
            'date' : today
        }
        currency_list.append(currency_data)
    return currency_list


