#----------------------------------------------------------
Order_status = "Inprogress"
if Order_status=="Paid":
	print("Paid")
else:
	print("Unpaid")
#----------------------------------------------------------
elec_bill=500
if elec_bill>300:
	print("High bill")
else:
	print("Normal")
#----------------------------------------------------------
user="premium"
purchase=9000
if user=="premium" and purchase>5000:
	print("yayy discounted")
elif user=="premium" and purchase>3000:
	print("small discount, sorry")
else:
	print("No discount")
#----------------------------------------------------------
credit_score = 90
salary = 60000
if salary>=30000:
	if  credit_score>=750:
		print("PreApproved Loan")
	else:
		print("Credit score not up to the mark")
else:
	print("Not eligible for the given salary")
#----------------------------------------------------------
marks=90
income=20000
if marks>=85:
	if income<30000:
		print("Scholarship eligible")
	else:
		print("Family income doesnt meet the criteria")
else:
	print("Student merit eligibility missed.")
#----------------------------------------------------------
username="checks"
OTP=1234
if username=="check":
	if OTP==1234:
		print("Access allowed")
	else:
		print("OTP Mismatch")
else:
	print("Username incorrect")
#----------------------------------------------------------
biometric = True
Intime = 8
if biometric:
	if Intime<=9:
		print("Present & Intime")
	else:
		print("Late to office")
else:
	print("Absent")