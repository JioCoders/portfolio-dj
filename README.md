# 🌐 Django Portfolio Website

A simple portfolio website built with **Django**, styled with custom CSS and JavaScript.  
This project demonstrates how to create and deploy a Django app to production using free hosting (Render).

---

## 🚀 Features
- Django-based portfolio website
- Custom **HTML templates**
- Static files support (**CSS, JS, Images**)
- Mobile-friendly responsive design
- Ready for **production deployment** with Whitenoise + Gunicorn
- Supports free deployment on [Render](https://render.com)

---

## 🛠️ Installation & Setup (Local)

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/portfolio_dj.git
cd portfolio_dj
```

2. Create & activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
```
3. Install dependencies
`pip install -r requirements.txt`

4. Run migrations
`python manage.py migrate`

5. Start development server
`python manage.py runserver`


Visit 👉 http://127.0.0.1:8000/

🗂️ Project Structure
portfolio_dj/           # Main Django project
│── portfolio/          # Django app (views, urls, templates)
│── static/             # Static files (css, js, images)
│── templates/          # Base templates
│── manage.py
│── requirements.txt
│── Procfile
│── README.md

⚡ Deployment (Render Free Hosting)

Push project to GitHub

Create a free Render
 account

Create New Web Service and connect your GitHub repo

Configure build & start commands:

Build Command:

`pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`


Start Command:

`gunicorn portfolio_dj.wsgi`


Set environment variables in Render:
```
DJANGO_SECRET_KEY

DJANGO_DEBUG=False

DJANGO_ALLOWED_HOSTS=your-app.onrender.com
```

📸 Screenshots (Optional)

Add a screenshot of your portfolio here

📜 License

This project is licensed under the MIT License – feel free to use and modify it.

👨‍💻 Author

Jiocoders
🔗 GitHub | Portfolio

---

👉 Lator on also include a **GitHub Actions workflow (`deploy.yml`)** so app will auto-deploys to Render every time after push code.
