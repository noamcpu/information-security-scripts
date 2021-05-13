from scapy.all import *
from scapy.layers.inet import IP, TCP

PC_F = "SynFloodSample.pcap"
DEST_FILE = r'C:\Networks\works\venv.txt'

ip_syn_count = {}


# I compare number of syns and acks
#and if there is above 5 syns(normal average ) from specific server is suspect as attacker
def main():
    pcap_file = rdpcap(PC_F)
    counter = 0
    for pkt in pcap_file:
        src = pkt[IP].src
        if pkt[TCP].flags == 2:
            counter = 1
        if pkt[TCP].flags == 16:
            counter = -1

        if src in ip_syn_count:
            ip_syn_count[src] += counter
        else:
            ip_syn_count[src] = counter

    with open(DEST_FILE, 'w') as file:
        for ip, count in ip_syn_count.items():
            if count >= 5:
                print(ip, count)
                file.write(ip)


if __name__ == '__main__':
    main()
