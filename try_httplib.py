import httplib

conn = httplib.HTTPConnection("127.0.0.1:5000")
conn.request('get', '/api/dfadfkeqw/')
response = conn.getresponse()
content = response.read()
import pdb; pdb.set_trace()