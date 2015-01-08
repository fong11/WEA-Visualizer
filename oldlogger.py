import web
import json
import HTML
import gviz_api
import datetime
import gspread
#https://developers.google.com/chart/interactive/docs/gallery/map
urls = (
    '/alertid', 'alertid',
    '/viewquestions', 'viewquestions',
    '/inputcrossmobile', 'inputcrossmobile',
    '/testalertid', 'testalertid',
    '/allalertid', 'allalertid',
    '/feedback', 'feedback',
    '/table', 'table',
    '/polygon', 'polygon',
    '/favicon.ico', 'icon'
)
def keydne(key, arr):
    if key in arr.keys():
         #these are opposite just for the use of this function above
        return False
    else:
        return True 
# Process favicon.ico requests
class icon:
    def GET(self): raise web.seeother("/static/favicon.ico")
# AND PhoneID = blah["PhoneID"]
class alertid:
    def GET(self):
        db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
        user_data = web.input()
        #web.header('Content-Type', 'application/json')
        #blah = json.loads(user_data)
        #results = db.select('data', where="AlertID =" +user_data['hi'])
        
        m = db.query("SELECT * FROM data WHERE (alertId = "+user_data['alertId']+" AND phoneId = "+user_data['phoneId']+")")
        #new = m[0]
        t = HTML.Table(header_row=['alertId', 'phoneId', 'geolocation', 'abstractLocation', 'timeReceived', 'timeAcknowledged', 'version', 'answers', 'comment', 'inTarget'])

        for new in m:
            readtr = str(datetime.datetime.fromtimestamp(int(new.timeReceived)).strftime('%Y-%m-%d %H:%M:%S'))
            readta = str(datetime.datetime.fromtimestamp(int(new.timeAcknowledged)).strftime('%Y-%m-%d %H:%M:%S'))
            
            t.rows.append([new.alertId, new.phoneId, new.geolocation, new.abstractLocation, readtr, readta, new.version, new.answers, new.comment, inTarget])
        htmlcode = str(t)
            #print htmlcode
        return htmlcode#new#("AlertID: "+new.AlertID +" "+ "PhoneID: "+new.PhoneID) 
class testalertid:
    def GET(self):
        db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
        user_data = web.input()
        #web.header('Content-Type', 'application/json')
        #blah = json.loads(user_data)
        #results = db.select('data', where="AlertID =" +user_data['hi'])
        
        m = db.query("SELECT * FROM data")
        #new = m[0]
        t = HTML.Table(header_row=['alertId', 'phoneId', 'geolocation', 'abstractLocation', 'timeReceived', 'timeAcknowledged', 'version', 'answers', 'comment', 'inTarget'])

        for new in m:
            readtr = str(datetime.datetime.fromtimestamp(int(new.timeReceived)).strftime('%Y-%m-%d %H:%M:%S'))
            readta = str(datetime.datetime.fromtimestamp(int(new.timeAcknowledged)).strftime('%Y-%m-%d %H:%M:%S'))
            #print readtr
            #print readta
            #encodedanswer = new.answers.encode('utf-8')
            #print encodedanswer
            #answerdata = json.loads(encodedanswer)
            #print answerdata["question"]
            t.rows.append([new.alertId, new.phoneId, new.geolocation, new.abstractLocation, readtr, readta, new.version, new.answers, new.comment, new.inTarget])
        htmlcode = str(t)
            #print htmlcode
        return htmlcode#new#("AlertID: "+new.AlertID +" "+ "PhoneID: "+new.PhoneID)
class viewquestions:
    def GET(self):
        db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
        user_data = web.input()
        #web.header('Content-Type', 'application/json')
        #blah = json.loads(user_data)
        #results = db.select('data', where="AlertID =" +user_data['hi'])
        
        m = db.query("SELECT * FROM data")
        #new = m[0]
        t = HTML.Table(header_row=['alertId', 'phoneId', 'question1', 'answer1', 'question2', 'answer2', 'question3', 'answer3',
         'question4', 'answer4', 'question5', 'answer5', 'question6', 'answer6', 'question7', 'answer7',
         'question8', 'answer8', 'question9', 'answer9', 'question10', 'answer10'])

        for new in m:
            readtr = str(datetime.datetime.fromtimestamp(int(new.timeReceived)).strftime('%Y-%m-%d %H:%M:%S'))
            readta = str(datetime.datetime.fromtimestamp(int(new.timeAcknowledged)).strftime('%Y-%m-%d %H:%M:%S'))
            #print readtr
            #print readta
            #encodedanswer = new.answers.encode('utf-8')
            #print encodedanswer
            #answerdata = json.loads(encodedanswer)
            #print answerdata["question"]
            t.rows.append([new.alertId, new.phoneId, 
              new.question1, new.answer1, new.question2, new.answer2, new.question3, new.answer3,
              new.question4, new.answer4, new.question5, new.answer5, new.question6, new.answer6,
              new.question7, new.answer7, new.question8, new.answer8, new.question9, new.answer9,
              new.question10, new.answer10])
        htmlcode = str(t)
            #print htmlcode
        return htmlcode#new#("AlertID: "+new.AlertID +" "+ "PhoneID: "+new.PhoneID)
