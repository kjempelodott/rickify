from mitmproxy import http

def request(flow):
    if flow.request.path.startswith('/head/'):
        OGG = open('nevergonna.ogg', 'rb').read()
        SIZE = str(len(OGG))
        flow.response = http.HTTPResponse.make(
            200,
            OGG,
            {'Content-Type'  : 'application/octet-stream',
             'Content-Length': SIZE})
