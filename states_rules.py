import random

# Define the states
CONFUSE = -1
INIT = 0
MAIN = 1

# stock
CRT_PRICE = 2
HIS_PRICE = 3

# weather
QUERY_WEATHER = 4


response_group = {

    "greet": ["Hi! I am a chatbot. I can help you to check the stock price",
              "Nice to meet you. I'm a stock chatbot and I'm ready to help you.",
              ],
    "finish": ["OK. Tell me when you need more assists!",
               "Alright. I'm glad to help you!",
               ],
    "function_intro": [
        "Currently I can help you with: \n1 Get lowest/highest data\n2 Get historical data \n3 Get earnings Per Share(TTM) \n4 Get some weather information"],

    "current_price": ["The current price of {} is {}, and there are some news about {}:\n{}",
                      "{} has a real-time price of {}, and there are some news about {}:\n{}",
                      ],
    "vague_historical_data": ["Please specify which time of data you want to query.",
                              "Which time do you want to know?"
                              ],
    "analyze": ["The Earning Per Share (TTM) of {} is currently {}."],

    "query_weather":  ["Ok, Please tell me your location"],

    "specify_location": ["Ok, you are at 112.87718 degrees east longitude and 37.967819 degrees north latitude. What weather conditions do you want to know specifically?"],

    "summary": ["The weather conditions are that {}, What else do you want to know?"],

    "icon": ["The weather icon is {}, What else do you want to know?"],

    "48_temperature": ["The temperature for the next 48 hours from now is as follows:{}, What else do you want to know?"],

    "weather_plot": ["wait a sec."],

    "highest": ["The highest price is {}, What else do you want to know?"],

    "lowest": ["The lowest price is {}, What else do you want to know?"]
}


def resp_sentence(intent):
    return random.choice(response_group[intent])


policy_rules = {
    (INIT, "greet"): (MAIN, resp_sentence("greet"), None),
    (MAIN, "greet"): (MAIN, resp_sentence("greet"), None),
    (MAIN, "finish"): (MAIN, resp_sentence("finish"), None),

    (MAIN, "function_intro"): (MAIN, resp_sentence("function_intro"), None),

    (MAIN, "current_price"): (CRT_PRICE, resp_sentence("current_price"), None),
    (CRT_PRICE, "current_price"): (CRT_PRICE, resp_sentence("current_price"), None),
    (CRT_PRICE, "finish"): (MAIN, resp_sentence("finish"), None),

    (MAIN, "clear_historical_data"): (MAIN, "Here is a figure:", None),


    (MAIN, "analyze"): (MAIN, resp_sentence("analyze"), None),

    (MAIN, "query_weather"): (MAIN, resp_sentence("query_weather"), None),

    (MAIN, "specify_location"): (MAIN, resp_sentence("specify_location"), None),

    (MAIN, "summary"): (MAIN, resp_sentence("summary"), None),

    (MAIN, "icon"): (MAIN, resp_sentence("icon"), None),

    (MAIN, "48_temperature"): (MAIN, resp_sentence("48_temperature"), None),

    (MAIN, "weather_plot"): (MAIN, "Here is a figure:", None),

    (MAIN, "highest"): (MAIN, resp_sentence("highest"), None),

    (MAIN, "highest"): (MAIN, resp_sentence("highest"), None),
}
