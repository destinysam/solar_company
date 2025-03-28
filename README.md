## Solar App

Solar Cell Company Calculation

#### License

MIT

# Frappe Bench Full Setup

Note:

## Prerequisites


- Python 3.10+
- Node.js 16+
- npm 7+
- Redis
- MariaDB 10.6+
- Yarn
- wkhtmltopdf (for PDF generation)
- Supervisor (for process management)
- Nginx (for reverse proxy)

## Step 1: Update System
```bash
sudo apt update && sudo apt upgrade -y
```

## Step 2: Install Dependencies
```bash
sudo apt install -y python3-dev python3-pip python3.10-venv \
    redis-server curl git-core \
    mariadb-server mariadb-client \
    libmysqlclient-dev xvfb libfontconfig wkhtmltopdf \
    libssl-dev libffi-dev nodejs npm \
    yarn supervisor nginx
```

## Step 3: Secure MariaDB
```bash
sudo mysql_secure_installation
```
Follow the prompts to set up a root password and remove unnecessary users.

## Step 4: Configure MariaDB
Edit the MariaDB configuration file:
```bash
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```
Add the following under `[mysqld]`:
```ini
default-storage-engine = innodb
innodb-file-format = Barracuda
innodb-file-per-table = 1
innodb-large-prefix = 1
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
```
Restart MariaDB:
```bash
sudo systemctl restart mariadb
```

## Step 5: Install Frappe Bench
```bash
pip install frappe-bench
```

## Step 6: Initialize Frappe Bench
```bash
bench init --frappe-branch version-14 frappe-bench
cd frappe-bench
```

## Step 7: Create a New Frappe Site
```bash
bench new-site mysite.local --mariadb-root-password root_password
```









