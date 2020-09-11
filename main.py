import requests
import threading
from http.cookiejar import MozillaCookieJar

total_count = 1
threads_count = int(input("How many threas would you like to run on?"))
def main(threadname):
    global total_count
    url = "https://oceanhero.today/web?q=test"
    cj = MozillaCookieJar('cookies.txt')
    cj.load(ignore_expires=True)
    while True:
        try:
            requests.get(url, cookies=cj)
            print(f"<{threadname}> {total_count}")
            total_count += 1
        except:
            print("There was an error peforming the request")

threads = list()
for index in range(threads_count):
    thread = threading.Thread( target=main, args=(f"Thread{index+1}",))
    threads.append(thread)
    thread.start()
