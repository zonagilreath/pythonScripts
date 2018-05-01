bot_template = "BOT : {0}"
user_template = "USER : {0}"

'''A function which returns the bot message
takes string argument and concatenates to standard bot response'''
def respond(message):
	bot_response = "I can hear you! You said: " + message
	return bot_response

'''A function which prints a string as a user messages and then prints the bot response'''
def send_message(message):
	print(user_template.format(message))
	bot_response = respond(message)
	print(bot_response.format(message))


send_message(input())