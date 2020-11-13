from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "this should not be visible!"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/app.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Other development config goes here