class allalertid:
    def GET(self):
        db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
        user_data = web.input()
        #web.header('Content-Type', 'application/json')
        #blah = json.loads(user_data)
        #results = db.select('data', where="AlertID =" +user_data['hi'])
        
        m = db.query("SELECT * FROM data")
        #new = m[0]
        t = HTML.Table(header_row=['alertId',   'phoneId'])
        for new in m:   
            t.rows.append([new.alertId,      new.phoneId])
        htmlcode = str(t)
            #print htmlcode
        return htmlcode#new#("AlertID: "+new.AlertID +" "+ "PhoneID: "+new.PhoneID) 
class feedback:

    def POST(self):
        db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
        user_data = web.data()
        #print user_data
        web.header('Content-Type', 'application/json')
        keys = ['alertId', 'phoneId', 'geolocation', 'abstractLocation', 'timeReceived', 'timeAcknowledged', 'inTarget']
        questionkey = ['question']
        answerkey = ['answerCode']
        finalentry = []
        entry = json.loads(user_data)

        numQuestions = 0
        feedbackExists = 0
        #checks to see if each entry exists, if not replace with "Not Known"
        for x in keys:
            if keydne(x, entry):
                entry[x] = 'Not Known'
        if keydne("feedback", entry):
            entry["feedback"] = {}
            entry["feedback"]["versionCode"] = '0'
            entry["feedback"]["comment"] = 'Not Known'
            entry["feedback"]["answers"] = []
        else:
            feedbackExists = 1
        originalSize = len(entry["feedback"]["answers"])
        #print len(entry)
        for y in range(1,11):
            #print str(entry["feedback"]["answers"][0]["question"])
            if originalSize < y:
           # if keydne('question', entry["feedback"]["answers"][y-1]):
                entry["feedback"]["answers"].append({"question":'Not Known',"answerCode":'Not Known'})
                #entry["feedback"]["answers"][y][
            else:
                numQuestions += 1
        #print feedbackExists
       #print feedbackExists
        n = db.insert('data', alertId=entry["alertId"], phoneId= entry["phoneId"], geolocation=(str(entry["geolocation"][0])+","+str(entry["geolocation"][1])),
         abstractLocation=str(entry["abstractLocation"]), timeReceived=entry["timeReceived"], timeAcknowledged=entry["timeAcknowledged"], version=entry["feedback"]["versionCode"], 
         answers=str(entry["feedback"]["answers"]), comment=entry["feedback"]["comment"], inTarget=entry["inTarget"],
         question1 =  entry["feedback"]["answers"][0]["question"],question2 =  entry["feedback"]["answers"][1]["question"],question3 =  entry["feedback"]["answers"][2]["question"],
         question4 =  entry["feedback"]["answers"][3]["question"],question5 =  entry["feedback"]["answers"][4]["question"],question6 =  entry["feedback"]["answers"][5]["question"],
         question7 =  entry["feedback"]["answers"][6]["question"],question8 =  entry["feedback"]["answers"][7]["question"],question9 =  entry["feedback"]["answers"][8]["question"],
         question10 =  entry["feedback"]["answers"][9]["question"], feedbackExists = feedbackExists, numQuestions = numQuestions,
         answer1 =  entry["feedback"]["answers"][0]["answerCode"],answer2 =  entry["feedback"]["answers"][1]["answerCode"],answer3 =  entry["feedback"]["answers"][2]["answerCode"],
         answer4 =  entry["feedback"]["answers"][3]["answerCode"],answer5 =  entry["feedback"]["answers"][4]["answerCode"],answer6 =  entry["feedback"]["answers"][5]["answerCode"],
         answer7 =  entry["feedback"]["answers"][6]["answerCode"],answer8 =  entry["feedback"]["answers"][7]["answerCode"],answer9 =  entry["feedback"]["answers"][8]["answerCode"],
         answer10 =  entry["feedback"]["answers"][9]["answerCode"],
         )
        return "success!"

