import urllib, json
url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
response = urllib.urlopen(url)
# print response.read()
data = json.loads(response.read())
print data



# py3
# import urllib.request, json
# with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
#     data = json.loads(url.read().decode())
#     print(data)


# < script >
# function
# collectJSON()
# {
#     var
# xmlhttp = new
# XMLHttpRequest();
# url = "http://api.openweathermap.org/data/2.5/weather?lat=";
# var key = "USE-YOUR-KEY";
# url += latitude + "&lon=" + longitude + "&appid=" + key;
# xmlhttp.open("GET", url, false);
# xmlhttp.send();
# if (xmlhttp.readyState == 4 & & xmlhttp.status == 200)
# {
# var result = xmlhttp.responseText;
# // var jsResult = JSON.parse(result);
# document.getElementById("show").innerHTML = result;
# }
# }
# < / script >