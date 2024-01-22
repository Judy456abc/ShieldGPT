import subprocess
import os
import tqdm

pcap_file = "AppDDos.pcap"
with open("ip_pairs_tshark.txt") as f:
    os.makedirs("split_tcpdump", exist_ok=True)
    for line in tqdm.tqdm(f.readlines()):
        if len(line.strip()) < 2:
            continue
        src_ip, dst_ip = line.strip().split()
        filename = f"split_tcpdump/{src_ip}_{dst_ip}.pcap"
        cmd = f"tcpdump -nr {pcap_file} -w {filename} 'ip src {src_ip} and ip dst {dst_ip}'"
        subprocess.run(cmd, shell=True)