# Project 4:  Brevet time calculator with Ajax

### Author: Brandon Sov , bhs@cs.uoregon.edu ###

##Description##

This project is a remodeled brevet time calculator which can be found at
https://rusa.org/octime_acp.html. The rusa site features a static way to get the
times after entering a control point in kilometers or miles. This is tedioius
because you need to be redirected to another page to see the times. Our solution
is to make it dynamic so you can see it at the time of entering a distance.

##Installation and running ##

For a unix machine such as a mac or a raspberry pi you can run this program
by entering this line in your terminal: <br/>
```
git clone https://github.com/brandonsov/proj4-brevets
cd proj4-brevets
make run
```

Then go to localhost:5000 or (IP address of device):5000 to see the brevet calculator.

##System compatibility##

This program has only been tested on a Macbook running macOS Sierra and a
raspberry Pi running Raspbian Jessie

##Features##
-If you enter a control at 0, the closing time will always be an hour from the
start of your brevet and the opening time will be your start time. <br/>
-If you input kilometers you can find the open and closing times for those controls
at the set date you gave.<br/>
-If you go over 20% of the set brevet distance for a control point, then it will
highlight red and warn you to change that.<br/>
-If you enter a control that is the length of the brevet, then according to the rules
found at https://rusa.org/pages/rulesForRiders then they will have different ending times. <br/>
-Rounds the distances as done by https://rusa.org/octime_acp.html (e.g. 2.5 gets
rounded up to 3 and 2.4 gets rounded down to 2)<br/>




##Screenshots ##
![Settings Window](https://raw.github.com/brandonsov/proj4-brevets/master/sample.png)

![Settings Window](https://raw.github.com/brandonsov/proj4-brevets/master/sample2.png)
