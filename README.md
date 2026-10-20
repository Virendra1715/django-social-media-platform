# 🚀 Django Social Media Platform

A full-stack social media web application built using Django, Python, HTML, CSS, and JavaScript.

The application allows users to create accounts, manage their profiles, publish posts, upload images, like posts, follow other users, explore content, and search for users.

This project is currently in the Django development phase. The next stages will focus on improving the existing application, integrating Django REST Framework (DRF), implementing JWT authentication, exploring AI/ML-powered features, and deploying the application.

---

## 📌 Project Overview

The primary goal of this project is to develop a social media platform while strengthening my understanding of Django web development, database management, authentication, and full-stack application architecture.

I am building this project incrementally, starting with a traditional Django application using server-rendered HTML templates.

The long-term goal is to evolve the project into a more scalable application with RESTful APIs, token-based authentication, a modern frontend, and intelligent features powered by machine learning.

---

## ✨ Current Features

The following features have been implemented in the current version of the project.

### 1. User Authentication
- User registration and login.
- User logout.
- Authentication using Django's authentication system.
- Access to authenticated user functionality.

### 2. User Profiles
- Individual user profiles.
- Profile information management.
- Profile editing.
- Profile image upload.
- User location and bio fields.

### 3. Posts and Content Sharing
- Create posts.
- Upload images with posts.
- Add captions to posts.
- Display posts through HTML templates.
- Store post information in the database.

### 4. Social Interactions
- Like posts.
- Follow other users.
- Store like and follow relationships.
- View user profiles and their content.

### 5. Explore and Search
- Explore page for discovering content.
- Search functionality for finding users or relevant content.

### 6. Database Management
- Django ORM for database operations.
- SQLite database for local development.
- Django models for managing users, profiles, posts, likes, and followers.
- Database migrations for tracking schema changes.

### 7. Frontend Development
- HTML for page structure.
- CSS for styling and layout.
- JavaScript for client-side interactions.
- Django templates for rendering dynamic content.

---

## 🛠️ Technology Stack

### Current Technologies

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Web framework and application backend |
| Django ORM | Database operations |
| SQLite | Local development database |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive layouts |
| JavaScript | Client-side interactions |
| Django Templates | Dynamic HTML rendering |
| Git | Version control |
| GitHub | Source code hosting and project management |

### Planned Technologies

| Technology | Planned Purpose |
|---|---|
| Django REST Framework (DRF) | Build RESTful APIs |
| JWT Authentication | Token-based authentication for API clients |
| React | Build a modern frontend that communicates with the backend API |
| PostgreSQL | Explore a production-oriented relational database |
| Machine Learning | Introduce intelligent and personalized features |
| Scikit-learn | Develop classical ML-based functionality where appropriate |
| Docker | Containerize the application |
| Cloud Hosting | Deploy the application for public access |
| API Documentation Tools | Document and test REST API endpoints |

These technologies are part of the roadmap and are not necessarily implemented in the current version.

---

## 🏗️ Project Structure

The project currently follows a Django project-and-app structure.

```text
django-social-media-platform/
│
├── socialmedia/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── userauth/
│   ├── migrations/
│   ├── templates/
│   │   ├── edit_profile.html
│   │   ├── explore.html
│   │   ├── loginn.html
│   │   ├── logout.html
│   │   ├── main.html
│   │   ├── modal.html
│   │   ├── profile.html
│   │   ├── profile_upload.html
│   │   ├── search.html
│   │   └── signup.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
