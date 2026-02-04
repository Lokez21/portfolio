# 🚀 Modern Flask Portfolio CMS

A sleek, professional, and fully configurable portfolio website built with **Flask**, **SQLite**, and **Bootstrap 5**. This project features a built-in CMS for easy content management and a highly interactive frontend with modern UI effects.

## ✨ Features

- **Dynamic CMS**: Powered by `Flask-Admin`. Manage your Bio, Education, Experience, and Projects without touching code.
- **Interactive Hero Section**:
  - Animated waving hand emoji.
  - Multi-speed **Parallax scrolling** effect.
  - Sequential cascading entrance animations.
- **Project Detail Pages**: Dedicated pages for each project with breadcrumb navigation.
- **Toast Notifications**: Modern Bootstrap overlays for contact form submissions.
- **Security**: Robust **CSRF Protection** enabled via `Flask-WTF` for all form submissions.
- **Social Media Integration**: Conditionally rendered LinkedIn and GitHub links in the splash section.
- **Responsive Design**: Fully mobile-friendly using Bootstrap 5.
- **Dynamic Footer**: Auto-updating copyright year via JavaScript.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite, SQLAlchemy (ORM)
- **Admin Panel**: Flask-Admin
- **Frontend**: HTML5, Vanilla CSS, Bootstrap 5, FontAwesome
- **Animations**: CSS Keyframes, JavaScript Scroll Handlers

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8+
- pip (Python package manager)

### 2. Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Database Setup
Initialize the database and populate it with seed data:
```bash
python seed_data.py
```
*Note: This will create a `site.db` file in the project directory.*

### 4. Run the Application
Start the development server:
```bash
python app.py
```
The site will be available at `http://127.0.0.1:5000`.

## ⚙️ Content Management (CMS)

Access the admin dashboard at:
Access the admin dashboard at:
`http://127.0.0.1:5000/admin`

> [!WARNING]
> **Default Credentials**
>
> -   **Username:** `admin`
> -   **Password:** `admin123`
>
> **Security Notice:** Please change these credentials immediately after your first login. The system enforces a strong password policy: minimum 10 characters, combining letters, numbers, and symbols.

From here, you can easily modify:
- **About**: Update your name, job title, email, bio, profile image, and social links.
- **Education/Experience**: Add or edit your professional and academic history.
- **Projects**: Add new projects with blurbs, long descriptions, and images.

## 📄 License

Created by Lokesh.This project is open-source and available under the [MIT License](LICENSE). 
