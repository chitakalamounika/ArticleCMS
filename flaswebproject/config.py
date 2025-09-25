import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")

    # Azure SQL connection string
    SQL_CONNECTION_STRING = os.environ.get("SQL_CONNECTION_STRING")

    # Blob Storage
    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT")
    BLOB_STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY")
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER")

    # MSAL Authentication
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    AUTHORITY = os.environ.get("AUTHORITY")  # e.g., https://login.microsoftonline.com/<tenant_id>
    CLIENT_ID = os.environ.get("CLIENT_ID")
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
