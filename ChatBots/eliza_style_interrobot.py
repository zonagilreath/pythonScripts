import re
import random

rules = {'do you think (.*)': ['if {0}? Absolutely.', 
								'No chance'], 
		'if (.*)': ["Do you really think it's likely that {0}", 
					'Do you wish that {0}', 
					'What do you think about {0}', 
					'Really--if {0}'], 
		'do you remember (.*)': ['Did you think I would forget {0}', 
					"Why haven't you been able to forget {0}", 
					'What about {0}', 'Yes .. and?'], 
		'I want (.*)': ['What would it mean if you got {0}', 
					'Why do you want {0}', 
					"What's stopping you from getting {0}"]}

def match_rules(rules, message):
	response, phrase = "default", None
	for pattern, responses in rules.items():
		match = re.search(pattern, message)
		if match is not None:
			response = random.choice(responses)
			if '{0}' in response:
				phrase = match.group(1)
			return response

def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'me', message)
    return message
