import os

class Config:
    # Secret key for session management
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")

    # Database connection string (to be set in Azure App Settings)
    SQL_CONNECTION_STRING = os.environ.get("SQL_CONNECTION_STRING")

    # Azure AD / MSAL config (placeholders for now)
    CLIENT_ID = os.environ.get("CLIENT_ID", "your-client-id")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "your-client-secret")
    AUTHORITY = os.environ.get("AUTHORITY", "https://login.microsoftonline.com/common")
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

# Default config object
config = Config()
