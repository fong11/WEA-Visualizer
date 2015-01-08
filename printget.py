import webbrowser
import httplib2

import webbrowser

h = httplib2.Http()
resp, content = h.request('http://maxwell.sv.cmu.edu:8001/allalertid', 'GET')
print content

