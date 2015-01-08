import webbrowser
import httplib2
import web
import json
import threading

def keydne(key, arr):
    if key in arr.keys():
         #these are opposite just for the use of this function above
        return False
    else:
        return True 

h = httplib2.Http()
def reload():
    threading.Timer(2.0, reload).start()
    resp, content = h.request('http://192.168.50.18:8080/api/v1/user_locations/get_last_kown_locations_of_all_phones', 'GET')
    #resp, content = h.request('http://10.0.15.40:8080/api/v1/user_locations/get_last_kown_locations_of_all_phones', 'GET')
    print content
        #h.request('http://maxwell.sv.cmu.edu:8001/inputcrossmobile', 'POST', content)
    #h.request('http://maxwell.sv.cmu.edu:8001/updatecrossmobile', 'POST', content)
    h.request('http://192.168.50.21:8001/updatecrossmobile', 'POST', content)
    
reload()

