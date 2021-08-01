import requests 
import http.client, urllib.request , urllib.parse , urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.parse.urlencode({
    # Request parameters
    'model-version': 'latest',
})

try:
    body = open('./imgs/image-with-faces-1.jpg',"rb").read()
    conn = http.client.HTTPSConnection('australiaeast.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v3.2/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################