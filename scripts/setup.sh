#!/bin/bash

# Update and upgrade the system
cd ../
sudo apt update -y
sudo apt upgrade -y

# Install Python, pip, and virtualenv
sudo apt install -y python3 python3-pip python3-venv

# Install Node.js and npm
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y nodejs

# Install PM2 to manage Node.js applications
sudo npm install -g pm2

# Prompt user for database configuration details
read -p "Enter your AWS database name: " db_name
read -p "Enter your AWS database user: " db_user
read -sp "Enter your AWS database password: " db_password
echo
read -p "Enter your AWS database host: " db_host
read -p "Enter your AWS database port: " db_port

# Backend setup
# Create a new virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install backend dependencies
pip install django djangorestframework django-cors-headers gunicorn psycopg2-binary

# Change into the backend directory
cd backend

# Update Django settings for AWS database
cat <<EOL >> settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '$db_name',
        'USER': '$db_user',
        'PASSWORD': '$db_password',
        'HOST': '$db_host',
        'PORT': '$db_port',
    }
}
EOL

# Make and apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Start the backend server with Gunicorn
gunicorn --workers 3 myproject.wsgi:application &

# Frontend setup
# Change to the frontend directory
cd ../frontend

# Install frontend dependencies
npm install

# Build the Next.js application
npm run build

# Serve the application with PM2
pm2 start npm --name "nextjs" -- start

# Nginx setup
# Install Nginx
sudo apt install -y nginx

# Configure Nginx for Django (Backend)
sudo tee /etc/nginx/sites-available/django <<EOF
server {
    listen 8000;
    server_name your_domain_or_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    location /static/ {
        alias /path/to/your/django/static/;
    }

    location /media/ {
        alias /path/to/your/django/media/;
    }
}
EOF

# Enable the Nginx configuration for Django and restart Nginx
sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

# Configure Nginx for Next.js (Frontend)
sudo tee /etc/nginx/sites-available/nextjs <<EOF
server {
    listen 3000;
    server_name your_domain_or_IP;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable the Nginx configuration for Next.js and restart Nginx
sudo ln -s /etc/nginx/sites-available/nextjs /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

# Optional - Manage processes with Supervisor
# Install Supervisor
sudo apt install -y supervisor

# Create Supervisor configuration for Gunicorn (Django)
sudo tee /etc/supervisor/conf.d/django.conf <<EOF
[program:gunicorn]
directory=$(pwd)/backend
command=$(pwd)/.venv/bin/gunicorn --workers 3 myproject.wsgi:application
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn.err.log
stdout_logfile=/var/log/gunicorn.out.log
EOF

# Create Supervisor configuration for Next.js
sudo tee /etc/supervisor/conf.d/nextjs.conf <<EOF
[program:nextjs]
directory=$(pwd)/frontend
command=npx serve -s build
autostart=true
autorestart=true
stderr_logfile=/var/log/nextjs.err.log
stdout_logfile=/var/log/nextjs.out.log
EOF

# Start Supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start all

# Prompt to create a superuser
read -p "Do you want to create a Django superuser now? (y/n) " answer
if [[ "$answer" == "y" ]]; then
    source ../.venv/bin/activate
    cd backend
    python3 manage.py createsuperuser
fi

echo "Setup completed successfully."
