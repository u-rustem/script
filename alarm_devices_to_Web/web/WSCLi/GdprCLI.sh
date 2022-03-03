#!/bin/sh

# if don't have JAVA_HOME please configure
# JAVA_HOME="/opt/allot/java/jdk"
# export JAVA_HOME
# export PATH=$JAVA_HOME/bin:$PATH

MAIN_CLASS=com.allot.nms.webservices.cli.gdpr.GdprCLI
SERVER=127.0.0.1
CONNECTION_TIMEOUT=300000
RECEIVE_TIMEOUT=1800000

echo Please insert password
read -s password


java -Dserver=$SERVER -Djava.naming.provider.url=http://$SERVER/wildfly-services -Dwildfly.config.url=wildfly-config.xml -Dtransport.security.layer.enable=false -Dauth=true -Dconnection.timeout=$CONNECTION_TIMEOUT -Dreceive.timeout=$RECEIVE_TIMEOUT -cp "*" $MAIN_CLASS "$@" -password $password


