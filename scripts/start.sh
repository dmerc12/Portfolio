#!/bin/bash

echo "Starting Gunicorn, Next.js, and Nginx..."
cd ../

# Restart Gunicorn and Next.js processes managed by Supervisor
sudo supervisorctl restart gunicorn
sudo supervisorctl restart nextjs

# Restart Nginx service
sudo systemctl restart nginx

echo "All services started."
