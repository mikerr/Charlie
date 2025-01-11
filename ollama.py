#!/usr/bin/env python3

import subprocess

sentence = "ummerize in once sentence: when was jaguar e type first released"

p = subprocess.Popen('ollama run qwen2.5:3b', stdin=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True )
p.stdin.write(sentence.encode('utf-8'))
p.stdin.flush()
p.stdin.close()
p.wait()


