#!/bin/bash

echo "Stopping Gunicorn, Next.js, and Nginx..."
cd ../

# Stop Gunicorn and Next.js processes managed by Supervisor
sudo supervisorctl stop gunicorn
sudo supervisorctl stop nextjs

# Stop Nginx service
sudo systemctl stop nginx

echo "All services stopped."
