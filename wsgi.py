import settings
from src import create_app

app = create_app(settings)

if __name__ == "__main__":
    app.run()
