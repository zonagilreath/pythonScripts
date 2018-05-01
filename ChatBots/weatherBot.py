# Import the random module
import random
from weather import Weather, Unit

weather_ = Weather(unit=Unit.CELSIUS)
location = weather_.lookup_by_location('Austin')
weather = location.condition.text

name = "WeatherBot"



# a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "Here in Austin the weather is {0}".format(weather.lower()),
      "It's {0} today in Austin".format(weather.lower())
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message


print(respond(input()))