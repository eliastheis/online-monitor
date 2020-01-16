import mysql.connector

from time import strftime



sql = None

db = None



def p(prefix, text): # nice print function

	t = getTime()

	print("[" + t + "][" + prefix + "] " + text)

def pp(prefix, text, line_end=''): # nice print function

	t = getTime()

	print("[" + t + "][" + prefix + "] " + text, end=line_end)



def getTime(format="%d.%m.%Y %H:%M:%S"):

	try:

		return strftime(format)

	except Exception:

		return getTime("%d.%m.%Y %H:%M:%S")



def getSqlConfig():

	host = ""

	user = ""

	password = ""

	database = ""

	try:

		with open("sql.con") as f:

			lines = f.readlines()

			for line in lines:

				if line.startswith("host"):

					host = line.replace("host=", "").replace("\n", "")

				if line.startswith("user"):

					user = line.replace("user=", "").replace("\n", "")

				if line.startswith("password"):

					password = line.replace("password=", "").replace("\n", "")

				if line.startswith("database"):

					database = line.replace("database=", "").replace("\n", "")

	except Exception as e:

		p("ERROR", "something went wrong with the sql.con")

		print(e)

		p("ERROR", "exiting...")

		exit()

	return host, user, password, database



def connectToSQL(h, u, pa, d):

	global sql

	global db

	try:

		db = mysql.connector.connect(host=h, user=u, passwd=pa, database=d)

		sql = db.cursor()

		p("MySQL", "connected to database: " + h + ", " + u + ", " + pa + ", " + d)

	except Exception as e:

		p("ERROR", "something went wrong with the sql connection: " + h + ", " + u + ", " + pa + ", " + d)

		print(e)

		p("ERROR", "exiting...")

		exit()

	return sql



def disconnectFromSQL():

	util.sql.close()

	p("MySQL", "dissconnected from database")



def executeSQL(cmd):

	global sql

	global db

	try:

		sql.execute(cmd)

		if "select" in cmd.lower() or 'show' in cmd.lower():

			return sql.fetchall()

		else:

			db.commit()

	except Exception as e:

		print(e)

		print('CMD:', cmd)

		exit()



def executeSQLMulti(cmd):

	global sql

	global db

	sql.execute(cmd, multi=True)

	db.commit()

	if "select" in cmd.lower() or 'show' in cmd.lower():

		return sql.fetchall()