from django.shortcuts import render
import requests
import json
import random
import os


class Weather:
    # https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={YOUR API KEY}
    url='https://api.openweathermap.org/data/2.5/weather?'
    key='aa1971877144126023f3c195462ecb6a'
    file='Report'

    def __init__(self,city):# exclude,
        #self.exclude=exclude
        self.appid=self.key
        self.city=city
        #self.point = lat + ',' + lon
        self.payload = {'appid':self.appid,'units':'metric','q':city} #'lat':lat,'lon':lon,'exclude':exclude,
        self.filename = str(Weather.file) + '.csv'
    def get_report(self):
        data = json.loads(requests.get(Weather.url,params=self.payload).text)
        return data
        #x = datetime.datetime(2018, 6, 1)
        #a=x.strftime("%H")
        #print(json.dumps(data, indent=2, sort_keys=True))
    def image_select(self,temp):
        if temp<0:
            ls=["Hoth.jpg","Niflheim.jpg","Land of always winter.jpg"]
            return random.choice(ls)
        elif temp>=0 and temp<5:
            ls=["Berk.png","North.jpg","Jotunheim.png","Drum Island.jpg"]
            return random.choice(ls)
        elif temp>=5 and temp<10:
            ls=["Asguard.jpg","Vanaheim.jpg"]
            return random.choice(ls)
        elif temp>=10 and temp<15:
            ls=["Hogwarts.jpg","Alfheim.jpg"]
            return random.choice(ls)
        elif temp>=15 and temp<20:
            ls=["Hobbiton.jpg","Konoha.jpg",]
            return random.choice(ls)
        elif temp>=20 and temp<25:
            ls=["Paradis.jpeg","Naboo.jpg"]
            return random.choice(ls)
        elif temp>=25 and temp<30:
            ls=["Wankanda.jpg","Alola.jpg","Dantooine.jpg"]
            return random.choice(ls)
        elif temp>=30 and temp<35:
            ls=["Fire nation.jpg","Stormlands.jpg"]
            return random.choice(ls)
        elif temp>=35 and temp<40:
            ls=["Sunagakure.jpg","Dagobah.jpeg"]
            return random.choice(ls)
        elif temp>=40 and temp<45:
            ls=["Alabasta.jpg","Agrabah.png","Agrabah.jpg"]
            return random.choice(ls)
        elif temp>=45 and temp<50:
            ls=["Tatooine.jpg","Dorne.jpg"]
            return random.choice(ls)
        elif temp>=50:
            ls=["Mordor.jpg","Muspelheim.jpg","Mustafar.jpeg"]
            return random.choice(ls)
# Create your views here.
def home(request):
    return render(request,'index.html')
def process(request):
    city = request.POST.get('city','Guest')
    ob = Weather(city)  # exclude,
    j=ob.get_report()
    #return render(request, 'res.html',{'res':json.dumps(j, indent=2, sort_keys=True)})
    city_n=j['name']
    c_temp=j['main']['temp']
    max_temp=j['main']['temp_max']
    min_temp=j['main']['temp_min']
    humid=j['main']['humidity']
    press=j['main']['pressure']
    feel=j['main']['feels_like']
    icon="http://openweathermap.org/img/wn/"+j['weather'][0]['icon']+"@2x.png"
    descrip=j['weather'][0]['description'].title()
    ln=ob.image_select(c_temp)
    im='Fantasy/'+ln
    land=os.path.splitext(ln)[0]
    return render(request, 'res.html',{
        'city':city_n,
        'temp':c_temp,
        'temp_max':max_temp,
        'temp_min':min_temp,
        'humidity':humid,
        'pressure':press,
        'feels':feel,
        'ico':icon,
        'desc':descrip,
        'i':im,
        'l':land,
    })