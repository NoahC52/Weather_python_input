# Weather_Python_input
Simply input a US based zipcode and receive weather!
# Hello!
This weather app I builit uses OpenWeather's API for delivering weather based on zipcode!
This version is much simipler than the SMS based one, all it uses is one input from the user asking them for the zipcode. We take the zipcode and transfer it to the API to convert the zipcode into longitude and latitude. We then take the longitude and latitude and use the API once more to get the weather data, the data will be in JSON, so we will just setup variables to hold parsed data for us. After all said is done we format it and print it out to the user.
# OpenWeather API key
You will need to get your own API key and add it. 
https://openweathermap.org/api
