import time

def countdown(seconds):
    while seconds > 0:
        print(f'Time Left: {seconds} sec')
        time.sleep(1)
        seconds -= 1
    print('Times up')


seconds = int(input('Enter time in seconds: '))
if seconds > 0:
    countdown(seconds)
else:
    print('Time cannot be negative fool...')