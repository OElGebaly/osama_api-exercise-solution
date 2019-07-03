## Introduction

    Project represents a soltuon API to read titanic passengers data from mysql DB , API is representd via 5 methods.

## Technologies

    - application is written in Python language using Flask library in order to obtain the API capabilities.
    - DB engine used is Mysql.
    - Used nginx as application server.
    - application is Docker based to run in 3 different docker containers. 


## Run

    $ docker-compose up -d

    deployment command will apply the below steps:

    - start 3 new docker containers.
    - DB container will be launching the Mysql 5.7 service.
    - app container will start by installing all the required libraries included into app/requirements.txt file , and run the commands necessary to start the python application, python image used is "jfloff/alpine-python:latest" as a small sized image.
    - nginx latest release with necessary configuration files




## Command Line Testing
	$ curl -v --request POST --url 'http://127.0.0.1/people' -H 'content-type: application/json' --data '{ "survived": false, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25}'


	$ curl --request PUT --url http://127.0.0.1/people/04d673e4-f4ef-4e92-a8b0-1b4d3d4f28bc --header 'Content-Type: application/json' --data ' {"survived": true, "passengerClass": 1, "name": "Mr. Osama", "sex": "Male", "age": 25, "siblingsOrSpousesAboard": 110, "parentsOrChildrenAboard":11, "fare":19.25}'


	$ curl --request GET --url http://127.0.0.1/people/04d673e4-f4ef-4e92-a8b0-1b4d3d4f28bc --header 'Content-Type: application/json' 

	$ curl --request GET --url http://127.0.0.1/people --header 'Content-Type: application/json' 


	$ curl --request DELETE --url http://127.0.0.1/people/04d673e4-f4ef-4e92-a8b0-1b4d3d4f28bc --header 'Content-Type: application/json' 
	"Deleted: 04d673e4-f4ef-4e92-a8b0-1b4d3d4f28bc"    

## GUI Testing

     ![image](/test_images/65910880_477562056336922_844799537179525120_n.png)

