# API POLLER

* The polls two api's, sends the message to message queue and then saves them to mongodb collection.
* Rabbitmq was used as message queue
* The API was polled asynchronously using python asyncio library
* Separate modules were created for database and message queue
* The message is saved in queue and then when the receiver receives it, the message is converted to json format
  and stored in mongodb collection.


# Rabbitmq Docker Image How to Run

* Command:- run ```docker build .``` if in same directory as dockerfile
            else run ```docker build -f <dockerfile path> .```


