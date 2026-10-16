from dotenv import load_dotenv

from tabvio_web.config import PROJECT_DIRECTORY

load_dotenv(dotenv_path=PROJECT_DIRECTORY / ".env", override=True)

from tabvio_web.server.routes import app

__all__ = ["app"]
