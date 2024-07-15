from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import LeaveRequest
from app.forms import LeaveRequestForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    leaves = LeaveRequest.query.all()
    return render_template('index.html', leaves=leaves)

@main.route('/request_leave', methods=['GET', 'POST'])
def request_leave():
    form = LeaveRequestForm()
    if form.validate_on_submit():
        leave = LeaveRequest(
            name=form.name.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            reason=form.reason.data
        )
        db.session.add(leave)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('request_leave.html', form=form)

@main.route('/approve_leave/<int:leave_id>')
def approve_leave(leave_id):
    leave = LeaveRequest.query.get_or_404(leave_id)
    leave.status = 'Approved'
    db.session.commit()
    return redirect(url_for('main.index'))
