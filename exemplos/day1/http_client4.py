import httpx

response = httpx.get('http://example.com/index.html')    
print(response)
print("*" * 50)
print(response.status_code)     
print("*" * 50)
print(response.headers)
print("*" * 50)
print(response.content)