import webview
from rondo import create_app

app = create_app()

if __name__ == "__main__":
    try:
        webview.create_window("Rondo Management App", app, min_size=(1000, 700))
        webview.start()
    except Exception as e:
        with open("error.txt", "w") as file:
            file.write(e)