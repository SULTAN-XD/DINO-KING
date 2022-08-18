import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
print('[•] Checking Update...')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92mCongratulations ! Your Device Support this Tools")

    import DINO
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
