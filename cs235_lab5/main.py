"""Web server entry point.

Note: 
Since we have defined all environment variables, we do NOT call `app.run()` and 
`python main.py` will not run the Flask server.
"""

from distutils.log import debug
from app import create_app

app = create_app()
