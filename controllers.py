from locale import currency
from app import app
from flask import Flask , render_template,request,redirect
import requests
import xmltodict
from datetime import datetime, timedelta
import pymysql
from models import CurrencyRate, Currency
from extensions import *
from sqlalchemy.sql import exists 


@app.route('/')
def get_currency_list():
    currency_list = []
    today = datetime.now().strftime("%d.%m.%Y")
    yesterday_=datetime.now()-timedelta(days=1)
    yesterday= yesterday_.strftime("%d.%m.%Y")
    print(today)
    currencies = Currency.query.all()


    for currency in currencies:
        today_rate = CurrencyRate.query.filter_by(date=today, code=currency.code).first()
        yesterday_rate = CurrencyRate.query.filter_by(date=yesterday, code=currency.code).first()
        if today_rate.rate == yesterday_rate.rate:
             status = 'fa-right-left'
        elif today_rate.rate > yesterday_rate.rate:
            status = 'fa-arrow-up'
        else:
            status = 'fa-arrow-down'

        currency_data= {
            'name' : currency.name,
            'code' : currency.code,
            'rate_today' : today_rate.rate,
            'rate_yesterday' : yesterday_rate.rate,
            'status': status
       

        }
        currency_list.append(currency_data)
    return render_template("index.html" , currency_list=currency_list, today=today, yesterday=yesterday)



@app.route("/setRate/<date>")
def addRates(date):
    exists = CurrencyRate.query.filter_by(date=date).first()
    if not exists:
        api_resp=requests.get(f'https://www.cbar.az/currencies/{date}.xml')
        resp_dict=xmltodict.parse(api_resp.content)
        currency_list = resp_dict['ValCurs']['ValType'][1]['Valute'] 
        for currency in currency_list:
            code=currency['@Code']
            rate=currency['Value']
            date=date
            new_currency = CurrencyRate(code=code, rate=rate, date=date)
            new_currency.save()

    return 'any'
    



# @app.route("/setrate/<date>")
# def addRates(date):
#     today = datetime.now().strftime("%d.%m.%Y")
#     currency=requests.get(f'https://www.cbar.az/currencies/{date}.xml')
#     currency_list=xmltodict.parse(currency.content)
#     currency_list = currency_list['ValCurs']['ValType'][1]['Valute'] 
#     for currency1 in currency_list:
#         name = currency1['Name'] 
#         code=currency1['@Code']
#         status = 'any'
#         currency = Currency( name=name,code=code, status=status)
#         currency.save()
        

#     return redirect ('/index')
    

# @app.route("/setrate")
# def addRates():
#     date = request.args.get("date")
#     print(date)
#     return date
#     currency=requests.get(f'https://www.cbar.az/currencies/{date}.xml')
#     currency_list=xmltodict.parse(currency.content)
#     currency_list = currency_list['ValCurs']['ValType'][1]['Valute'] 
#     for currency in currency_list:
#         code=currency['@Code']
#         rate=currency['Value']
        
#         currency = CurrencyRate( code=code, rate=rate, date=date)
#         currency.save()

#     return redirect ('/setRate')








