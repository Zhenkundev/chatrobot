# Chatbot_Stock&Weather
## Description
This is a python-based chatbot that can be integrated with WeChat. It can be used to query basic weather conditions and some stock information. After integrating the robot on WeChat, users can send text information to the robot for query on WeChat.
## Project process
+ Chatbot_Stock&Weather
   * chat.py ----------> Chatbot class
   * weixin.py --------> Connect with WeChat to register the robot
   * chatbot2.py -----> Use API to extract weather information from the weather website dark sky
   * chatbot5.py -----> Use API to extract stock information from stock website iexfinance
   * demo_rasa.json -> Training data
   * states_rules.py --> Configuration with state machine and reply rules
   * IMG_2160.GIF ---> Show project results in GIF format
   * .mp4 -> Display project results in video format
   
## Samples show
Go to [here](https://www.bilibili.com/video/av63839931/)
## Conversation started
1\.The user opens the weixin.py file, registers the robot, and finds information about the friends to talk to.
```
my_friend = bot.friends().search("WeChat nickname for a friend")[0]
```
2\.Run the weixin.py file
## Packages
Here are some packages that you need to download in advance for your projects
### Rasa-NLU
The recommended way to install Rasa NLU is using pip which will install the latest stable version of Rasa NLU:
```
pip install rasa_nlu
```
Rasa NLU has different components for recognizing intents and entities, most of these will have some additional dependencies.
When you train your model, Rasa NLU will check if all required dependencies are installed and tell you if any are missing.
#### For more installation information
Go to [Rasa install](https://rasa.com/docs/rasa/user-guide/installation/)
### WXPY
wxpy support Python 3.4-3.6, and 2.7 version
To ensure the package can be installed in different Python version
Replace pip in the commond below to pip3 or pip2
#### From PyPI with pip:
```
pip install -U wxpy
```
#### From douban IO PyPI source (Recommend for users in China mainland):
```
pip install -U wxpy -i "https://pypi.doubanio.com/simple/"
```
#### For more installation information
Go to [wxpy install](https://wxpy.readthedocs.io/zh/latest/#)
### iexfinance
#### From PyPI with pip (latest stable release):
```
$ pip3 install iexfinance
```
#### From development repository (dev version):
If you want to use the bleeding edge version you can get it from github:
```
$ git clone https://github.com/addisonlynch/iexfinance.git
$ cd iexfinance
$ python3 setup.py install
```
#### For more installation information
Go to [iexfiance install](https://github.com/addisonlynch/iexfinance)
### Darksky
#### Installation
```
pip3 install darksky_weather
```
#### Get started
Before you start using this library, you need to get your API key [here](https://darksky.net/dev/register)
#### For more installation information
Go to [dark sky](https://darksky.net/dev)
## Reference page
(https://pypi.org/project/iexfinance/)

(https://spacy.io/)

(https://rasa.com/docs/nlu/)

(https://github.com/youfou/wxpy)

(https://darksky.net/dev)
