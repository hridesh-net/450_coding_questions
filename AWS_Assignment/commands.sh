# install Python 3.11 in Ubuntu

# add the following PPA.
sudo add-apt-repository ppa:deadsnakes/ppa

# Refresh the cache
sudo apt update

#  install Python 3.11 using the below command.
sudo apt install python3.11

# Check Python version 
python3 --version


# Use update-alternatives to create symbolic links to python3
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2


# choose which one to use as Python3 via the command:
sudo update-alternatives --config python3


## Install Python 2.7

# Adding Universe repo
sudo apt-add-repository universe
sudo apt update

# Install Python2.7
sudo apt install python2-minimal

# Check Python2 version
python2 -V

# See all available Python version on the system
ls /usr/bin/python*

# to set Python 3 as default or first version in the priority list, simply update the alternatives list, using this command:
sudo update-alternatives --config python


## install jdk 8
sudo apt-get install openjdk-8-jdk

## install jdk 17
sudo apt update
sudo apt install openjdk-17-jdk

# To switch b/w java version
sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_version/bin/java
# OR 
sudo update-alternatives --config java

# To list available versions of jdk or java
update-java-alternatives --list


## Installing Tomcat

sudo apt update

# check for available apache Tomcat package
sudo apt-cache search Tomcat

#install apache tomcat
sudo apt install tomcat9 tomcat9-admin

#check ports
ss -lt
