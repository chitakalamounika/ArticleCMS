# ArticleCMS – Azure Deployment Proof

This document provides verification of the **cloud deployment setup** for the ArticleCMS project.  
It includes screenshots from the Azure portal showing that all required resources were created and integrated.

---

## ✅ Azure Resources Setup

### 1. Resource Group
All resources are organized under a dedicated resource group for easy management.  

![Resource Group](screenshots/resource_group.png)

---

### 2. Storage Container
Blob storage created to store application files and static assets.  

![Storage Container](screenshots/storage_container.png)

---

### 3. Azure SQL Database
Configured SQL Database used by the Flask web app for content storage.  

![SQL Database](screenshots/sql_db.png)

---

### 4. Web App
Flask application deployed as an **Azure App Service**.  

![Web App](screenshots/web_app.png)

---

### 5. Logging Configuration
Application logging is enabled in Azure to monitor and troubleshoot.  

![Logging](screenshots/logging.png)

---

### 6. Redirect URI Setup (Authentication)
Redirect URI configured for authentication (if OAuth / identity provider is enabled).  

![Redirect URI](screenshots/redirect_uri.png)
