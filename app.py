from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from io import StringIO
import csv
import datetime
from werkzeug.wrappers import Response

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:dbpass@ip_address:port/dbname'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# database
db = SQLAlchemy(app)

from sensors import Diabetes

# DB data creation
db.create_all()

#Routes
#GET Data
@app.route('/getData/all/<string:form>', methods=['GET'])
def getDataAll(form):
    data = Diabetes.query.all()
    if form == "json":
        return jsonify(data=[d.serialize for d in data])
    elif form == "csv":
        output = StringIO()
        writer = csv.writer(output)
        line = ['sensor, value, created']
        writer.writerow(line)

        for row in data:
            line = [str(row.sensor) + ", " + str(row.value) + ", " + str(row.date)]
            writer.writerow(line)

        output.seek(0)
        return Response(output, mimetype="text/csv",
                        headers={"Content-Disposition": "attachment;filename=sensors_data.csv"})
    else:
        return "<h1>ERROR, YOU NEED TO INDICATE THE RIGHT FORMAT (JSON OR CSV)</h1>"


@app.route('/getData/<int:sensor>/<string:form>', methods=['GET'])
def getData(sensor, form):
    if 0 <= sensor < 4:
        data = Diabetes.query.filter_by(sensor=sensor).all()
        if form == "json":
            return jsonify(data=[d.serialize for d in data])
        elif form == "csv":
            output = StringIO()
            writer = csv.writer(output)
            line = ['value, created']
            writer.writerow(line)

            for row in data:
                line = [str(row.value) + ", " + str(row.date)]
                writer.writerow(line)

            output.seek(0)

            fileName = "";
            if sensor == 0:
                fileName = "temperatures.csv"
            if sensor == 1:
                fileName = "galvanics.csv"
            if sensor == 2:
                fileName = "heartRates.csv"
            if sensor == 3:
                fileName = "oxygens.csv"

            return Response(output, mimetype="text/csv",
                            headers={"Content-Disposition": "attachment;filename=" + fileName})
        else:
            return "<h1>ERROR, YOU NEED TO INDICATE THE RIGHT FORMAT (JSON OR CSV)</h1>"
    else:
        return "<h1>ERROR, THERE IS NO SUCH SENSOR TYPE</h1>"

#POST/GET New Data
@app.route('/addData', methods=['POST','GET'])
def addData():
    if request.method == 'POST':
        print(request)
        sensor = request.json['sensor']
        value = request.json['value']
        created = request.json['date']
        date = datetime.datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
        print("NEW VALUE: [SENSOR=" + sensor + ", VALUE=" + value + ", DATE=" + str(date) + "]")
        newData = Diabetes(sensor=sensor, value=value, date=date)
        db.session.add(newData)
        db.session.commit()
        return newData.serialize
    else:
        return "<h1>Welcome to webserver! GET addData request sucess!!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
