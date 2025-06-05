from flask import Flask,request
from subprocess import getoutput as go
import json
from pprint import pprint as pp
import sys

try: PORT = sys.argv[1] 
except: PORT = 7000

app = Flask(__name__)

def get_ctrls():
    out = [o.strip() for o in go("v4l2-ctl -l").split("\n") if o.find(":")>-1]
    aa = {}
    for o in out: 
        key = o.split()[0] 
        value = o[o.find(":")+1:].strip()
        values = value.split()
        vd = {}
        for v in values: 
            try: vv = int(v.split("=")[1])
            except: vv = v.split("=")[1]
            vd[v.split("=")[0]] = vv
            aa[key] = vd

    return json.dumps(aa)

def set_ctrl(ctrl,value,debug=False):
    o = go(f"v4l2-ctl -c {ctrl}={value}")
    if debug: pp(o)
    return json.dumps({ctrl:value})

@app.route('/')
def home(): return open("index.html").read()

@app.route('/get')
def get(): return get_ctrls()

@app.route('/set')
def sets(): 
    for k in request.args.keys(): set_ctrl(k,request.args[k],debug=True)
    return(json.dumps(request.args))



app.run(host="0.0.0.0",port=PORT,debug=True)
