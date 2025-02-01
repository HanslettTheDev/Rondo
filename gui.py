import os
import sys
import webview
from rondo import create_app


def get_resource_path(relative_path:str, folder:str = "rondo"):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), folder, relative_path)

app = create_app()

app.static_folder = get_resource_path("static") 
app.template_folder = get_resource_path("templates")


if __name__ == "__main__":
    webview.create_window("Rondo Management App", app, min_size=(1000, 700))
    webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = False
    webview.start(debug=True)