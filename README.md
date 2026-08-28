### Introduction
Welcome to this small repo designeg to help the Raspberry Pi owners.
This app is just looking for wlan0 ip address on your's Pi and send it directly to your Telegram.
### Configuration
So firstly you need to create a bot token in telegram using @BotFather and paste it to the `.env` file near the /src directory.
You can easily use the programm right after installation of all the depencies which are `httpx` and `python-dotenv` to extract the `BOT_TOKEN` from  `.env` file. 
But you always can just change the token itself in the `tg_api.py` file and even do not create any extra files.
### Docker
If you want to use it in docker as it was originally intended, then you have to install docker-engine firstly. 
Then you have to build the docker image itself with:
```
docker image build -t raspberry-hello:latest .
```
After that u can easily run it with:
```
docker run --rm --network host raspberry-hello:latest 
```
### Systemd configuration
s
