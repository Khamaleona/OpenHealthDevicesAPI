# OpenHealthDevicesAPI
Web API for the Open Health Devices project

<hr>

<h2>Introduction</h2>

As we can see in the related repository "OpenHealthDevices", the sensors created can send its measurements to a web server/API in order to keep them stored safely. This API is designed to allow users to get the measurements of those sensors they are interested in. 

We have designed this API using Python with PyMySQL, a pure-Python MySQL client library that works with MySQL 5.5+ and MariaDB 5.5+. In odert to set up the API, we installed XAMPP (that includes Apache Tomcat and MySQL) as it is easier to use. However, you could install the server and database engine that you prefer.

<hr>

<h2>Description</h2>

This simple API is composed by two files:

<ul>
  <li>sensors.py</li>
  <li>app.py</li>
</ul>

<b>Sensors.py:</b> this file describes the database Diabetes table structure. This tables stores every measurement obtained from each sensor. It has four attributes, id (an identification number), sensor (a number that indicates which sensor took the measurement), value (the measurement itself) and date (the measurement date and time). 

<b>App.py:</b> this is the main script of our API. It indicates the initial configuration and main functions the API performs:
<ul>
  <li><b>GET DATA (ALL):</b> a GET request that returns all the data stored in the database as a JSON object.</li>
  <li><b>GET DATA (sensor):</b> a GET request that returns all the data stored of a given sensor number identification as a JSON object.</li>
  <li><b>ADD DATA:</b> a POST request that send the measurement read for the sensor. This request must have a sensor identification number, the measurement value and the date and time it has been made.</li>
  <li><b>DOWNLOAD (sensor):</b> this function permits users to download all data related to a given sensor as a CSV file.</li>
