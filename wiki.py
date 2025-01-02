import wikipedia

while True:
    query = input()
    try: 
        results = wikipedia.summary(query, sentences = 1)
        print(results)
    except:
        print ("sorry I don't know that")
