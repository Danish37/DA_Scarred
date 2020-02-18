import requests
url = "http://172.17.50.43/algenius"
r = requests.get(url)
#print(r.text)
print("Status code: OK")
print("\t *",r.status_code)
h = requests.head(url)
print("Header: \n ********")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("********")

url2 = "http://172.17.50.43/headers.php"
headers = {
    'User-Agent':'Mobile'
}
r2 = requests.get(url2,headers = headers)
print(r2.text)