### Introduction
Welcome to this small repo designed to help the Raspberry Pi owners.
This app is just looking for first non-loopback IP address (like wlan0 or eth0) on your Pi and send it directly to your Telegram.
### Configuration
Firstly you need to create a bot token in telegram using @BotFather and paste it to the `.env` file in the project root (next to /src).
You can easily use the program right after installation of all the dependencies which are`httpx` for api requests to the Telegram API
and `python-dotenv` to extract the `BOT_TOKEN` from `.env` file.
But you always can just change the token itself in the `tg_api.py` file and even do not create any extra files.
### Docker
If you want to use it in docker as it was originally intended, then you have to install docker-engine firstly.
`Note: You have to build docker image on the directly on the Raspberry so there is going to be no any architecture mistakes.`
Then you have to build the docker image itself with:
```
sudo docker image build -t raspberry-hello:latest .
```
After that u can easily run it with:
```
sudo docker run --rm --network host raspberry-hello:latest 
```
### Systemd configuration
To make it work on Pi startup you need an already working program either it's in docker container or just a python module.
Then you need to create a systemd service that going to execute the app after the NetworkManager has been started.
Creating a file in `/etc/systemd/system/raspberry-hello.service`
Which contains the service itself:
#### Docker variant
`[Unit]
Description=Send Raspberry Pi IP to Telegram on boot
Wants=network-online.target
After=network-online.target docker.service
Requires=docker.service

[Service]
Type=oneshot
ExecStart=/usr/bin/docker run --rm --network host raspberry-hello:latest

[Install]
WantedBy=multi-user.target`
#### Python variant
`Note: for the python variant, install deps first: pip3 install httpx python-dotenv, and keep .env inside WorkingDirectory.`
`[Unit]
Description=Send Raspberry Pi IP to Telegram on boot
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/path/to/raspberry-pi-hello
ExecStart=/usr/bin/python3 /path/to/raspberry-pi-hello/src/main.py

[Install]
WantedBy=multi-user.target`

Once everything is set up you can reload daemons:
`sudo systemctl daemon-reload`
And enable the service:
`sudo systemctl enable raspberry-hello.service`
You can check if everything works perfectly with:
`sudo systemctl start --now raspberry-hello.service`
If you configured everything as described you should receive a message into Telegram.