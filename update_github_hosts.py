import socket
import os
from datetime import datetime, timedelta

domains = [
    "github.com",
    "gist.github.com",
    "api.github.com",
    "assets-cdn.github.com",
    "raw.githubusercontent.com",
    "gist.githubusercontent.com",
    "cloud.githubusercontent.com",
    "camo.githubusercontent.com",
    "avatars0.githubusercontent.com",
    "avatars1.githubusercontent.com",
    "avatars2.githubusercontent.com",
    "avatars3.githubusercontent.com",
    "avatars4.githubusercontent.com",
    "avatars5.githubusercontent.com",
    "avatars6.githubusercontent.com",
    "avatars7.githubusercontent.com",
    "avatars8.githubusercontent.com",
    "user-images.githubusercontent.com",
    "github.githubassets.com"
]

OUTPUT_FILE = "github_hosts.txt"

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        print(f"[!] 无法解析 {domain}: {e}")
        return None

def generate_hosts():
    lines = []
    for domain in domains:
        ip = resolve_domain(domain)
        if ip:
            lines.append(f"{ip}\t{domain}")
    return lines

def save_hosts(lines):
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        print(f"[+] 删除旧文件 {OUTPUT_FILE}")
        
    # 获取北京时间 (UTC+8)
    bj_time = (datetime.utcnow() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# GitHub Start (Updated: {bj_time})\n")
        for line in lines:
            f.write(line + "\n")
        f.write("# GitHub End\n")
    print(f"[+] 已生成 {OUTPUT_FILE}")

if __name__ == "__main__":
    hosts = generate_hosts()
    save_hosts(hosts)
