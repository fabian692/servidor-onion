# servidor-onion

sudo apt update

sudo apt install tor

sudo nano /etc/tor/torrc

HiddenServiceDir /var/lib/tor/flask_hidden_service/

HiddenServicePort 80 127.0.0.1:5000

sudo systemctl restart tor

sudo cat /var/lib/tor/flask_hidden_service/hostname
