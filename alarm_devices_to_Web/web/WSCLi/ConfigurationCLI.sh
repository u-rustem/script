#!/bin/sh

# if don't have JAVA_HOME please configure
# JAVA_HOME="/opt/allot/java/jdk"
# export JAVA_HOME
# export PATH=$JAVA_HOME/bin:$PATH

MAIN_CLASS=com.allot.nms.webservices.cli.configuration.ConfigurationCLI
USERNAME=admin
PASSWORD=Bagabu123456!
SERVER=10.0.208.3
CONNECTION_TIMEOUT=300000
RECEIVE_TIMEOUT=1800000

java -Dserver=$SERVER -Djava.naming.provider.url=http://$SERVER/wildfly-services -Dwildfly.config.url=wildfly-config.xml -Duser=$USERNAME -Dpassword=$PASSWORD -Dtransport.security.layer.enable=false -Dauth=true -Dconnection.timeout=$CONNECTION_TIMEOUT -Dreceive.timeout=$RECEIVE_TIMEOUT -cp "*" $MAIN_CLASS "$@"
