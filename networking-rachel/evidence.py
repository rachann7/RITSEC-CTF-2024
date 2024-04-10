from scapy.all import *
import random
import string

# Function to generate random payloads
def generate_random_payload(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Number of packets to generate
num_packets = 100000

# Generate and save the packets to a pcap file
packets = []

# Add flood of packets with random payloads
for _ in range(num_packets):
    payload_length = random.randint(50, 200)  # Random payload length between 50 and 200 bytes
    random_payload = generate_random_payload(payload_length)
    packet = Ether() / IP(dst="10.0.0.1") / TCP(dport=80) / Raw(load=random_payload)
    packets.append(packet)

# Generate a random index to insert the packet with the flag
flag_index = random.randint(1, num_packets - 1)  # Exclude the first and last positions
flag = "RS{pc@p$_@r3_0ur_fr!3nd$}"
http_packet = Ether() / IP(dst="10.0.0.1") / TCP(dport=80) / Raw(load="GET / HTTP/1.1\r\n\r\n" + flag)
packets.insert(flag_index, http_packet)

# Save all the packets to a pcap file
wrpcap("evidence.pcap", packets)

