from maquetacion import MainFrame
from window import App

if __name__ == '__main__':

    app = App()
    app.title("URL SCANNER")
    frame = MainFrame(app)
    app.mainloop()