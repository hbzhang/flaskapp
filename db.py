from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'b2a96b5dac6889'
app.config['MYSQL_DATABASE_PASSWORD'] = '3b9e36b5'
app.config['MYSQL_DATABASE_DB'] = 'heroku_b1ddb90599150e5'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-01.cleardb.net'
mysql.init_app(app)
