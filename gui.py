import webview
from rondo import create_app

app = create_app()

if __name__ == "__main__":
    print(app.config.values())
    print(app.static_folder)
    webview.create_window("Rondo Management App", app, min_size=(1000, 700))
    webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = False
    webview.start(debug=True)