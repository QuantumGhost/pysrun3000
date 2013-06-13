import requests


host = 'auth.example.com'   # Authenticatioon Server 


def get_mac():
    from uuid import uuid1
	mac = uuid1().hex[-12:]
	mac = list(mac)
	for i in range(10, 0, -2):
		mac.insert(i, ':')
	return ''.join(mac)


def login(host, username, password):
	params = {
		'n': '100', 'is_pad': '1', 'type': '1',
		'uname': username, 'pass': password, 'drop': '0',
		'x': '98', 'y': '24', 'mac': get_mac()
	}
	r = requests.post(
		'http://{}/cgi-bin/do_login'.format(host), params)
	print(r.text)


def logout(host, uid):
	params = {
		'uid': uid
	}
	r = requests.post('http://{}/cgi-bin/do_logout'.format(host), params)


uid = login(host, 'username', 'password')
# logout(host, uid)