page_template = """
<!DOCTYPE html>
<html>
  <script src="https://www.google.com/jsapi" type="text/javascript"></script>
  <script>
    google.load('visualization', '1', {packages:['table']});

    google.setOnLoadCallback(drawTable);
    function drawTable() {

      var json_table = new google.visualization.Table(document.getElementById('table_div_json'));
      var json_data = new google.visualization.DataTable(%(jsontwo)s, 0.6);
      json_table.draw(json_data, {});
    }
  </script>
  <body>
    
    <div id="table_div_json"></div>
  </body>
</html>
"""
#<H1>Table created using ToJSon</H1>
chart_template = """
<html>
  <head>
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  <script>
    google.load('visualization', '1', { 'packages': ['map'] });
    google.setOnLoadCallback(drawMap);

    function drawMap() {

    var options = { showTip: true, enableScrollWheel: true, mapType: "normal", useMapTypeControl: true,
          icons: {
            default: {
              normal: 'http://mt.google.com/vt/icon?color=ff004C13&name=icons/spotlight/spotlight-waypoint-a.png',
              selected: 'http://mt.google.com/vt/icon?color=ff004C13&name=icons/spotlight/spotlight-waypoint-b.png'
            }
          }
    };

    var map = new google.visualization.Map(document.getElementById('chart_div'));
    var json_data = new google.visualization.DataTable(%(json)s, 0.6);
    map.draw(json_data, options);
  };
  </script>
  </head>
  <body>
    <div id="chart_div"></div>
  </body>
</html>
"""

class table:
    def GET(self):
        db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
        user_data = web.input()
        #web.header('Content-Type', 'application/json')
        #blah = json.loads(user_data)
        #results = db.select('data', where="AlertID =" +user_data['hi'])
        
        m = db.query("SELECT * FROM data")
        #new = m[0]

       # t = HTML.Table(header_row=['alertId',   'phoneId'])  



        descriptiontwo = {"alertId": ("number", "alertId"),
                     "phoneId": ("number", "phoneId")}
        datatwo = [{"alertId": 0, "phoneId": 0}]
        for new in m:
            datatwo.append({"alertId":int(new.alertId), "phoneId":int(new.phoneId)})


        data_tabletwo = gviz_api.DataTable(descriptiontwo)
        data_tabletwo.LoadData(datatwo)

        jsontwo = data_tabletwo.ToJSon(columns_order=("alertId", "phoneId"),
                               order_by="alertId")

        # Putting the JS code and JSon string into the template
        #print "Content-type: text/html"
        #print chart_template % vars()
        return page_template % vars()
        
        #return chartt_template
