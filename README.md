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
Clone the repository and set up a virtual environment:

#### Windows
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### macOS / Linux
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
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

## 🧊 Static Site Generation
To host your portfolio for free on **GitHub Pages**, you can convert this dynamic Flask app into static HTML.

### 1. Update Content
Always run the local server to update your content via the Admin panel:
```bash
python app.py
```
Go to `http://127.0.0.1:5000/admin`, log in, and make your changes.

### 2. Generate Static Files
Once you are happy with the content, run the freeze script:
```bash
python freeze.py
```
This will generate a `docs/` folder containing your complete portfolio as HTML files.

### 3. Deploy
Upload the contents of the `docs/` folder to your GitHub repository (or the `docs/` folder if configured for GitHub Pages).

### 4. Contact Form Note
The static site uses **Formspree** for the contact form. Make sure to update the `action` URL in `templates/index.html` with your own Formspree ID before deploying.

## 📄 License

Created by Lokesh.This project is open-source and available under the [MIT License](LICENSE). 
