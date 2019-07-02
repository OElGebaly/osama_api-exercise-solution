

# -*- coding: utf-8 -*-
from io import TextIOWrapper
import csv
from flask import Flask, request
from os import environ as env
from uuid import uuid4


# Init app
app = Flask(__name__)

import api.routes

app.config['SQLALCHEMY_DATABASE_URI'] = env.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.get("SQLALCHEMY_TRACK_MODIFICATIONS")
app.secret_key = env.get("APP_SECRET_KEY")


from .models import Raw_data, db, raw_data_schema, raw_datas_schema

# Database
with app.app_context():
        db.init_app(app)
        db.create_all()  

try:
    csv_file = "../../db/titanic.csv"
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        uuid = uuid4()
        new_raw_data = Raw_data(uuid,survived=row[0], passengerClass=row[1], name=row[2], sex=row[3], age=row[4], siblingsOrSpousesAboard=row[5], parentsOrChildrenAboard=row[6], fare=row[7])

        db.session.add(new_raw_data)
        db.session.commit()

except Exception as e:
        print('Caught this error: ' + repr(e))
