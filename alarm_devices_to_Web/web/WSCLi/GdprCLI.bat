@echo off

set MAIN_CLASS=com.allot.nms.webservices.cli.gdpr.GdprCLI
set SERVER=127.0.0.1
set CONNECTION_TIMEOUT=300000
set RECEIVE_TIMEOUT=1800000

echo Please Insert password
set /p psw=

java -Dserver=%SERVER% -Djava.naming.provider.url=http://%SERVER%/wildfly-services -Dwildfly.config.url=wildfly-config.xml -Dtransport.security.layer.enable=false -Dauth=true -Dconnection.timeout=%CONNECTION_TIMEOUT% -Dreceive.timeout=%RECEIVE_TIMEOUT% -cp "*" %MAIN_CLASS% %* -password %psw%

