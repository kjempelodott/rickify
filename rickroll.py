from mitmproxy import http

OGG = open('nevergonna.ogg', 'rb').read()
SIZE = str(len(OGG))

def request(flow):
    flow.response = http.HTTPResponse.make(
        200,
        OGG,
        {'Content-Type'  : 'application/octet-stream',
         'Content-Length': SIZE})
