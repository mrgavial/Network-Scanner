import scapy.all as scapy
import argparse


def input_argument():
    object = argparse.ArgumentParser()
    object.add_argument("--ip",dest="dest_ip",help="Enter IP Address")

    input_user = object.parse_args()

    return input_user

def scan_network(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_packet
    (results,unanswered) = scapy.srp(combined_packet,timeout=1)
    results.summary()

ip_address = input_argument()
scan_network(ip_address.dest_ip)
