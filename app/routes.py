from flask import Blueprint, render_template, request, redirect, url_for, flash
from .decorators import login_required, role_required
from .models import db, Employee

bp = Blueprint("main", __name__)

@bp.route('/')
def index():
    # return render_template('home.html')
    employees = Employee.query.all()
    return render_template('admin/index.html', employees=employees)

@bp.route('/dashboard')
@login_required
def dashboard():
    employees = Employee.query.all()
    return render_template('dashboard.html', employees=employees)

@bp.route('/admin')
@login_required
@role_required('admin')
def admin_area():
    employees = Employee.query.all()
    return render_template('admin/index.html', employees=employees)

@bp.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        membership = request.form['membership']
        rate = request.form['rate']
        hours = request.form['hours']
        if rate <= "0" or hours <="0":
            flash(f'Rate or Hours should not be zero o less!')
            return render_template('admin/add.html')
        salary = float(rate) * int(hours)
        total = salary
        if membership.lower() == 'part-time' or  membership.lower() == 'Part-time':
            total = salary * .10 
            new_employee.netpay = salary - total
        if not name.strip() or not membership.strip():
            flash('Incomplete Information')
            return render_template('admin/add.html')

        new_employee = Employee( name=name, membership=membership, rate=rate, hours=hours, netpay=total)
        db.session.add(new_employee)
        db.session.commit()
        flash(f'Added new {membership} employee successfully!')
        return redirect(url_for('main.index'))


    return render_template('admin/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.membership = request.form['membership']
        employee.rate = request.form['rate']
        employee.hours = request.form['hours']
        if employee.rate <= "0" or employee.hours <="0":
            flash(f'Rate or Hours should not be zero o less!')
            return render_template('admin/edit.html')
        salary = float(employee.rate) * int(employee.hours)
        if employee.membership.lower() == 'part-time' or employee.membership.lower() == 'Part-time' :
            total = salary * .10
            employee.netpay = salary - total
        else:
            employee.netpay = salary

        db.session.commit()
        flash('Updated successfully!')
        return redirect(url_for('main.index'))

    return render_template('admin/edit.html', employee=employee)

@bp.route('/delete/<int:id>')
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee deleted successfully!')
    return redirect(url_for('main.index'))
