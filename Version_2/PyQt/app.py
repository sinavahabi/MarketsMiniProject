"""
    Program: Market Status Application
    Author: sina vahabi
    Copyright: 2023/03
    'Version 2.0'
"""

# Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
# Commands:
# pip install PyQt5

import sys
from PyQt5.QtWidgets import (QApplication, QTabWidget, QTextEdit, QWidget, QFormLayout,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QMessageBox)
from PyQt5.QtGui import QIcon
# Importing 'DataBase()' classe from database.py module.
from MarketsMiniProject.Version_2.database import DataBase


# Instantiating main class 'App()' which inheritance from 'QTabWidget()'.
class App(QTabWidget):
    def __init__(self):
        super(App, self).__init__()
        # Instantiating class object.
        self.db = DataBase()
        # Instantiating 'QLineEdit()' objects and setting them to ReadOnly.
        self.crypto_currency_text = QLineEdit('Click on the option you want, to see the status:')
        self.crypto_currency_text.setReadOnly(True)
        self.local_market_text = QLineEdit('Click on the option you want, to see the status:')
        self.local_market_text.setReadOnly(True)
        # Instantiating 'QTextEdit()' objects and setting them to ReadOnly.
        self.crypto_currency_result = QTextEdit()
        self.crypto_currency_result.setReadOnly(True)
        self.local_market_result = QTextEdit()
        self.local_market_result.setReadOnly(True)
        self.welcome_text = QTextEdit()
        self.welcome_text.setReadOnly(True)
        # Instantiating 'QWidget()' objects.
        self.welcome_tab = QWidget()
        self.crypto_currency_tab = QWidget()
        self.local_market_tab = QWidget()
        # Adding Tabs.
        self.addTab(self.welcome_tab, "Welcome")
        self.addTab(self.crypto_currency_tab, "Crypto Currency Market")
        self.addTab(self.local_market_tab, "Iran Local Market")
        # Calling tabs methods.
        self.WelcomeTab()
        self.CryptoCurrencyTab()
        self.LocalMarketTab()
        # Instantiating program UI.
        self.setWindowTitle('Market App')
        self.setWindowIcon(QIcon('Icons/Main.png'))
        self.resize(800, 600)
        self.setMinimumSize(800, 600)

    # Defining Crypto Currency Market tab method.
    def CryptoCurrencyTab(self):
        # Creating 'QFormLayout()' object.
        layout = QFormLayout()
        # Removing some extra spaces.
        layout.setContentsMargins(0, 0, 0, 0)
        # Creating horizontal and vertical layouts.
        horizontal = QHBoxLayout()
        vertical = QVBoxLayout()
        # Adding 'QTextEdit()' Object Widget.
        vertical.addWidget(self.crypto_currency_result)

        # Bitcoin button.
        # Creating 'QPushButton()' object.
        btc_btn = QPushButton('1. Bitcoin')
        # Adding 'QPushButton()' object Widget Horizontally.
        horizontal.addWidget(btc_btn)
        # Setting button icon.
        btc_btn.setIcon(QIcon('Icons/Bitcoin.png'))
        # Setting a button shortcut
        btc_btn.setShortcut('Ctrl+1')
        # Setting a tool tip for button, so that when mouse hovers on the button, user will see a hint message.
        btc_btn.setToolTip('Ctrl+1: <b>Bitcoin Price</b>')
        # Connecting 'QPushButton()' object to 'clicked()' method, by passing 'bitcoin()' method on it.
        # By doing this we specify the action that has to be done after user clicked on the button.
        btc_btn.clicked.connect(self.bitcoin)

        # Ethereum button.
        eth_btn = QPushButton('2. Ethereum')
        horizontal.addWidget(eth_btn)
        eth_btn.setIcon(QIcon('Icons/Ethereum.png'))
        eth_btn.setShortcut('Ctrl+2')
        eth_btn.setToolTip('Ctrl+2: <b>Ethereum Price</b>')
        eth_btn.clicked.connect(self.ethereum)

        # Binance Coin button.
        bnb_btn = QPushButton('3. Binance Coin')
        horizontal.addWidget(bnb_btn)
        bnb_btn.setIcon(QIcon('Icons/Binance.png'))
        bnb_btn.setShortcut('Ctrl+3')
        bnb_btn.setToolTip('Ctrl+3: <b>Binance Coin Price</b>')
        bnb_btn.clicked.connect(self.binance)

        # Quit button.
        quit_btn = QPushButton('Quit')
        horizontal.addWidget(quit_btn)
        quit_btn.setIcon(QIcon('Icons/Quit.png'))
        quit_btn.setShortcut('Ctrl+Q')
        quit_btn.setToolTip('Use <b>\'Ctrl+Q\'</b> to quit')
        # Connecting 'QPushButton()' object to 'clicked()' method, by passing 'self.close()' on it, which is a built-in
        # method from 'QWidget()' class. 'close()' method will immediately close the app when related button is clicked.
        quit_btn.clicked.connect(self.close)

        # Adding rows to 'QFormLayout()' object and passing required values to it.
        # Adding 'QLineEdit' object as a row to 'QFormLayout()' object.
        layout.addRow(self.crypto_currency_text)
        # Adding 'QTextEdit' (which has been added as a widget to vertical layout)
        # object, as a row to 'QFormLayout()' object.
        layout.addRow(vertical)
        # Adding 'QLabel' object as a row to 'QFormLayout()' object which going to be set in horizontal layout.
        layout.addRow(QLabel('Choose: '), horizontal)
        # setting 'QWidget()' object layout (main layout). by passing final changes of 'QFormLayout()', we specify
        # parameters and their layout in this tab.
        self.crypto_currency_tab.setLayout(layout)
        # Notice that main class ('App()') has inheritance from 'QTabWidget()' class.

    # Defining Iran Local Market tab method.
    def LocalMarketTab(self):
        layout = QFormLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        horizontal = QHBoxLayout()
        vertical = QVBoxLayout()
        vertical.addWidget(self.local_market_result)

        # 18-Karat Gold button.
        gold_btn = QPushButton('1. 18 Karat Gold')
        horizontal.addWidget(gold_btn)
        gold_btn.setIcon(QIcon('Icons/Gold.png'))
        gold_btn.setShortcut('Ctrl+1')
        gold_btn.setToolTip('Ctrl+1: <b>Gold Price</b>')
        gold_btn.clicked.connect(self.gold)

        # Gold Coin button.
        gold_coin_btn = QPushButton('2. Gold Coin')
        horizontal.addWidget(gold_coin_btn)
        gold_coin_btn.setIcon(QIcon('Icons/GoldCoin.png'))
        gold_coin_btn.setShortcut('Ctrl+2')
        gold_coin_btn.setToolTip('Ctrl+2: <b>Gold Coin Price</b>')
        gold_coin_btn.clicked.connect(self.gold_coin)

        # Dollar button.
        dollar_btn = QPushButton('3. US Dollar')
        horizontal.addWidget(dollar_btn)
        dollar_btn.setIcon(QIcon('Icons/Dollar.png'))
        dollar_btn.setShortcut('Ctrl+3')
        dollar_btn.setToolTip('Ctrl+3: <b>Dollar Price</b>')
        dollar_btn.clicked.connect(self.dollar)

        # Total Index of Iran Stock Exchange button.
        stock_market_btn = QPushButton('4. Total Index of Iran Stock Exchange')
        horizontal.addWidget(stock_market_btn)
        stock_market_btn.setIcon(QIcon('Icons/StockExchange.png'))
        stock_market_btn.setShortcut('Ctrl+4')
        stock_market_btn.setToolTip('Ctrl+4: <b>Total Index of Iran Stock Exchange Amount</b>')
        stock_market_btn.clicked.connect(self.stock_market)

        # Quit button.
        quit_btn = QPushButton('Quit')
        horizontal.addWidget(quit_btn)
        quit_btn.setIcon(QIcon('Icons/Quit.png'))
        quit_btn.setShortcut('Ctrl+Q')
        quit_btn.setToolTip('Use <b>\'Ctrl\'+Q</b> to quit')
        quit_btn.clicked.connect(self.close)

        layout.addRow(self.local_market_text)
        layout.addRow(vertical)
        layout.addRow(QLabel('Choose: '), horizontal)
        self.local_market_tab.setLayout(layout)

    # Defining Welcome tab method.
    def WelcomeTab(self):
        layout = QFormLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        vertical = QVBoxLayout()
        vertical.addWidget(self.welcome_text)

        # Quit button
        quit_btn = QPushButton('Quit')
        vertical.addWidget(quit_btn)
        quit_btn.setIcon(QIcon('Icons/Quit.png'))
        quit_btn.setShortcut('Ctrl+Q')
        quit_btn.setToolTip('Use <b>\'Ctrl+Q\'</b> to quit')
        quit_btn.clicked.connect(self.close)

        # Setting welcome text by 'setHtml()' method.
        self.welcome_text.setHtml("<font color='red' size='3'><red>'~~~~~~~~~~~~~~ Welcome to Market App ~~~~~~~~~~~~~~~'")

        layout.addRow(vertical)
        self.welcome_tab.setLayout(layout)

    # Defining 'bitcoin()' method. this method specifies the actions which will occur when Bitcoin button is clicked and
    # this method is being called.
    def bitcoin(self):
        # Calling 'btc_api()' method from object that was instantiated from 'DataBase()' class.
        self.db.btc_api()
        # Creating 'QMessageBox()' object.
        message = QMessageBox()
        # If returned value from web was empty by the try except method from 'api.py' module, then show this message
        if self.db.btc_price == '':
            # Setting 'QMessageBox()' object Icon as informational method.
            message.setIcon(QMessageBox.Information)
            # Setting 'QMessageBox()' object text that will be shown to user.
            message.setText('something wen\'t wrong!')
            # Setting 'QMessageBox()' object text title that will be shown to user.
            message.setWindowTitle('server error!')
            # Setting 'QMessageBox()' object window icon.
            message.setWindowIcon(QIcon('Icons/Error.png'))
            # Setting standard 'Ok' button.
            message.setStandardButtons(QMessageBox.Ok)
            # application will keep running no matter which option they choose.
            message.exec_()
            self.local_market_result.setPlainText('we\'re not able to show the results at the moment,'
                                                  ' please try again later!')
        else:
            # Setting 'QTextEdit()' object text with 'setPlainText()' method.
            self.crypto_currency_result.setPlainText('Bitcoin price is: ' + str(self.db.btc_price) +
                                                     ' $' + ' at this moment.')

            message.setIcon(QMessageBox.Information)
            message.setText('Do you want to save Bitcoin price result into the DataBase as well?')
            message.setWindowTitle('Inserting BTC status to DB!')
            message.setWindowIcon(QIcon('Icons/Bitcoin.png'))
            # Setting standard 'Yes' or 'No' buttons.
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            # Creating a variable and passing 'message.exec_()' to it, so every time that this message is shown to user,
            # application will keep running no matter which option they choose.
            return_value = message.exec_()
            if return_value == QMessageBox.Yes:
                # If user agrees to insert result's data into DataBase, we call program run count and DataBase methods.
                self.db.bitcoin_run_count()
                self.db.bitcoin_run_count_reader()
                self.db.btc_mongo_db()
            else:
                # Otherwise if they chose 'No' option, program run count and DataBase methods won't be called and
                # application will continue running
                return return_value

    # Defining 'ethereum()' method. this method specifies the actions which will occur when Ethereum button is clicked
    # and this method is being called.
    def ethereum(self):
        self.db.eth_api()
        message = QMessageBox()
        # If returned value from web was empty by the try except method from 'api.py' module, then show this message
        if self.db.eth_price == '':
            message.setIcon(QMessageBox.Information)
            message.setText('something wen\'t wrong!')
            message.setWindowTitle('server error!')
            message.setWindowIcon(QIcon('Icons/Error.png'))
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
            self.local_market_result.setPlainText('we\'re not able to show the results at the moment,'
                                                  ' please try again later!')
        else:
            self.crypto_currency_result.setPlainText('Ethereum price is: ' + str(self.db.eth_price) +
                                                     ' $' + ' at this moment.')
            message.setIcon(QMessageBox.Information)
            message.setText('Do you want to save Ethereum price result into the DataBase as well?')
            message.setWindowTitle('Inserting ETH status to DB!')
            message.setWindowIcon(QIcon('Icons/Ethereum.png'))
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            return_value = message.exec_()
            if return_value == QMessageBox.Yes:
                self.db.ethereum_run_count()
                self.db.ethereum_run_count_reader()
                self.db.eth_mongo_db()
            else:
                return return_value

    # Defining 'binance()' method. this method specifies the actions which will occur when Binance Coin button is
    # clicked and this method is being called.
    def binance(self):
        self.db.bnb_api()
        message = QMessageBox()
        # If returned value from web was empty by the try except method from 'api.py' module, then show this message
        if self.db.bnb_price == '':
            message.setIcon(QMessageBox.Information)
            message.setText('something wen\'t wrong!')
            message.setWindowTitle('server error!')
            message.setWindowIcon(QIcon('Icons/Error.png'))
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
            self.local_market_result.setPlainText('we\'re not able to show the results at the moment,'
                                                  ' please try again later!')
        else:
            self.crypto_currency_result.setPlainText('BNB price is: ' + str(self.db.bnb_price) +
                                                     ' $' + ' at this moment.')
            message.setIcon(QMessageBox.Information)
            message.setText('Do you want to save Binance Coin price result into the DataBase as well?')
            message.setWindowTitle('Inserting BNB status to DB!')
            message.setWindowIcon(QIcon('Icons/Binance.png'))
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            return_value = message.exec_()
            if return_value == QMessageBox.Yes:
                self.db.bnb_run_count()
                self.db.bnb_run_count_reader()
                self.db.bnb_mongo_db()
            else:
                return return_value

    # Defining 'gold()' method. this method specifies the actions which will occur when 18-Karat Gold button is clicked
    # and this method is being called.
    def gold(self):
        self.db.gold_api()
        message = QMessageBox()
        # If returned value from web was empty by the try except method from 'api.py' module, then show this message
        if self.db.gold_price == '':
            message.setIcon(QMessageBox.Information)
            message.setText('something wen\'t wrong!')
            message.setWindowTitle('server error!')
            message.setWindowIcon(QIcon('Icons/Error.png'))
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
            self.local_market_result.setPlainText('we\'re not able to show the results at the moment,'
                                                  ' please try again later!')
        else:
            self.local_market_result.setPlainText('18 Karat Gold price in Iran is: ' + str(self.db.gold_price) +
                                                  ' Rials' + ' at this moment.')
            message.setIcon(QMessageBox.Information)
            message.setText('Do you want to save 18 Karat Gold price result into the DataBase as well?')
            message.setWindowTitle('Inserting 18-Karat Gold status to DB!')
            message.setWindowIcon(QIcon('Icons/Gold.png'))
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            return_value = message.exec_()
            if return_value == QMessageBox.Yes:
                self.db.gold_run_count()
                self.db.gold_run_count_reader()
                self.db.gold_mongo_db()
            else:
                return return_value

    # Defining 'gold_coin()' method. this method specifies the actions which will occur when Gold Coin button is clicked
    # and this method is being called.
    def gold_coin(self):
        self.db.gold_coin_api()
        message = QMessageBox()
        # If returned value from web was empty by the try except method from 'api.py' module, then show this message
        if self.db.gold_coin_price == '':
            message.setIcon(QMessageBox.Information)
            message.setText('something wen\'t wrong!')
            message.setWindowTitle('server error!')
            message.setWindowIcon(QIcon('Icons/Error.png'))
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
            self.local_market_result.setPlainText('we\'re not able to show the results at the moment,'
                                                  ' please try again later!')
        else:
            self.local_market_result.setPlainText('Gold Coin price in Iran is: ' + str(self.db.gold_coin_price) +
                                                  ' Rials' + ' at the moment.')
            message.setIcon(QMessageBox.Information)
            message.setText('Do you want to save Gold Coin price result into the DataBase as well?')
            message.setWindowTitle('Inserting Gold Coin status to DB!')
            message.setWindowIcon(QIcon('Icons/GoldCoin.png'))
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            return_value = message.exec_()
            if return_value == QMessageBox.Yes:
                self.db.gold_coin_run_count()
                self.db.gold_coin_run_count_reader()
                self.db.gold_coin_mongo_db()
            else:
                return return_value

    # Defining 'dollar()' method. this method specifies the actions which will occur when dollar button is clicked and
    # this method is being called.
    def dollar(self):
        self.db.dollar_api()
        message = QMessageBox()
        # If returned value from web was empty by the try except method from 'api.py' module, then show this message
        if self.db.dollar_price == '':
            message.setIcon(QMessageBox.Information)
            message.setText('something wen\'t wrong!')
            message.setWindowTitle('server error!')
            message.setWindowIcon(QIcon('Icons/Error.png'))
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
            self.local_market_result.setPlainText('we\'re not able to show the results at the moment,'
                                                  ' please try again later!')
        else:
            self.local_market_result.setPlainText('US Dollar price in Iran is: ' + str(self.db.dollar_price) +
                                                  ' Rials' + ' at the moment.')
            message.setIcon(QMessageBox.Information)
            message.setText('Do you want to save US Dollar price result into the DataBase as well?')
            message.setWindowTitle('Inserting US Dollar status to DB!')
            message.setWindowIcon(QIcon('Icons/Dollar.png'))
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            return_value = message.exec_()
            if return_value == QMessageBox.Yes:
                self.db.dollar_run_count()
                self.db.dollar_run_count_reader()
                self.db.dollar_mongo_db()
            else:
                return return_value

    # Defining 'stock_market()' method. this method specifies the actions which will occur when
    # Total Index of Iran Stock Exchange button is clicked and this method is being called.
    def stock_market(self):
        self.db.stock_market_api()
        message = QMessageBox()
        # If returned value from web was empty by the try except method from 'api.py' module, then show this message
        if self.db.stock_market_amount == '':
            message.setIcon(QMessageBox.Information)
            message.setText('something wen\'t wrong!')
            message.setWindowTitle('server error!')
            message.setWindowIcon(QIcon('Icons/Error.png'))
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
            self.local_market_result.setPlainText('we\'re not able to show the results at the moment,'
                                                  ' please try again later!')
        else:
            self.local_market_result.setPlainText('Total Index of Iran Stock Exchange is: ' +
                                                  str(self.db.stock_market_amount) + ' Million.')
            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText('Do you want to save Total Index of Iran Stock Exchange amount'
                            ' result into the DataBase as well?')
            message.setWindowTitle('Inserting TSE status to DB!')
            message.setWindowIcon(QIcon('Icons/StockExchange.png'))
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            return_value = message.exec_()
            if return_value == QMessageBox.Yes:
                self.db.stock_market_run_count()
                self.db.stock_market_run_count_reader()
                self.db.stock_market_mongo_db()
            else:
                return return_value

    # Defining the method bellow will show a message to ask user if they want to quit or not, everytime they press
    # close button or when they click the quit button and everything else related to that such as 'Ctrl+Q' shortcut key.
    def closeEvent(self, event):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText('Are you sure you want to quit?')
        message.setWindowTitle('Quit')
        message.setWindowIcon(QIcon('Icons/Quit.png'))
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return_value = message.exec_()
        if return_value == QMessageBox.Yes:
            # If user decides to click on 'Yes' button, close event will be accepted, and application will be closed.
            event.accept()
        else:
            event.ignore()
            # Otherwise if they chose 'No' option, application will continue running.


if __name__ == '__main__':
    # Creating 'QApplication()' object called app and passing system arguments to it.
    app = QApplication(sys.argv)
    # Creating an object from 'App()' class.
    market_app = App()
    # Show window.
    market_app.show()
    # Including some stylesheets to application.
    with open('style.css', 'r') as style:
        app.setStyleSheet(style.read())
    # Exit the app by using 'sys.exit()' and passing 'QApplication()' exec_() method to it.
    sys.exit(app.exec_())
