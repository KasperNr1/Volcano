# Homelab Documentation - vanbos-server

This document outlines the setup, access methods, and management commands for the services running on the Ubuntu server.

## Booting
On Mac
```
wakeonlan -i 192.168.2.255 -p 9 2c:44:fd:15:1f:56
```

On Mobile
```
python -c "import socket; b=bytes.fromhex('f'*12 + '2c44fd151f56'*16); s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1); s.sendto(b, ('192.168.2.255', 9))"
```


---

## 1. Core Management
All Docker services are managed from the directory: `~/homelab`

### General Commands
* **Start all services:** `docker compose up -d`
* **Stop all services:** `docker compose stop`
* **Check resource usage:** `btop` (Host command)
* **View combined logs:** `docker compose logs -f`

---

## 2. Services List

### 📂 Samba File Sharing
Network storage for university projects and server backups.
* **Address:** `smb://<SERVER_IP>/HomeFiles`
* **Access:** Use macOS Finder (Cmd+K). Authenticate with Ubuntu credentials.
* **Storage Path:** `~/homelab/data/samba`
* **Logs:** `docker logs -f homelab-samba-1`

### 🎮 Minecraft Server (Java Edition)
Publicly accessible gaming server with whitelist security.
* **Local Address:** `<SERVER_IP>:25565`
* **Public Address:** `<YOUR_PUBLIC_IP>:25565`
* **Admin Commands (OP):**
    `docker exec -u 1000 homelab-minecraft-1 mc-send-to-console op <username>`
* **Whitelist Management:**
    * `docker exec -u 1000 homelab-minecraft-1 mc-send-to-console whitelist add <username>`
    * `docker exec -u 1000 homelab-minecraft-1 mc-send-to-console whitelist remove <username>`
* **Logs:** `docker logs -f homelab-minecraft-1`

### 🖨️ CUPS Print Server
Network-enables the Epson ET-2710 via USB.
* **Web Interface:** `http://<SERVER_IP>:631`
* **Setup:** Native install on Ubuntu (Bare Metal) for USB stability.
* **Status:** Idle, Accepting Jobs, Shared.
* **Logs:** `sudo tail -f /var/log/cups/error_log`

### 📄 Scanservjs (Web Scanner)
Browser-based scanning directly to the Samba share.
* **Web Interface:** `http://<SERVER_IP>:8080`
* **Output Folder:** Scans are automatically saved to `HomeFiles/Scans`.
* **Logs:** `docker logs -f homelab-scanservjs-1`

### 🔐 WireGuard VPN
Secure remote access to the local network.
* **Usage:** Launch WireGuard client on Mac/Phone and toggle the 'Homelab' tunnel.
* **Function:** Allows access to local IPs (192.168.2.x) and the Scanner UI from anywhere.

---

## 3. Network Configuration
* **Internal IP:** Found via `hostname -I`
* **Public IP:** Found via `curl -4 ifconfig.me`
* **Router (Speedport Smart 4):**
    * **Port Activation:** 25565 (TCP) forwarded to server IP.
    * **Admin UI:** `http://192.168.2.1`

---

## 4. Troubleshooting
* **Container fails to start:** Check `docker compose logs`. Ensure no port conflicts.
* **Scanner not found:** Refresh the web UI at port 8080. If persistent, power cycle the Epson printer.
* **Whitelist not working:** Ensure `ENFORCE_WHITELIST: "true"` is set in `docker-compose.yml`.
