Library_books={"Science":1,"Maths":45,"Social":90,"Biology":25,"Hindi":20,"Telugu":25,"English":40,"Physics":50}
def Library_Management(Library_books,Return_Days,Requested_book,Request_count=5,Issued=False):
	while Requested_book
	if len(Library_books)!=0:
		for i in Library_books:
			print("Available books in",i, "are:",Library_books[i])
			if Library_books[Requested_book]!=0:
				print("Issue granted")
				Issued=True
			else:
				print("Book not available")

	
Library_Management(Library_books,5,"Maths")


request=input("Enter the book needed: ")
Issued=False
if request in Library_books:
		if Library_books[request]!=0:
			print("Issue granted")
			Issued=True
		else:
			print("Book not available")
else:
		print("Not present in library")
# Reduce book quantity after issuing.
if Issued:
	Library_books[request]=Library_books[request]-1
	print(Library_books)
# Allow issuing multiple books (system runs continuously).
# Provide an exit option to stop the system.
req_count=0
while Library_books!=0:
	request=input("Enter the requirement: ")
	req_count=req_count+1
	print(req_count)
	if req_count == 5:
		print("Max limit exceeded,try again later")
		break
	if request in Library_books: 
		if Library_books[request]!=0:
			print("Book issued")
			days_calc=int(input("how many days back was this book issued"))
			if days_calc>3:
				if days_calc>=7:
					print("fine of 200 rupees")
					print("Due date crossed,fine to be paid")

				else:
					print("fine of 100 rupees")
					print("Due date crossed,fine to be paid")


			else:
				print("Returned before due date")
		else:
			print("Book currently not available")
	else:
		print("Not present in library")
# Calculate late return fine (if returned after due date).

# Display fine amount based on number of late days.