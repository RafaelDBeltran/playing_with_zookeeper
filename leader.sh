#!/bin/bash

sudo docker exec -it zoo_zoo1_1 bin/zkServer.sh status | grep Mode
sudo docker exec -it zoo_zoo2_1 bin/zkServer.sh status | grep Mode
sudo docker exec -it zoo_zoo3_1 bin/zkServer.sh status | grep Mode