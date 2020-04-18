import sys
# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSlot

# WARNING - MUST RUN IN VIRTUAL ENVIRONMENT SINCE PYQT5 WILL NOT WORK WITH MACOS 10.12
# $ python3 -m venv myenv
# $ . myenv/bin/activate
# $ pip install PyQt5==5.13.0
# $ python3 pyqt_demo.py

# Create an instance of your application window
def window(): 
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(100, 100, 800, 500)
    window.move(60, 15)
    weatherMsg = QLabel(f'Tomorrow\'s forecast: \n{weather_descr}', parent=window)
    helloMsg = QLabel(f'Latest news: \n{news_feed.entries[1].title}', parent=window)
    widget = QWidget()
    testBtn = QPushButton(window)
    testBtn.setText('Test Button')
    testBtn.clicked.connect(testBtn_clicked)
    weatherMsg.move(60, 15)
    helloMsg.move(60, 45)
    testBtn.move(60, 80)
    window.show()
    sys.exit(app.exec_())

def testBtn_clicked():
   print("button clicked")


if __name__ == '__main__':
    import feedparser

    # get weather
    weather_feed=feedparser.parse('http://www.rssweather.com/zipcode/95687/rss.php')
    weather_entry = weather_feed.entries[0].title
    weather_descr = weather_feed.entries[2].description
    print(weather_entry)
    print('Tomorrow\'s forecast: \n' + weather_descr + "\n")


    # 'monkeypatching' workaround for ssl issue with feedparser in python3
    import ssl
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    # get news
    news_feed = feedparser.parse('http://www.npr.org/rss/rss.php?id=1001')
    for entry in news_feed.entries:
        news_entry = entry.title
        print(news_entry)
    window()
