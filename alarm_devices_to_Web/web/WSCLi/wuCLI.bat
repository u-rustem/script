echo off

set MAIN_CLASS=com.allot.nms.webservices.cli.wu.WuCLI
set USERNAME=user
set PASSWORD=password
set SERVER=127.0.0.1
set CONNECTION_TIMEOUT=300000
set RECEIVE_TIMEOUT=1800000

java -Dserver=%SERVER% -Djava.naming.provider.url=http://%SERVER%/wildfly-services -Dwildfly.config.url=wildfly-config.xml -Duser=%USERNAME% -Dpassword=%PASSWORD% -Dtransport.security.layer.enable=false -Dauth=true -Dconnection.timeout=%CONNECTION_TIMEOUT% -Dreceive.timeout=%RECEIVE_TIMEOUT% -cp "*" %MAIN_CLASS% %*