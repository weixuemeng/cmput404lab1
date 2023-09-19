import requests
print(requests.__version__)

# sepcifu url
url = "https://raw.githubusercontent.com/weixuemeng/cmput404lab1/main/version.py" 

# Make an HTTP GET request
res = requests.get(url)

print(res)
print()