from PyQt5.QtWidgets import *
from PyQt5.uic import *
import resources

import sys


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        loadUi("login.ui", self)
        self.exit_.clicked.connect(self.__exit)
        self.login.clicked.connect(self.__login)

    def __login(self):
        user_name = self.user_name.text()
        user_password = self.user_password.text()
        remember = self.remember.isChecked()
        if len(user_name) <= 0 or len(user_password) <= 0:
            print("Fields must be filled")
        else:
            print("Welcome {}".format(user_name))

    def __exit(self):
        self.close()
        sys.exit(0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
