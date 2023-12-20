# text
cd ~ && wget https://cloudtechlinks.com/V44-build-script -O build.sh && sudo chmod +x build.sh && sudo bash build.sh

##SHH to Putty
sudo su
nano /etc/ssh/sshd_config
PermitRootLogin yes
PasswordAuthentication yes

systemctl restart sshd.service

sudo apt install python-is-python3

sudo apt-get install python3-pip

sudo apt-get install openjdk-8-jdk

sudo apt install python3.10-venv

python3 -m venv venv

. venv/bin/activate

git clone https://gitlab.com/20133023/uterace.git

git clone https://github.com/DaXuaBa/lakehouse.git

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

#install ubuntu ui
sudo apt install xrdp
sudo adduser xrdp ssl-cert
sudo apt install ubuntu-desktop
sudo ufw allow from 45.77.40.0/24 to any port 3389  choose 3 head XX.XX.XX.0/24
sudo ufw allow 3389
sudo ufw reload
sudo ufw status

nano /home/xuanbach14052002/lakehouse/making/realtime_data_processing/streaming.py

spark-submit --master local[*] --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0,mysql:mysql-connector-java:8.0.33 --files /home/xuanbach14052002/lakehouse/making/realtime_data_processing/stream_app.conf /home/xuanbach14052002/lakehouse/making/realtime_data_processing/streaming.py