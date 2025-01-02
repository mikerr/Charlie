#!/usr/bin/env python3

# charlie - local voice assistant 
#
# Can ask :
# "whats the time", "tell me the time"
# "whats the date"

import sounddevice, queue
import json, subprocess, datetime
import vosk

import wikipedia
#import wolframalpha

#from wolframclient.evaluation import WolframLanguageSession
#from wolframclient.language import wl

q = queue.Queue()
def callback(indata, frames, time, status):
    q.put(bytes(indata))

def read_question (sentence):

    today = datetime.datetime.now()

    if ("calculate" in sentence):
        sentence.replace("calculate","")
        wolfy = WolframLanguageSession('/usr/bin/wolfram') 
        answer = wolfy.evaluate(sentence)
        return (answer)
    if ("time" in sentence):
        now = today.strftime("%H %M")
        answer = "the time is " + now
        return answer
    if ("date" in sentence):
        now = today.strftime("%B %d")
        answer = "the date is " + now
        return answer
    try: 
        answer = wikipedia.summary(sentence, sentences = 1)
        return (answer)
    except:
        return ("I don't know that")
    return ""

def timeofday():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 : daytime = "Morning"
    if hour >= 12 : daytime = "Afternoon"
    if hour >= 18 : daytime = "Evening"
    return (daytime)

def speak(sentence):
        p = subprocess.Popen(['espeak','-a 10','--stdin'], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
        p.stdin.write(sentence.encode('utf-8'))
        p.stdin.flush()
        p.stdin.close()
        p.wait()

device_info = sounddevice.query_devices(None, "input")
samplerate = int(device_info["default_samplerate"])

#speak("Good " + timeofday()) # good morning, afternoon
stream = sounddevice.RawInputStream(samplerate=samplerate, blocksize = 8000, dtype="int16", channels=1, callback=callback)
stream.start()

vosk.SetLogLevel(-1)
model = vosk.Model(lang="en-us")
rec = vosk.KaldiRecognizer(model, samplerate)
        
print("Press ctrl-c to stop the recording")

while True:
  try:
    data = q.get()
    if rec.AcceptWaveform(data):
        jres = json.loads(rec.Result())
        question = jres["text"]
        if (question != "") :
            print(question)
            answer = read_question(question)
            if (answer !+ "") :
                 stream.stop() # stop listening while we are speaking
                 print (">>",answer)
                 speak(answer)
                 stream.start() # start listening again
  except:
    exit(0)

