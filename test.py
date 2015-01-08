    <button id="resetpoly">RESET POLYGON</button>
 $("#resetpoly").click(function(){
    url = 'http://maxwell.sv.cmu.edu:8001/resetpolygon?alertId=%(urlAlertId)s';
    //url = 'markers?alertId=1';

    $.get(url,function(data,status) {
        //console.log(data);

        
        eval(data);

        },'html'); 
  });














class markers:
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
        #m = db.query("SELECT * FROM data WHERE alertId <> -99")
        m = db.query("SELECT * FROM data WHERE (alertId = "+user_data['alertId']+")")
        #print m
        newalert = str(user_data['alertId'])
      #  print oldalert
       # print newalert
        alerttype = "alert"
        response = "response"
        dataone = ""
        datatwo = ""
        centerlat = 0
        centerlong = 0
        counter = 0
        noMarkers = 0
        markerIcon = ""
        listener = ""
        content = ""
        currPhoneIds = []
        #icons : noFeedback, yesFeedback, and noTarget
        for new in m:
            if(int(new.reset) == 1 and int(new.isWEAPlus) == 1):
                markerIcon = "isWEAPlus"
                noMarkers = True;
            elif(int(new.reset) == 1):
                markerIcon = "noAlert"
                noMarkers = True;
            elif(int(new.inTarget) == 0):
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
//if(markers["""+ str(counter) + """]){
//markers["""+ str(counter) + """].setMap(null);
//markers["""+ str(counter) + """]= null;
//}
var marker""" + str(counter) + """ = new google.maps.Marker({
  position: myLatlng""" + str(counter) + """,
  map: map, 
  icon:""" + markerIcon + """,
  title: '""" + str(new.crossId) + """'
});
"""
            content +="""
  var contentString"""+str(counter)+""" = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">"""+ str(new.alerttype) +" Alert"+ """</h1>'+
      '<div id="bodyContent">'+
      '<p><b>PhoneId:</b> """+str(new.phoneId)+"""'+
      '</p>'+
      '<p><b>Phone Number:</b> """+str(new.crossId)+"""'+
      '</p>'+
      '<p><b>Response:</b> """+str(new.response)+"""'+
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
            currPhoneIds.append(str(new.phoneId))
        #print len(currPhoneIds)
        #needs input
        if len(currPhoneIds) != 0:
          query = "SELECT * FROM data WHERE alertId = -99 AND ("
          for uniquePhoneId in range(len(currPhoneIds)):
            if (uniquePhoneId + 1) != len(currPhoneIds):
              query+="phoneId <> " + str(currPhoneIds[uniquePhoneId]) +" AND "
            else:
              query+="phoneId <> " + str(currPhoneIds[uniquePhoneId])
          query += ")"
          #print query
        else:
          query = "SELECT * FROM data WHERE alertid = -99"

        crossmobile = db.query(query)

        #countertwo = 0
        for entries in crossmobile:
          splitblue = entries.geolocation.split(',')
          markerIcon = "noAlert"
          dataone+= """
  var myLatlng""" + str(counter) + """ = new google.maps.LatLng(""" + str(float(splitblue[0])) + ", " + str(float(splitblue[1])) + """);
  """
          datatwo+= """
//if(markers["""+ str(counter) + """]){
//markers["""+ str(counter) + """].setMap(null);
//markers["""+ str(counter) + """]= null;
//}
  var marker""" + str(counter) + """ = new google.maps.Marker({
    position: myLatlng""" + str(counter) + """,
    map: map, 
    icon:""" + markerIcon + """,
    title: '""" + str(entries.crossId) + """'
  });
  """
          counter +=1
        oldalert = newalert
        markerarray = ""
        for each in range(counter):
          markerarray += """
markers.push(marker""" + str(each) + """); """
        dataone = dataone.replace('"', '\\"')
        content = content.replace('"', '\\"')
        datatwo = datatwo.replace('"', '\\"')
        listener = listener.replace('"', '\\"')
        removemarkers = """
for (var i = 0; i < markers.length; i++ ) {
  markers[i].setMap(null);
  markers[i] = null;
}
markers.length = 0;
markers = [];"""
        finalmarkers = removemarkers + dataone + content + datatwo + listener +markerarray
        return finalmarkers







class resetpolygon:
    def GET(self):
        db = web.database(dbn='mysql', user='root', pw='12345', db='responses')
        user_data = web.input()
        global oldalert
        global newalert
        #web.header('Content-Type', 'application/json')
        #blah = json.loads(user_data)
        #results = db.select('data', where="AlertID =" +user_data['hi'])]
        noMarkers = False;
        polygondata = ""
        polygondatatwo = ""
        polygoncoords = ""
        m = db.query("SELECT * FROM data WHERE (alertId = "+user_data['alertId']+")")
        for new in m:
            if(int(new.reset) == 1 and int(new.isWEAPlus) == 1):
                noMarkers = True;
            elif(int(new.reset) == 1):
                noMarkers = True;
            elif(int(new.inTarget) == 0):
                noMarkers = False;
            elif(int(new.feedbackExists) == 0):
                noMarkers = False;
            else:
                noMarkers = False;
        try:
          oldalert
        except NameError:
          oldalert = ""
        newalert = str(user_data['alertId'])
        if(oldalert != newalert):

          polygoncenter = [0,0]
  #SETTING UP THE POLYGON
          gc = gspread.login('ieacmusv@gmail.com', 'iea@cmusv')

          worksheet = gc.open("Orchestrator").sheet1

          values_list = worksheet.col_values(1)
          #eventually need to change 30 into alertid that is specified as input! need to implement this
          alertrow = values_list.index(newalert) + 1

          polygon = worksheet.acell("S"+str(alertrow)).value
          splitpolygon = polygon.split(',')
          alerttype = worksheet.acell("L"+str(alertrow)).value
          polygonType = worksheet.acell("R"+str(alertrow)).value
         # print polygonType
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
              #print splitpolygon[geos*2-1] + "hi"
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
        if(noMarkers==0):
          polygondatatwo = ""
        removepolygon = ""
        removepolygon += """
if(alertCreator){
  alertCreator.setMap(null);
}
for (var i = 0; i < alertpolygon.length; i++ ) {
  alertpolygon[i].setMap(null);
  alertpolygon[i] = null;
}
alertpolygon.length = 0;
alertpolygon = {};"""
        polygoncoords = polygoncoords.replace('"', '\\"')
        polygondata = polygondata.replace('"', '\\"')
        polygondatatwo = polygondatatwo.replace('"', '\\"')
        return removepolygon + polygoncoords + polygondata + polygondatatwo
