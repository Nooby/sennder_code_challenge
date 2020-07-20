from flask import Flask

app = Flask(__name__)

from app import main  # noqa: Import not at top of file.
