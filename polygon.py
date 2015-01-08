import webbrowser
import threading

#h = httplib2.Http()
#resp, content = h.request('http://localhost:8080/alertid?AlertID=11&PhoneID=9999', 'GET')
#print content
url = 'http://maxwell.sv.cmu.edu:8001/polygon?alertId=1'

#def printit():
#	threading.Timer(5.0, printit).start()
webbrowser.open(url, new=0, autoraise= True)

#printit()