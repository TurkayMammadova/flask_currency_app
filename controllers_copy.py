
    
# from app import app
# from flask import Flask , render_template,request,redirect
# import requests
# import xmltodict
# from datetime import datetime, timedelta
# import pymysql

# from extensions import *



# @app.route("/")
# def currency_data():
#     today = datetime.now().strftime("%d.%m.%Y")
#     yesterday=datetime.now()-timedelta(days=1)
#     yesterday_ = yesterday.strftime("%d.%m.%Y")

#     currency1=requests.get(f'https://www.cbar.az/currencies/{yesterday_}.xml')
#     currency_list1=xmltodict.parse(currency1.content)

    

#     currency_list1 = currency_list1['ValCurs']['ValType'][1]['Valute'] 


#     currency2=requests.get(f'https://www.cbar.az/currencies/{today}.xml')
#     currency_list2=xmltodict.parse(currency2.content)
#     currency_list2 = currency_list2['ValCurs']['ValType'][1]['Valute']
#     if request.method ==  'GET':
#         for i in range (len(currency_list2)) :
#             title=currency_list2[i]['Name']
#             code=currency_list2[i]['@Code']
#             kurs_today=currency_list2[i]['Value']
#             currency = Currency(title=title, code=code, kurs_today=kurs_today)
#             currency.save()

#     if request.method ==  'GET':
#         for i in range (len(currency_list1)) :
#             kurs_yesterday=currency_list1[i]['Value']
#             currency = CurrencyYesterday(kurs_yesterday=kurs_yesterday)
#             currency.save()




#             return redirect("/index")

# @app.route('/index')
# def get_currency_list():
#     currency_list=Currency.query.all()
#     currency_list2 = CurrencyYesterday.query.all()

#     today = datetime.now().strftime("%d.%m.%Y")
#     yesterday=datetime.now()-timedelta(days=1)
#     yesterday_ = yesterday.strftime("%d.%m.%Y")
#     print(currency_list)
#     return render_template("index.html",currency_list=currency_list, currency_list2=currency_list2, today=today,yesterday=yesterday_)
    


# # connection = pymysql.connect(host='localhost',
# #                              user='root',
# #                              database='products_db',
# #                              charset='utf8mb4',
# #                              password='123',
# #                              cursorclass=pymysql.cursors.DictCursor )

# # with connection:
# #     with connection.cursor() as cursor:
# #         # Create a new record
# #         sql = "INSERT INTO `Cerrency` ('title', 'kod','kurs') VALUES (%s, %s,%s)"
# #         cursor.execute(sql,('name','code','kurs'))
# #     connection.commit()
#     return render_template("index.html", cerrency_list = cerrency_list, cerrency_list2 =  cerrency_list2, today=today,yesterday=yesterday_)






# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              database='products_db',
#                              charset='utf8mb4',
#                              password='123',
#                              cursorclass=pymysql.cursors.DictCursor )

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `Cerrency` ('title', 'kod','kurs') VALUES (%s, %s,%s)"
#         cursor.execute(sql,('name','code','kurs'))
#     connection.commit()

    # return render_template("index.html", cerrency_list = cerrency_list, cerrency_list2 =  cerrency_list2, today=today,yesterday=yesterday_)






# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              database='products_db',
#                              charset='utf8mb4',
#                              password='123',
#                              cursorclass=pymysql.cursors.DictCursor )

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `Cerrency` ('title', 'kod','kurs') VALUES (%s, %s,%s)"
#         cursor.execute(sql,('name','code','kurs'))
#     connection.commit()





   for currency in currencies:
        today_rate = CurrencyRate.query.filter_by(date=today, code=currency.code).first()
        yesterday_rate = CurrencyRate.query.filter_by(date=yesterday, code=currency.code).first()
        currency_data={
            'name' : currency.name,
            'code' : currency.code,
            'rate' : today_rate,
            'rate': yesterday_rate,

            # 'status': "arrow-up"
        }
        currency_list.append(currency_data)
    return render_template("index.html" , currency_list=currency_list, today=today, yesterday=yesterday)
