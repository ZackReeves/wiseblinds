Wise Blinds - Embedded Systems CW1
==================================

This repository contains all the files developed as part of ELEC60013 - Embedded Systems, completed Spring 2023.

Wise Blinds is an IoT powered smart curtain device intended to improve sleep quality and environment control. It contains a range of sensors which are controlled by raspberry pis measuring:

- Temperature
- Humidity
- Light
- Clap detection

The Light sensor is used to control the opening and closing of the curtains in the morning and evenings, whilst the temperature and humidity sensors control the curtain through the day in the case of extreme weather, where closing the curtains to keep heat in or out is beneficial. This data is stored in a secure database (hosted on firebase for prototyping), where it can be accessed by the motor controller. The curtains are controlled by a motor connected to a raspberry pi.

It is all controlled via mobile app which allows the user to choose between automatic and mannual modes as well as turning on and off clap detection.

[**Application**](Application)
---------------------------------
This folder contains all the files used for the development of the application made with expo.


[**MotorPi**](MotorPi)
----------------------
This folder contains the files for the raspberry pi controlling the motor and microphone for clap detection.

[**SensorPi**](SensorPi)
------------------------
This folder contains the files for the raspberry pi responsible for the temperature, humidity and light sensors as well as the initial data processing of each reading.


Website
-------
[Wise Blinds Website](https://zelenkomaxime.wixsite.com/wiseblinds?classId=5472a3f9-8019-4764-a3a2-2804674e716c&assignmentId=95c87d7e-e230-4e23-862b-9817d51049b5&submissionId=5f7ddafe-815f-861b-a6c8-b568b47b4d22)

Contributors
------------

- Zack Reeves
- Kert Laansalu
- Floro Balzer
- Max Zelenko
