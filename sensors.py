from app import db

class Diabetes(db.Model):
    __tablename__ = "Diabetes"
    id = db.Column(db.Integer, primary_key=True)
    sensor = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    print("DIABETES RABLE CREATED")

    def __init__(self, sensor, value, date):
        self.sensor = sensor
        self.value = value
        self.date = date

    @property
    def serialize(self):
        return {
            'sensor':self.sensor,
            'value':self.value,
            'date':self.date
        }