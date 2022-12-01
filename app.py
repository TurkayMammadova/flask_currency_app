from flask import Flask 
import configparser



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Testing321@localhost:3306/products_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "32dbaf20ae5f8f961952b9ad0269868c"




from extensions import *
from models import *
from controllers import *
from api import get_today_rates, get_rate_by_date


if __name__ == "__main__":
    app.run(port=5000,debug=True)

