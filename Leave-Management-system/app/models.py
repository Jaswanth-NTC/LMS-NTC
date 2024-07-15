from datetime import datetime
from app import db

class LeaveRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(128))
    status = db.Column(db.String(10), default='Pending')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
