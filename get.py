import webbrowser

#h = httplib2.Http()
#resp, content = h.request('http://localhost:8080/alertid?AlertID=11&PhoneID=9999', 'GET')
#print content
url = 'http://maxwell.sv.cmu.edu:8001/alertid?alertId=15&phoneId=990003461134161'
webbrowser.open_new(url)