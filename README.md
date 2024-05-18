# Portfolio
A portfolio website for myself to show off my coding skills

## Index
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Contributors](#contributors)

## Technologies Used

* Python
* Next.js
* Bootstrap
* Tailwind CSS
* Django
* Django REST framework
* django-cors-headers
* gunicorn
* nginx
* framer-motion
* react-countup
* react-icons
* react-toastify
* swiper
* react-tsparticles
* tsparticles

## Getting Started

### Backend Setup
1. **Clone the repository:**
    ```sh
    git clone https://github.com/dmerc12/Portfolio.git
    cd Portfolio
    ```

2. **Create a new virtual environment:**
    ```sh
    python3 -m venv .venv
    ```

3. **Activate the virtual environment:**
    ```sh
    source .venv/bin/activate
    ```

4. **Install the necessary dependencies:**
    ```sh
    pip install pip install django djangorestframework django-cors-headers gunicorn
    ```

5. **Change into the backend directory:**
    ```sh
    cd backend
    ```

6. **Make and apply migrations:**
    ```sh
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

7. **Run the backend server:**
    ```sh
    gunicorn --workers 3 myproject.wsgi:application
    ```

### Frontend Setup
1. **Change to the frontend directory:**
    ```sh
    cd ../frontend
    ```

2. **Install the necessary dependencies:**
    ```sh
    npm install
    ```

3. **Build the Next.js application:**
    ```sh
    npm run build
    ```

4. **Serve the application:**
    ```sh
    npm install -g serve
    serve -s build
    ```

### Nginx Setup
1. **Install Nginx:**
    ```sh
    sudo apt update
    sudo apt install nginx
    ```

2. **Configure Nginx for Django (Backend):**
    ```sh
    sudo nano /etc/nginx/sites-available/django
    ```

    Add the following configuration:
    ```nginx
    server {
        listen 8000;
        server_name your_domain_or_IP;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /static/ {
            alias /path/to/your/django/static/;
        }

        location /media/ {
            alias /path/to/your/django/media/;
        }
    }
    ```

    **Enable the configuration and restart Nginx:**
    ```sh
    sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled
    sudo nginx -t
    sudo systemctl restart nginx
    ```

3. **Configure Nginx for Next.js (Frontend):**
    ```sh
    sudo nano /etc/nginx/sites-available/nextjs
    ```

    Add the following configuration:
    ```nginx
    server {
        listen 3000;
        server_name your_domain_or_IP;

        location / {
            proxy_pass http://127.0.0.1:3000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```

    **Enable the configuration and restart Nginx:**
    ```sh
    sudo ln -s /etc/nginx/sites-available/nextjs /etc/nginx/sites-enabled
    sudo nginx -t
    sudo systemctl restart nginx
    ```

### Optional - Manage Processes with Supervisor

1. **Install Supervisor:**
    ```sh
    sudo apt install supervisor
    ```

2. **Create Supervisor configuration for Gunicorn (Django):**
    ```sh
    sudo nano /etc/supervisor/conf.d/django.conf
    ```

    Add the following configuration:
    ```ini
    [program:gunicorn]
    directory=/path/to/your/django/project
    command=/path/to/your/django/project/venv/bin/gunicorn --workers 3 myproject.wsgi:application
    autostart=true
    autorestart=true
    stderr_logfile=/var/log/gunicorn.err.log
    stdout_logfile=/var/log/gunicorn.out.log
    ```

3. **Create Supervisor configuration for Next.js:**
    ```sh
    sudo nano /etc/supervisor/conf.d/nextjs.conf
    ```

    Add the following configuration:
    ```ini
    [program:nextjs]
    directory=/path/to/your/nextjs/project
    command=npx serve -s build
    autostart=true
    autorestart=true
    stderr_logfile=/var/log/nextjs.err.log
    stdout_logfile=/var/log/nextjs.out.log
    ```

4. **Start Supervisor:**
    ```sh
    sudo supervisorctl reread
    sudo supervisorctl update
    sudo supervisorctl start all
    ```

## Contributors

- [Dylan Mercer](https://github.com/dmerc12)
