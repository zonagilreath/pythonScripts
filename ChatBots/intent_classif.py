import re

bot_template = "BOT : {0}"
user_template = "USER : {0}"

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))


keywords = {'goodbye': ['bye', 'farewell'], 
			'thankyou': ['thank', 'thx'], 
			'greet': ['hello', 'hi', 'hey']}

responses = {'goodbye': ['bye', 'farewell'], 
			'thankyou': ['thank', 'thx'], 
			'greet': ['hello', 'hi', 'hey']}

patterns = {}

for intent, keys in keywords.items():
	patterns[intent] = re.compile('|'.join(keys))

def match_intent(message):
	matched_intent = None
	for intent, pattern in patterns.items():
		if re.search(pattern, message):
			matched_intent = intent
	return matched_intent

def respond(message):
	intent = match_intent(message)
	key = 'default'
	if intent in responses:
		key = intent
	return responses[key]