#!/usr/bin/env python3
import wikipedia

while True:
    query = input(":")
    try: 
        results = wikipedia.summary(query, sentences = 1)
        print(results)
    except:
        try: # try again 
            results = wikipedia.summary(query, sentences = 1,features="html.parser")
            print(results)
        except:
            try: 
                results = wikipedia.summary("what " + query, sentences = 1)
                print(results)
            except:
                print ("sorry I don't know that")
