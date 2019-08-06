# README #

![Robot framework](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Robot-framework-logo.png/250px-Robot-framework-logo.png)

Robot Framework Desktop Application Automation/Robotic Process Automation example

This has been made to be run (and tested) on Windows 10 (not set in dark mode)


### Who is this repository for? ###

Newcomers to Robot Framework interested in automated Desktop application testing or RPA, looking for examples

### What is Robot Framework? ###

Robot framework is a python based, open source test automation framework with great extensibility. Robot framework is cross platform and will run on Mac, Linux and Windows. 

See [here ](https://robotframework.org/)for Robot Framework home page


### What exactly is this? ###

A basic Robot Framework Desktop Application (Microsoft Paint) test suite with the following tasks:

* Open Paint
* Open File In Paint
* Rotate Image in Paint
* Save File and Exit Paint

[Sikuli](https://github.com/rainmanwy/robotframework-SikuliLibrary) is the supporting library used in this suite along with custom Python keywords for key presses



### How do I get set up? ###

* Install [Python 3](https://python.org/)
* Install Java SDK and add PATH enviroment variables
* Clone or download this repository
* Using the command line navigate in to the project folder and execute the command ```pip install -r requirements``` this will install robot framework and the required supporting library and dependencies as well as [pypiwin32](https://github.com/Googulator/pypiwin32)

Once everything has been installed you can run the test suite from the command line in the projects folder with the command```robot .\rpa.robot``` 



### Who do I talk to? ###

* Anthony O`Donnell - [LinkedIn](https://www.linkedin.com/in/anthonyodonnell)
