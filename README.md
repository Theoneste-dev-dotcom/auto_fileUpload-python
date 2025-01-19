Author: DUFITIMANA Theoneste
Date: 2022-01-19
Time: 5:50:00.000000

Project Name: AUTO-IMAGE UPLOAD with PYTHON

## PROJECT DESCRIPTIONS

## Objective:

Write a Python script to automate the following tasks:

    1.    Monitor a folder where a camera regularly saves captured pictures.

    2.    Automatically upload each picture after 30 seconds using the curl command.

    3.    Once a picture is successfully uploaded, move it to another folder named uploaded to avoid redundancy.

## Requirements:

    •    URL for Upload:

https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php

    •    Key Attribute:

Use the attribute imageFile when uploading images with the curl command.

Example curl Command:

curl -X POST -F imageFile=@/path/to/your/image.jpg <upload_url>
