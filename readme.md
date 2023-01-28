# v4l2_web_ctl

This is a simple python/flask app to control `v4l2-ctl`. If you're here you know what this is for.

- The homepage provides sliders automagically
- `/get` dumps a json state parsed from `v4l2-ctl -C`
- `/set?CTL=VAL` sets the `VAL` for the `CTL` with `v4l2-ctl -c CTL=VAL`

## Reqs

flask, so `python -m pip install flask`

## To start

- `python server.py PORT`
    - if no port, we're going to `7000`

## To use

Go to `http://your_up:PORT`

## To install service

`bash install_systemd.sh` , and it will run on `port 7000` we say otherwise per above (change in `start.sh`) 
