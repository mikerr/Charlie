#!/usr/bin/env python3
# pip3 install wolframclient
# sudo apt-get install wolfram-engine (free on pi)

import time
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl
# Explicit mention of kernel was needed here
session = WolframLanguageSession('/usr/bin/wolfram') 
print ("starting")

while True:
    query = input(":")
    start = time.time()
    out = session.evaluate(query)
    duration = time.time() - start

    print(out)
    print ("done in " + str(duration))

