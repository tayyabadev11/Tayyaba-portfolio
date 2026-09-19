# Tayyaba Zafar — Portfolio Website

## Description
This is a personal portfolio website built with Django to present my background, skills, services, and projects as a BS Artificial Intelligence student and web developer. It features a home page with a hero introduction, an about section with my profile picture and background, a dedicated skills section, a services page outlining what I offer, a dynamic projects page showcasing my work with live status tracking, a contact page for visitors to get in touch, and a newsletter subscription system so visitors can get notified about new projects. The project follows a clean, reusable template structure with a custom black and red theme, and uses environment-based configuration to keep sensitive settings secure.

## Features

### Home Page
- Hero banner with introduction, short bio, and a skills preview
- Call-to-action buttons ("View My Work", "Get In Touch")

### About Page
- Profile picture alongside a personal introduction
- Skill tags
- Link to my GitHub profile
- Download CV and View CV options

### Skills Page
- Grid showcasing my technical skills

### Services Page
- Cards listing the services I offer, each with a detailed description

### Projects Page
- Dynamic project cards powered by backend data
- Live status tracking per project:
  - **Completed** — shows a Live Demo link (if deployed) and/or GitHub Repository link
  - **In Progress** — shows a GitHub Repository link only
  - **In Development** — shows demo/preview images instead of links
- Key Features and Technologies Used tags for each project, pulled dynamically from the backend

### Contact Page
- Working contact form
- Direct email, phone, and GitHub contact details

### Newsletter Subscription
- Visitors can subscribe with their email to get notified whenever a new project is added
- Subscriber emails are securely stored in the database
- Managed through the Django admin panel
- Email sending configured via Gmail SMTP using an App Password (kept secure through environment    variables)

### General
- Reusable navbar and footer shared across all pages
- Footer includes quick navigation links, GitHub profile link, and the newsletter subscription form
- Fully responsive design for mobile and desktop
- Consistent black-and-red / orange accent theme throughout the site

## Technologies Used
- Python
- Django
- HTML
- CSS
- SQLite
- python-decouple (environment variable management)

## Project Requirements
The required Python packages and dependencies are listed in the `requirements.txt` file.

## Folder Structure
Portfolio-Project/
├── Portfolio/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── portfolio_app/
│ ├── views.py
│ ├── urls.py
│ ├── models.py
│ ├── forms.py
│ ├── admin.py
│ └── migrations/
├── static/
│ ├── css/
│ │ └── style.css
│ ├── files/
│ │ └── CV.pdf
│ └── images/
│ ├── profile.png
│ └── projects/
│ ├── noodle-store.png
│ ├── job-portal.png
│ └── portfolio.png
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── about.html
│ ├── skills.html
│ ├── services.html
│ ├── projects.html
│ ├── contact.html
│ └── includes/
│ ├── navbar.html
│ └── footer.html
├── manage.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── db.sqlite3

## Installation

1. Clone the repository

   git clone https://github.com/tayyabadev11/Tayyaba-portfolio.git

   cd Tayyaba-portfolio

2. Create and activate a virtual environment

   python -m venv venv

   venv\Scripts\activate

3. Install the required packages

   pip install -r requirements.txt

4. Create a `.env` file in the project root and add

   SECRET_KEY=your-secret-key

   DEBUG=True

   EMAIL_HOST_USER=your-email@gmail.com

   EMAIL_HOST_PASSWORD=your-gmail-app-password

5. Run migrations

   python manage.py makemigrations

   python manage.py migrate

6. Create a superuser (optional, for admin access)

   python manage.py createsuperuser


7. Run the development server

   python manage.py runserver


8. Open `http://127.0.0.1:8000/` in your browser

## Environment
Project configuration and sensitive settings — including the secret key and email credentials — are managed using environment variables through a `.env` file, which is excluded from version control via `.gitignore`.

## Author
Tayyaba Zafar