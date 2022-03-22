from pymongo import MongoClient
import smtplib

HOST = "mongodb"
PORT = "27017"
MONGO_USER = "DUMMY"
MONGO_PASS = "PASS"
MONGO_DB = "fluentd"
MONGO_COL = "access"
E_USER="test@doman.com"
E_PASS="DUMMY"

client = MongoClient(
	host = [ str(HOST) + ":" + str(PORT) ],
	serverSelectionTimeoutMS = 3000,
	username = MONGO_USER,
	password = MONGO_PASS,
)

def get_status_count(client,MONGO_DB,MONGO_COL):
	res = {}
	fluentdb = client[MONGO_DB]
	collectn = fluentdb[MONGO_COL]
	for cl in collectn.find():
		status = cl['status']
		if status in res.keys():
			res[status] += 1
		else:
			res[status] = 1
	return res

def send_mail(count,E_USER,E_PASS):
	eClient = smtplib.SMTP('smtp.gmail.com', 587)
	eClient.starttls()
	eClient.login(E_USER, E_PASS)
	message = f"Number of access denial exceeds threshold. Count = {count}"
	eClient.sendmail(E_USER, E_PASS, message)
	eClient.quit()

if __name__ == "__main__":
	sCount = get_status_count(client,MONGO_DB,MONGO_COL)
	count = sCount['403']
	if  count > 10:
		try:
			send_mail(count,E_USER,E_PASS)
		except:
			print("Mail Send failed!!")
	else:
		print("Number of access denials is less than threshold")