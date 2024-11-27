from urllib.request import urlopen

response = urlopen('http://example.com/index.html')

print(response)
print("*" * 50)
print(response.read())