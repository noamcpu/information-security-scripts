from scapy.all import *
from scapy.layers.http import *
import sys

from scapy.layers.l2 import Ether

sys.path.insert(0, '.')
from create_recording import recording_path  # the path to the pcap file of this assignment

"""
process pcap file, and extract the source MAC address of the 3rd captured packet.
"""


def show_mac_address():
    packets = rdpcap(recording_path)
    packets = packets[2]
    print(packets[Ether].src)
    # print mac address


show_mac_address()
