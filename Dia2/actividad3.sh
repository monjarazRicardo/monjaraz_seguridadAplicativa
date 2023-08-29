scaneo=$(nmap 127.0.0.1 | tail -2 | awk {'print $6'}| cut -d "(" -f 2)
echo "Los Host activos son: " $scaneo
