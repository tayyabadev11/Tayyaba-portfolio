from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def skills(request):
    return render(request, 'skills.html')
def services(request):
    return render(request, 'services.html')
def projects(request):
    projects_list = [
        {
            'title': 'Noodle Store',
            'image': 'images/projects/noodle-store.png',
            'description': "Noodle Store is a Django-based web application built to showcase and manage a catalog of noodle products for an online food store. Visitors can browse through available noodle varieties, view individual product pages with full details such as name, description, price and category, and explore items organized by category for easier navigation. On the backend, a fully functional Django admin panel lets an administrator add new products, update listings, upload images, and manage the catalog without touching any code.",
            'features': ['View Noodle Products', 'Product Details Page', 'Product Categories', 'Product Images', 'Django Admin Panel'],
            'tech': ['Python', 'Django', 'HTML', 'CSS', 'SQLite'],
            'status': 'completed',
            'live_link': '',
            'repo_link': 'https://github.com/tayyabadev11/noodle-store',
            'demo_images': [],
        },
        {
            'title': 'Job Portal',
            'image': 'images/projects/job-portal.png',
            'description': "Job Portal is a Django-based web application designed to connect employers with job seekers in a simple and organized way. Employers can create an account, post job openings with details such as title, company, location, salary, and description, and manage their listings from a personal dashboard. Job seekers can browse available jobs, search by title, and apply directly by submitting a cover letter along with their resume, with role-based access keeping each user's experience secure and relevant.",
            'features': ['Role-Based Access (Employer/Seeker)', 'Post & Manage Jobs', 'Search Jobs', 'Apply with Resume & Cover Letter', 'My Jobs / My Applications Dashboard', 'Django Admin Panel'],
            'tech': ['Python', 'Django', 'HTML', 'CSS', 'SQLite'],
            'status': 'completed',
            'live_link': '',
            'repo_link': 'https://github.com/tayyabadev11/job-portal',
            'demo_images': [],
        },
        {
            'title': 'Personal Portfolio Website',
            'image': 'images/projects/portfolio.png',
            'description': "This is a personal portfolio website built with Django to present my background, skills, services, and projects as a BS Artificial Intelligence student and web developer. It features a home page with a hero introduction, an about section with profile picture and background, a dedicated skills section, a services page, a projects page showcasing completed work, and a contact page for visitors to get in touch — all following a clean, reusable template structure with a custom black and red theme.",
            'features': ['Hero Banner & Skills Preview', 'About Page with CV Download', 'Skills Showcase', 'Services Page', 'Projects Showcase', 'Working Contact Form'],
            'tech': ['Python', 'Django', 'HTML', 'CSS', 'SQLite'],
            'status': 'completed',
            'live_link': '',
            'repo_link': 'https://github.com/tayyabadev11/Tayyaba-portfolio',
            'demo_images': [],
        },
    ]
    return render(request, 'projects.html', {'projects': projects_list})
def contact(request):
    return render(request, 'contact.html')
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed successfully!")
        else:
            messages.error(request, "This email is already subscribed or invalid.")
    return redirect(request.META.get('HTTP_REFERER', '/'))