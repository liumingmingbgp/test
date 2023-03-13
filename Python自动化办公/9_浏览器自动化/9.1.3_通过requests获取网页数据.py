import requests

url = 'https://www.baidu.com/'
r = requests.get(url)
# print(r.status_code)
# print(r.text)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
r = requests.get(url, headers=headers)
with open('9_浏览器自动化/baidu.html', 'w') as f:
    f.write(r.text)


url = 'http://httpbin.org/post'
data = {
    'username':'二两',
    'password':'123456'
}
r = requests.post(url, data = data)
print(r.text)