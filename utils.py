#Encode city for Airbnb URL
def create_airbnb_url(city, checkin, checkout):
    #https://www.airbnb.com/s/Dubai-~-United-Arab-Emirates?guests=2&checkin=01%2F12%2F2016&checkout=01%2F20%2F2016&ss_id=d6heijmr&source=bb
    city_encode = city.replace(',',"-")
    city_encode = city_encode.replace(' ',"-")

    print "city is", city_encode
    checkin_encode = checkin[5:7] + "%2F" + checkin[8:10] + "%2F" + checkin[0:4]
    print "checkin is", checkin_encode
    checkout_encode = checkout[5:7] + "%2F" + checkout[8:10] + "%2F" + checkout[0:4]
    print "checkout is", checkout_encode

    airbnb_url = "https://www.airbnb.com/s/" + city_encode + "?guests=2&checkin="+checkin_encode+"&checkout=" + checkout_encode

    return airbnb_url

print create_airbnb_url("Dubai, United Arab Emirates", "2016-01-23 09:30", "2016-01-24 08:15")
