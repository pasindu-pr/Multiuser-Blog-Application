from webapp import create_app
from dotenv import find_dotenv, load_dotenv
import os

app = create_app()
load_dotenv(find_dotenv())

debug = False

if os.environ.get("ENVIRONMENT") == "development":
    debug = True

if __name__ == "__main__":
    app.run(debug=debug)