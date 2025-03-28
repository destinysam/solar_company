## Solar App

Solar Cell Company Calculation

#### License

MIT


# Table of Contents


- [Frappe Bench Full Setup](#frappe-bench-full-setup)
- [Setup Solar app](#setup-solar-app)
  


# Frappe Bench Full Setup

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

## Step 8: Add site to hosts
```bash
sudo nano /etc/hosts
```
## Setup Solar app

## Step 10: Get solar app
```bash
bench get-app solar_app https://github.com/destinysam/solar_company
```

## Step 11: Install solar app on the site
```bash
bench --site mysite.local install-app solar_app
```

## Step 12: Let's migrate now
```bash
bench --site site_name migrate
```

## Step 13: Finally,Start the server
```bash
bench start
```

## Step 14: Doctypes Available
```bash
Calculation Entry: A doctype holds calculcation entries
Customer: A doctype holds customer entries.
```

## Step 15: API's
```bash
http://{{site_name}}:8000/api/method/solar_app.api.v1.tariff.get_monthly_tariff : API to fetch low tariff and high tariff for monthly based on query params year and month

Query Params:
year: str
month: str

Response:
{
    "message": {
        "low_tariff": 0.0,
        "high_tariff": 289.2
    }
}
```


Thank you