#    <meta http-equiv="refresh" content="5">
polygon_template = """
<!DOCTYPE html>
<html>
  <head>   
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <style type="text/css">
      html { height: 100%% }
      body { height: 100%%; margin: 0; padding: 0 }
      #map-canvas { height: 100%% }
      #legend {
        font-family: Arial, sans-serif;
        background: #fff;
        padding: 10px;
        margin: 10px;
        border: 3px solid #000;
      }
      #legend h3 {
        margin-top: 0;
      }
      #legend img {
        vertical-align: middle;
      }
    </style>
    <script type="text/javascript"
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDcbJ4NJyaFF8sYJgY__J90b4dVwFqTtn8">
    </script>
    <script type="text/javascript">
var alertpolygon = {};
%(polygondata)s
var alertCreator;
function initialize() {

  %(dataone)s
  var mapOptions = {
    zoom: 10,
    center: alertpolygon['test'].center
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  %(content)s
  var icons = {
    noFeedback: {
      name: 'In target, no feedback',
      icon: 'http://mt.google.com/vt/icon?color=ff004C13&name=icons/spotlight/spotlight-waypoint-a.png'
    },
    yesFeedback: {
      name: 'In target, with feedback',
      icon: 'http://mt.google.com/vt/icon?psize=30&font=fonts/arialuni_t.ttf&color=ff304C13&name=icons/spotlight/spotlight-waypoint-a.png&ax=43&ay=48&text=%%E2%%80%%A2'
    },
    noTarget: {
      name: 'Not in target',
      icon: 'http://mt.google.com/vt/icon?color=ff004C13&name=icons/spotlight/spotlight-waypoint-b.png'
    },
    noAlert: {
      name: 'Not in scope',
      icon: 'http://mt.google.com/vt/icon?color=ff004C13&name=icons/spotlight/spotlight-waypoint-blue.png'
    }
  };
  var noFeedback = 'http://mt.google.com/vt/icon?color=ff004C13&name=icons/spotlight/spotlight-waypoint-a.png';
  var yesFeedback = 'http://mt.google.com/vt/icon?psize=30&font=fonts/arialuni_t.ttf&color=ff304C13&name=icons/spotlight/spotlight-waypoint-a.png&ax=43&ay=48&text=%%E2%%80%%A2';
  var noTarget = 'http://mt.google.com/vt/icon?color=ff004C13&name=icons/spotlight/spotlight-waypoint-b.png';
  var noAlert = 'http://mt.google.com/vt/icon?color=ff004C13&name=icons/spotlight/spotlight-waypoint-blue.png';
  %(datatwo)s
%(polygoncoords)s

%(polygondatatwo)s

  %(listener)s
  var legend = document.getElementById('legend');
  for (var key in icons) {
    var type = icons[key];
    var name = type.name;
    var icon = type.icon;
    var div = document.createElement('div');
    div.innerHTML = '<img src="' + icon + '"> ' + name;
    legend.appendChild(div);
  }

  map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);
}

google.maps.event.addDomListener(window, 'load', initialize);
  </script>  
  </head>
  <body>
    <div id="map-canvas"></div>
    <div id="legend"><h3>Legend</h3></div>
  </body>

</html>
"""
class inputcrossmobile:
    def POST(self):

      db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
      user_data = web.input()
      #results = db.select('data', where="AlertID =" +user_data['hi'])
      entry = json.loads(user_data)    

      #CHANGE THESE DEPENDING ON WHAT ERVIN RETURNS
      keys = ['phoneId', 'geolocation']

      #m = db.query("SELECT alertId, phoneId FROM data")
      for new in entry:
          for x in keys:
              if keydne(x, new):
                  entry[x] = 'Not Known'
          m = db.query("INSERT INTO crossmobile (alertId, phoneId, geolocation) VALUES (-99, " + entry['phoneId'] + ", " + entry['geolocation'] + 
            "ON DUPLICATE KEY UPDATE geolocation=VALUES("+entry['geolocation']+")")


