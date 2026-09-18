# Portfolio

## Description
This is a personal portfolio website built with Django to present my background, skills, services, and projects as a BS Artificial Intelligence student and web developer. It features a home page with a hero introduction, an about section with my profile picture and background, a dedicated skills section, a services page outlining what I offer, a projects page showcasing my completed work, and a contact page for visitors to get in touch. The project follows a clean, reusable template structure with a custom black and red theme, and uses environment-based configuration to keep sensitive settings secure.

## Features

**Home Page**
* Hero banner with introduction and a short skills preview

**About Page**
* Profile picture alongside a personal introduction
* Link to my GitHub profile
* Download CV and View CV options

**Skills Page**
* Grid showcasing my technical skills with icons

**Services Page**
* Cards listing the services I offer, each with a detailed description

**Projects Page**
* Showcase of completed projects with name, description, and technologies used

**Contact Page**
* Working contact form
* Direct email, phone, and GitHub contact details

**General**
* Reusable navbar and footer shared across all pages
* Fully responsive design for mobile and desktop

## Technologies Used

* Python
* Django
* HTML
* CSS
* SQLite

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
│ ├── admin.py
│ └── migrations/
├── static/
│ ├── css/
│ │ └── style.css
│ ├── files/
│ │ └── CV.pdf
│ └── images/
│ └── profile.png
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

5. Run migrations

   python manage.py makemigrations

   python manage.py migrate

6. Create a superuser (optional, for admin access)

   python manage.py createsuperuser

7. Run the development server

   python manage.py runserver

8. Open `http://127.0.0.1:8000/` in your browser

## Environment
Project configuration and sensitive settings are managed using environment variables.

## Author
Tayyaba Zafar