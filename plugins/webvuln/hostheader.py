import requests


def host_header(host, port):
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print("Couldn't fetch data for the given PORT")
        return

    url = port + host
    headers = {'Host': 'http://evil.com'}
    response = requests.get(url, headers=headers)
    if 'evil.com' in response.headers:
        print("Vulnerable to Host Header Injection")
    else:
        print("Not Vulnerable to Host header injection")
