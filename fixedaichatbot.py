print("Welcome to the Smart Private Library Management System chatbot!")
print("you can ask me anything or type 'exit' to end the chat.")
print("how can i assist you today?")
import datetime
import time
name=input("please enter your name:")
presenthour=datetime.datetime.now().hour
if presenthour<12:
		print("good morning!",name)
elif 12<=presenthour<18:
		print("good afternoon!",name)
else:
		print("good evening!",name)
	
responses=[
	
  {"library_status": "The library is open today from 6:00 AM to 11:00 PM.",
  "seat_and_room_availability": "Currently, 12 study seats and 1 group discussion room are available.",
  "booking_details": "Your booking for Seat 14 is confirmed from 4:00 PM to 8:00 PM today.",
  "payment_and_subscription_status": "Your monthly subscription is active and valid until 31 March.",
  "study_hours_and_entry_exit": "Today you studied for 5 hours 20 minutes. Last entry was at 10:10 AM.",
  "book issue return due dates": "You have issued 2 books. The next due date is 28 March."}


]
def get_response(userques):
	userquestion=userques.lower()
	for question in responses[0]:
		if question in userquestion:
			return responses[0][question]
		
	return "I am so sorry , I do not have the information you are Looking for . Please ask another question"

			
while True:
		userinput=input("You:")
		if userinput.lower()=='exit':
				print("chatbot:Thank you for using the smart private library management system chatbot.Goodbye!")
				break
		elif userinput.strip()=='':
				print("chatbot:please enter a valid question.")
		else:
				answer=get_response(userinput)
				print("chatbot:",answer)

		if(userinput.lower()=='exit'):
			break
