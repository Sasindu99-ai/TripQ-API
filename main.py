from pathlib import Path

from vvecon.zorion import App

app = App(Path(__file__).resolve().parent)
asgi = app.asgi()
wsgi = app.wsgi()

if __name__ == '__main__':
    app.run()
