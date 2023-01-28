#! /bin/bash
#first make start sh's 
PYTHON=$(which python)
echo $PYTHON

#v4l start
echo "#!/bin/bash
$PYTHON server.py 7000" > start.sh

#now making system file

echo "[Unit]
Description=v4l2_web_ctl
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=$USER
WorkingDirectory=$PWD
ExecStart=/bin/bash $PWD/start.sh

[Install]
WantedBy=multi-user.target
" > v4l2_web_ctl.service


sudo mv v4l2_web_ctl.service /etc/systemd/system/v4l2_web_ctl.service
sudo systemctl daemon-reload
sudo systemctl enable v4l2_web_ctl
sudo systemctl start v4l2_web_ctl
