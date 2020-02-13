import requests, json, threading
from random import randint

url = 'https://discordapp.com/api/v6/entitlements/gift-codes/<code>?with_application=false&with_subscription_plan=true'
def check_code():
    code = ""
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV0123456789"
    for i in range(0,23):
        code += alpha[randint(0, len(alpha) - 1)]
    r = requests.get(url.replace('<code>', code)).text
    data = json.loads(r)
    if(data["message"] == "Unknown Gift Code"):
        print("Message : " + data["message"]+"\nCode : " + code)
    elif(data["message"] == "You are being rate limited."):
        print("You're perma-ban.\nUse a proxy.")
    else:
        print("Dude wtf ? Here is your code : " + code)
        
while True:
    for i in range(10):
        threading.Thread(target=check_code).start()
