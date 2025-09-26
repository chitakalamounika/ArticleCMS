# Article CMS (Flask + Azure)

A simple **Content Management System (CMS)** built with Flask.  
It uses **Azure SQL Database** for storing articles and **Azure Blob Storage** for images.  
Deployed on **Azure App Service** with GitHub Actions CI/CD.  

---

## 🚀 Tech Stack
- Python (Flask)  
- Azure SQL Database  
- Azure Blob Storage  
- Azure App Service  
- Bootstrap 5  

---

## ⚙️ Local Setup

### 1. Clone repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Linux/Mac:
```bash
export SECRET_KEY="supersecretkey"
export SQL_CONNECTION_STRING="Driver={ODBC Driver 18 for SQL Server};Server=tcp:<your-sql-server>.database.windows.net,1433;Database=<your-db>;Uid=<your-admin-user>;Pwd=<your-password>;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
export BLOB_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=<yourstorageaccount>;AccountKey=<youraccountkey>;EndpointSuffix=core.windows.net"
export BLOB_CONTAINER="cms"
export BLOB_URL="https://<yourstorageaccount>.blob.core.windows.net/cms"
```

Windows (PowerShell):
```powershell
$env:SECRET_KEY="supersecretkey"
$env:SQL_CONNECTION_STRING="Driver={ODBC Driver 18 for SQL Server};Server=tcp:<your-sql-server>.database.windows.net,1433;Database=<your-db>;Uid=<your-admin-user>;Pwd=<your-password>;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
$env:BLOB_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=<yourstorageaccount>;AccountKey=<youraccountkey>;EndpointSuffix=core.windows.net"
$env:BLOB_CONTAINER="cms"
$env:BLOB_URL="https://<yourstorageaccount>.blob.core.windows.net/cms"
```

### 5. Run the app
```bash
export FLASK_APP=FlaskWebProject
flask run --host=0.0.0.0 --port=5000
```

Open in browser:  
👉 `http://127.0.0.1:5000`

---

## ☁️ Deployment to Azure

### 1. Push code to GitHub
```bash
git add .
git commit -m "Deploy CMS"
git push origin main
```

### 2. Configure GitHub Secrets
- Go to Azure App Service → **Get Publish Profile**.  
- In GitHub repo → **Settings → Secrets → Actions → New repository secret**.  
  - Name: `AZURE_WEBAPP_PUBLISH_PROFILE`  
  - Value: paste the publish profile XML.  

### 3. Workflow file (`.github/workflows/deploy.yml`)
```yaml
name: Deploy Flask CMS to Azure Web App

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Deploy to Azure Web App
        uses: azure/webapps-deploy@v2
        with:
          app-name: "<your-app-service-name>"
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          package: .
```

### 4. Configure App Service → Settings → Configuration
Add these keys:  
- `SECRET_KEY`  
- `SQL_CONNECTION_STRING`  
- `BLOB_CONNECTION_STRING`  
- `BLOB_CONTAINER` (`cms`)  
- `BLOB_URL`  

### 5. Visit your live app
👉 `https://<your-app-service>.azurewebsites.net`

## 📸 Screenshots

### 1. Local Flask App Running
![Local Run](screenshots/local_run.png)

### 2. Azure SQL Database
![Azure SQL](screenshots/azure_sql.png)

### 3. Azure Blob Storage
![Blob Storage](screenshots/blob_storage.png)

### 4. Deployed App
![Deployed App](screenshots/deployed_app.png)


---

## ✅ Screenshots to Collect
- Terminal: `flask run` working  
- Browser: `http://127.0.0.1:5000` homepage  
- Azure SQL Database overview & query editor  
- Azure Blob container with images  
- Azure App Service overview & settings  
- Live deployed app in browser  
