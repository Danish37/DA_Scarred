import requests
url = "http://172.17.50.43/algenius"
r = requests.get(url)
#print(r.text)
print("Status code:")
print("\t *",'OK')
h = requests.head(url)
print("Header: \n ********")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("********")

url2 = "http://httpbin.org/headers"
headers = {
    'User-Agent':'Mobile'
}
r2 = requests.get(url2,headers = headers)
print(r2.text)