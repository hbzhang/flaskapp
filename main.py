import io
import csv
import pymysql
from app import app
from db import mysql
from flask import send_file, Flask, Response, render_template,jsonify

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'],
                                      _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/getimage', methods=['GET'])

def getImage():
    filename = 'shoot.png'
    return send_file(filename, mimetype='image/png')

@app.route('/getrisk', methods=['GET'])
def get_employee():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)

		cursor.execute("SELECT emp_id, emp_first_name, emp_last_name, emp_designation FROM employee")
		result = cursor.fetchall()
		for row in result:
			line = [str(row['emp_id']) + ',' + row['emp_first_name'] + ',' + row['emp_last_name'] + ',' + row[
			'emp_designation']]
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
	return jsonify({'threats': [{"gunthreat":"high"}]})
	#return jsonify({'tasks': [make_public_task(task) for task in tasks]})

@app.route('/')
def download():
	return render_template('download.html')


@app.route('/download/report/csv')
def download_report():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)

		cursor.execute("SELECT emp_id, emp_first_name, emp_last_name, emp_designation FROM employee")
		result = cursor.fetchall()

		output = io.StringIO()
		writer = csv.writer(output)

		line = ['Emp Id, Emp First Name, Emp Last Name, Emp Designation']
		writer.writerow(line)

		for row in result:
			line = [str(row['emp_id']) + ',' + row['emp_first_name'] + ',' + row['emp_last_name'] + ',' + row['emp_designation']]
			writer.writerow(line)

		output.seek(0)

		return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=employee_report.csv"})
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

if __name__ == "__main__":
    app.run()
