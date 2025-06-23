# TEDxCUSAT Auth API

A simple, functional authentication system built as part of the TEDxCUSAT Technical Team recruitment task.  
It includes secure backend functionality with a minimal frontend for testing and demonstration. 

Deployed live using Render [here](https://tedx-auth-frontend.onrender.com/).

⚠️ If requests seem stuck or take unusually long, this is expected due to server cold starts (see [Important Notes](#️important-notes)).

Supports:
- Secure user registration and login  
- Password hashing (via Django's built-in system)  
- Role-based access (user/admin)  
- Admin-only features (user list, admin dashboard)  
- JWT authentication (access + refresh tokens)  
- Google OAuth2 login  
- Basic frontend for testing

---

## 🔧 Tech Stack

- **Backend**: Django, Django REST Framework, Simple JWT, social-auth-app-django  
- **Frontend**: Static HTML/JS/CSS (for testing)  
- **Database**: SQLite (default), easily swappable with PostgreSQL  
- **Deployment**: Tested on [Render](https://render.com/)

---

## ✅ Features Checklist

| Feature                         | Status   |
|--------------------------------|----------|
| Signup/Login with validation   | ✅ Done  |
| Password hashing               | ✅ Done (via Django) |
| Role-based access control      | ✅ Done (user/admin) |
| JWT authentication             | ✅ Done  |
| Token refresh endpoint         | ✅ Done  |
| Google OAuth login             | ✅ Done  |
| Admin-only endpoints           | ✅ Done  |
| Basic frontend for interaction | ✅ Done  |
| OAuth token returned to frontend | ✅ Done via redirect |
| Logout + frontend state clearing | ✅ Done  |

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Pseudozoid/tedx-auth-api.git
cd tedx-auth-api
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Add `.env` File
Create a .env file in the root directory. Use the `.env.example` for reference:
```env
DJANGO_SECRET_KEY=your-django-secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Run Migrations
```bash
python manage.py migrate
```

> This also creates a default admin user if configured in migrations.

### 6. Start the Server
```bash
python manage.py runserver
```

---

## 🌐 Google OAuth Setup
1. Go to https://console.cloud.google.com/apis/credentials

2. Create OAuth2 credentials:

    - Authorized redirect URL: `http://127.0.0.1:8000/oauth/complete/google-oauth2/`

3. Paste the Client ID and Secret into your `.env`.

## 🧪 Test Frontend

The static frontend (located at `index.html`) supports:

- Login/Signup  
- Google OAuth login  
- Token-based profile fetch  
- Admin-only dashboard  
- Token refresh and logout  

To use it:
1. Open `index.html` in your browser.  
2. Signup or login using credentials or Google OAuth.  
3. Use the buttons to interact with the API.

---

## 👥 Role-Based Access

- Every new user defaults to the `"user"` role.  
- Admins can access:
  - `/api/admin-area/` – Protected resource  
  - `/api/admin/users/` – List of all users  

The user role is included in every `/api/profile/` response.

### Default Admin Credentials
- Username: admin
- Mail: admin@example.com
- Password: admin123
---

## 🔒 Security Notes

- Passwords are stored securely using Django’s password hashing framework (PBKDF2 + salt).  
- JWT tokens are short-lived, and refresh logic is included on the frontend.  
- `.env` is used to manage secrets locally. Never commit secrets to version control.

---

## 🗂 Example `.env.example`

```env
DJANGO_SECRET_KEY=your-secret-key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## 📦 Deployment
- Tested on **Render** using:
  - **Gunicorn** as the WSGI server
  - Environment variables managed via the Render dashboard
  - **SQLite** for temporary development storage  
    (can be replaced with **PostgreSQL** for persistent storage)

## 📬 Contact

If something doesn't work as expected or if you have any questions, please reach out to me before judging the quality of my code :)

- 📧 Email: sarathmadhavr@gmail.com  
- 🐙 GitHub: [Pseudozoid](https://github.com/Pseudozoid) (just drop an issue in this repo)

I’ll be happy to help or clarify anything related to this project.

## ⚠️ Important Notes

- ⚙️ **Local Setup Caution**:  
  While this repo contains everything needed to run the project locally, doing so can be troublesome unless you're comfortable debugging Django + OAuth-related issues.  
  Certain configurations (especially related to environment variables, Google OAuth client setup, and redirect URIs) are **system-specific**, and errors may occur if not configured correctly.

- 🚀 **Hosted Deployment Warning**:  
  The project is deployed on [Render](https://render.com) using the **free plan** for the purpose of demonstration, which means:
  - Cold starts may cause slow initial responses.
  - There might be occasional delays or temporary unavailability due to limited free-tier resources.
  
  These issues are expected under the free plan. Please be patient when testing the hosted version.

  ---

> Made with ❤️ by Pseudozoid


