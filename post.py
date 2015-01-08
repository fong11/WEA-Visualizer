import webbrowser
import httplib2

h = httplib2.Http()
#h.request('http://maxwell.sv.cmu.edu:8001/feedback', 'POST', '{"alertId":"15","PhoneID":"9999","inTarget":"1", "geolocation":[37.3232, -122.0853], "timeReceived":"1403902621", "timeAcknowledged":"1403902621", "feedback":{ "versionCode":"1", "answers":[{"question":"hii","answerCode":"Y"},{"question":"hii","answerCode":"Y"},{"question":"hii","answerCode":"Y"}], "comment":"this works"}}')
#h.request('http://maxwell.sv.cmu.edu:8001/feedback', 'POST', '{"alertId":"1","phoneId":"11","inTarget":"1", "geolocation":[25.3332, -122.0853], "timeReceived":"1403902621", "timeAcknowledged":"1403902621", "feedback":{ "versionCode":"1", "answers":[{"question":"hii","answerCode":"Y"},{"question":"hii","answerCode":"Y"},{"question":"hii","answerCode":"Y"}], "comment":"this works"}}')
h.request('http://10.215.4.30:8001/feedback', 'POST', '{"alertId":"1","phoneId":"11","inTarget":"1", "geolocation":[25.3332, -122.0853], "timeReceived":"1403902621", "timeAcknowledged":"1403902621", "feedback":{ "versionCode":"1", "answers":[{"question":"hii","answerCode":"Y"},{"question":"hii","answerCode":"Y"},{"question":"hii","answerCode":"Y"}], "comment":"this works"}}')
#'http://maxwell.sv.cmu.edu:8000/add'
#'{"AlertID":"01", "PhoneID":"9999", "Geolocation":"xx", "AbstractLoc":"abs", "TimeReceived":"00:00", "TimeAck":"11:11", "FeedBack":"Need real stuff later"}