class polygon:
    def GET(self):
        db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
        user_data = web.input()
        #web.header('Content-Type', 'application/json')
        #blah = json.loads(user_data)
        #results = db.select('data', where="AlertID =" +user_data['hi'])
        try:
          oldalert
        except NameError:
          oldalert = ""
        #m = db.query("SELECT * FROM data WHERE (alertId = "+user_data['alertId']+")")
        m = db.query("SELECT * FROM data")
        print m
        newalert = "1"
      #  print oldalert
       # print newalert
        if(oldalert != newalert):
          polygondata = ""
          polygondatatwo = ""
          polygoncoords = ""
          polygoncenter = [0,0]
  #SETTING UP THE POLYGON
          gc = gspread.login('ieacmusv@gmail.com', 'iea@cmusv')

          worksheet = gc.open("Orchestrator").sheet1

          values_list = worksheet.col_values(1)
          #eventually need to change 30 into alertid that is specified as input! need to implement this
          alertrow = values_list.index("1") + 1

          polygon = worksheet.acell("S"+str(alertrow)).value
          splitpolygon = polygon.split(',')
          alerttype = worksheet.acell("L"+str(alertrow)).value
          polygonType = worksheet.acell("R"+str(alertrow)).value
          print polygonType
          if (str(polygonType).lower() == "circle"):

            polygondata += """
alertpolygon['test'] = {
  center: new google.maps.LatLng(""" + str(float(splitpolygon[0]))+ "," + str(float(splitpolygon[1])) + """),
  alertradius: """ + str(float(splitpolygon[2])) + """
};
"""
            polygondatatwo += """
  for (var alert in alertpolygon) {
    var polygonOptions = {
      strokeColor: '#FF0000',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillOpacity: 0.0,
      map: map,
      center: alertpolygon[alert].center,
      radius: alertpolygon[alert].alertradius * 1000
    };
    // Add the circle for this city to the map.
    alertCreator = new google.maps.Circle(polygonOptions);
  }
"""
          else:

            polygoncoords += """
var coords = ["""
            for geos in range((len(splitpolygon)-2)/2):
              print splitpolygon[geos*2-1] + "hi"
              polygoncenter[0]+=float(splitpolygon[geos*2])
              polygoncenter[1]+=float(splitpolygon[geos*2+1])
              if geos != ((len(splitpolygon)-2)/2)-1:
                polygoncoords += """
  new google.maps.LatLng(""" + str(float(splitpolygon[geos*2]))+ "," + str(float(splitpolygon[geos*2+1])) + """),"""
              else:
                polygoncoords += """
  new google.maps.LatLng(""" + str(float(splitpolygon[geos*2]))+ "," + str(float(splitpolygon[geos*2+1])) +""")"""
            polygoncoords+= """
];
"""
            polygoncenter[0] = polygoncenter[0]/((len(splitpolygon)-2)/2)
            polygoncenter[1] = polygoncenter[1]/((len(splitpolygon)-2)/2)
            polygondata +="""
alertpolygon['test'] = {
  center: new google.maps.LatLng(""" + str(polygoncenter[0])+ "," + str(polygoncenter[1]) + """),
};
"""
            polygondatatwo+="""
  newPolygon = new google.maps.Polygon({
    paths: coords,
    strokeColor: '#FF0000',
    strokeOpacity: 0.8,
    strokeWeight: 3,
    fillColor: '#FF0000',
    fillOpacity: 0.35
  });

  newPolygon.setMap(map);
"""
          response = worksheet.acell("O"+str(alertrow)).value
        dataone = ""
        datatwo = ""
        centerlat = 0
        centerlong = 0
        counter = 0
        markerIcon = ""
        listener = ""
        content = ""
        currentPhoneIds = []
        #icons : noFeedback, yesFeedback, and noTarget
        for new in m:
            if(int(new.inTarget) == 0):
                markerIcon = "noTarget"
            elif(int(new.feedbackExists) == 0):
                markerIcon = "noFeedback"
            else:
                markerIcon = "yesFeedback"
            split = new.geolocation.split(',')
            dataone+= """
var myLatlng""" + str(counter) + """ = new google.maps.LatLng(""" + str(float(split[0])) + ", " + str(float(split[1])) + """);
"""
            datatwo+= """
var marker""" + str(counter) + """ = new google.maps.Marker({
  position: myLatlng""" + str(counter) + """,
  map: map, 
  icon:""" + markerIcon + """,
  title: """ + """'Hello World!'""" + """
});
"""
            content +="""
  var contentString"""+str(counter)+""" = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">"""+ str(alerttype) +" Alert"+ """</h1>'+
      '<div id="bodyContent">'+
      '<p style="font-size:90%"><b>PhoneId:</b> """+str(new.phoneId)+"""'+
      '</p>'+
      '<p><b>Response:</b> """+str(response)+"""'+
      '</p>'+
"""
            for z in range(1,int(new.numQuestions)+1):
                content +="""
      '<p><b>Question:</b> """+str(eval("new.question"+str(z)))+"""<br>'+
      '<b>Answer:</b> """+str(eval("new.answer"+str(z)))+"""</p>'+
"""
            content +="""
      '</div>'+
      '</div>';

  var infowindow"""+ str(counter) + """ = new google.maps.InfoWindow({
      content: contentString""" + str(counter) + """
  });
"""
            listener+="""
  google.maps.event.addListener(marker"""+ str(counter) + """, 'click', function() {
                  if(!marker"""+ str(counter) + """.open){
                      infowindow"""+ str(counter) + """.open(map,marker"""+ str(counter) + """);
                      marker"""+ str(counter) + """.open = true;
                  }
                  else{
                      infowindow"""+ str(counter) + """.close();
                      marker"""+ str(counter) + """.open = false;
                  }
                  google.maps.event.addListener(map, 'click', function() {
                      infowindow"""+ str(counter) + """.close();
                      marker"""+ str(counter) + """.open = false;
                  });
              });
"""
            #this is the counter to make each item unique
            counter +=1
            #list for ervin's server
            #currPhoneIds.extend(str(new.phoneId))
        #crossmobile = db.query("SELECT")
        oldalert = newalert
        return (polygon_template % vars())
        
        #return chartt_template
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()