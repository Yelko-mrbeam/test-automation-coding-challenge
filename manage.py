import os

from app import create_app

app_instance = create_app()
app_instance.debug = True
app_instance.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4000)))
