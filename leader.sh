#!/bin/bash

sudo docker exec -it playing_with_zookeeper_zoo1_1 bin/zkServer.sh status | grep Mode
sudo docker exec -it playing_with_zookeeper_zoo2_1 bin/zkServer.sh status | grep Mode
sudo docker exec -it playing_with_zookeeper_zoo3_1 bin/zkServer.sh status | grep Mode