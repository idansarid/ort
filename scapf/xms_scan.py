from scapy.all import sr
from scapy.all import IP, TCP

ans, unans = sr(IP(dst="www.slashdot.org")/TCP(dport=[80,666],flags="A"))
# ans, unans = sr(IP(dst="192.168.1.1")/TCP(dport=666,flags="FPU") )
a = IP(dst="www.slashdot.org/30")