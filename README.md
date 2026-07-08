# Attendance System

A Flask-based attendance system with:
- user registration and login
- attendance record storage
- editing and deleting attendance records
- help desk requests
- dashboard view for monitoring records

## Run locally

1. Create a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app
   ```bash
   python app.py
   ```
4. Open your browser at
   ```text
   http://127.0.0.1:5000
   ```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Deploy to GitHub

1. Initialize Git
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. Create a repository on GitHub.
3. Connect the remote
   ```bash
   git remote add origin https://github.com/your-username/your-repo-name.git
   git branch -M main
   git push -u origin main
   ```

## Deploy to Render

1. Push your project to GitHub.
2. Open Render and create a new Web Service.
3. Connect your GitHub repository.
4. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn wsgi:app`
   - Environment Variable: `SECRET_KEY=your-secret-key`
5. Click Create Web Service.

## Deploy to Heroku

```bash
heroku create
heroku git:remote -a your-heroku-app-name
heroku config:set SECRET_KEY=your-secret-key
git push heroku main
```
