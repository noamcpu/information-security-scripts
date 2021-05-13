from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP

author = "_Noam Itzhak_"

DN= '8.8.8.8'


def dns_packet(msg, type_d):
    if type_d == 'PTR':
        msg = '.'.join(msg.split(".")[::-1]) + '.in-addr.arpa'
    pkt = IP(dst=DN) / UDP(sport=23456, dport=53) / DNS(qdcount=1) / DNSQR(qtype=type_d, qname=msg)
    response = sr1(pkt, verbose = 0)
    ans = response[DNS].ancount
    for i in range(ans):
        if type_d == 'PTR':
            print(response[DNSRR][i].rdata.decode("utf-8"))
        if type_d == 'A':
            print(response[DNSRR][i].rdata)


def main():
    type_d = input("enter type(A or PTR)\n")
    msg = input("enter domain \n")
    dns_packet(msg, type_d)


if __name__ == '__main__':
    main()
