from pathlib import Path
import requests
import csv
import sys
import io
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import tkinter

#Accesare, verificare, descarcare si creare fisier.csv
fisier_csv = 'fisier.csv'
path = Path(fisier_csv)

if path.is_file():
    print(f'Fisierul {fisier_csv} exista')
else:
    print(f'Fisierul {fisier_csv} nu exista, se descarca...')
    URL = 'https://data.primariatm.ro/datastore/dump/d680ddb5-45be-4842-95b6-afdef322991a?bom=True'
    r = requests.get(URL, allow_redirects=True)
    open('fisier.csv', 'wb').write(r.content)

    with open('fisier.csv', 'r') as file:
        reader = csv

#Interfata grafica
root = tkinter.Tk()
root.title('PROIECT LP2')
root.geometry('800x650')

frame_title = tkinter.Frame(root)
frame_site = tkinter.Frame(root)
frame_change = tkinter.Frame(root)


class Temperatura(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - TEMPERATURA')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.756601, 21.228378], zoom_start=12.49999)
        folium.Marker(location=[45.73293, 21.2191], popup='02-Bd. L. Rebreanu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.74303, 21.2429], popup='03-St. Surorile Martir Caceu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.7626, 21.24761], popup='04-Bd. Take Ionescu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.77008, 21.22317], popup='05-C.Aradului_Miresei', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.77472, 21.22146], popup='06-C.Aradului_Liege', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.76003, 21.21837], popup='07-St. Gh.Lazar', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.76302, 21.21068], popup='08-Bd.Cetatii', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.75174, 21.21601], popup='09-Pasajul Jiul', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.73908, 21.20977], popup='10-St. Budai Deleanu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.76952, 21.23034], popup='12-St. Divizia 9 Cavalerie', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.73305, 21.25929], popup='13-Calea Buziasului-AEM', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.75685, 21.25545], popup='14-St. Ion Mihalache', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.75002, 21.20511], popup='15-St. Garii', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.7701, 21.24926], popup='16- St.Aristide Demetriade', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.802535, 21.221965], popup='20-Dumbravita Vest', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.702602, 21.207354], popup='21-Chisoda', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.726303, 21.295644], popup='22-Mosnita Noua', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.758015, 21.223886], popup='23-HUB 700', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.772581, 21.281521], popup='24-Calea Lugojului', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.808657, 21.280012], popup='25-Dumbravita Est', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.760627, 21.250988], popup='Strada Timocului', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.728525, 21.3121389999999], popup='Mosnita Noua', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.74836, 21.267372], popup='ASOCIATIA CRIES', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.7946160555555, 21.2476561388888], popup='Senzor mobil instalat pe autobuz', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.7130500299999, 21.19271429], popup='Calea Sagului & Strada Ovidiu Cortus', icon=folium.Icon(color='green')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class Presiunea(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - PRESIUNEA')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.756601, 21.228378], zoom_start=12.49999)
        folium.Marker(location=[45.76062700000007, 21.250988000000003], popup='Strada Timocului', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.760434650000015, 21.215262025], popup='Strada Liege & Calea Torontului', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.765177040000005, 21.202405090000003], popup='Strada Cloșca Strada Herța', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.77269334, 21.2165856], popup='Strada Liege & Calea Torontalului', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.75802495, 21.23284987], popup='Piața Ionel I. C. Brătianu', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.7532, 21.232271190000002], popup='Strada Michelangelo & Bulevardul Ion C. Brătianu', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.74781517000002, 21.225506240000005], popup='Bulevardul Vasile Pârvan & Bulevardul Mihai Viteazu', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.74048983, 21.222777360000002], popup='Strada Alexandru Odobescu & Strada Ciprian Porumbescu', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.75829999999998, 21.293959999999977], popup='Ghiroda, Strada Sf.Andrei', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.728525, 21.31213899999998], popup='Mosnita Noua, Strada Bolero', icon=folium.Icon(color='orange')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class Umiditatea(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - UMIDITATEA')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)


        m = folium.Map(location=[45.756601, 21.202405090000003], zoom_start=12.49999)
        folium.Marker(location=[45.765177040000005, 21.20545], popup='Strada Closca Strada Herta', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.79047230000001, 21.22835129999999], popup='Dumbravita, Strada Parcului', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.755948, 21.245462], popup='29-CET Centru', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.77512131000001, 21.3009718799999], popup='Calea Lugojului & Strada Victoria', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.713050029999984, 21.19271429], popup='Calea Șagului & Strada Ovidiu Cotruș', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.73771499999999, 21.244698], popup='Bulevardul Liviu Rebreanu & Aleea Sănătăţii', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.7532, 21.232271190000002], popup='Strada Michelangelo & Bulevardul Ion C. Brătianu', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.74803599999997, 21.268859999999993], popup='ASOCIAȚIA CRIES', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.758089516666665, 21.140438350000004], popup='Senzor mobil instalat pe autobuz', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.75829999999998, 21.293959999999977], popup='Ghiroda', icon=folium.Icon(color='lightgreen')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class Comp_vol(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - COMPUSI VOLATILI')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.786601, 21.238378], zoom_start=12.49999)
        folium.Marker(location=[45.77269334, 21.2165856], popup='Strada Liege & Calea Torontalului', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.765177040000005, 21.202405090000003], popup='Strada Cloșca Strada Herța', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.76643873, 21.242551319999997], popup='Strada Divizia 9 Cavalerie & Strada Aristide Demetriade', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.75324373, 21.2222366], popup='Bulevardul Republicii & Spitalul de Copii', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.74781517000002, 21.225506240000005], popup='Bulevardul Vasile Pârvan & Bulevardul Mihai Viteazu', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.74048983, 21.222777360000002], popup='Strada Alexandru Odobescu & Strada Ciprian Porumbescu', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.74542868999999, 21.25433565], popup='Calea Stan Vidrighin & Strada Batania', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.73771499999999, 21.244698], popup='Bulevardul Liviu Rebreanu & Aleea Sănătăţii', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.72812850999998, 21.205470030000004], popup='Calea Șagului & Strada Ana Ipătescu', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.713050029999984, 21.19271429], popup='Calea Șagului & Strada Ovidiu Cotruș', icon=folium.Icon(color='orange')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class Formal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - FORMALDEHIDA')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.786601, 21.238378], zoom_start=12.49999)
        folium.Marker(location=[45.75324373, 21.2222366], popup='Bulevardul Republicii & Spitalul de Copii', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.7532, 21.232271190000002], popup='Strada Michelangelo & Bulevardul Ion C. Brătianu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.75802495, 21.23284987], popup='Piața Ionel I. C. Brătianu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.74781517000002, 21.225506240000005], popup='Bulevardul Vasile Pârvan & Bulevardul Mihai Viteazu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.74048983, 21.222777360000002], popup='Strada Alexandru Odobescu & Strada Ciprian Porumbescu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.73771499999999, 21.244698], popup='Bulevardul Liviu Rebreanu & Aleea Sănătăţii', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.72812850999998, 21.205470030000004], popup='Calea Șagului & Strada Ana Ipătescu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.73771499999999, 21.244698], popup='Bulevardul Liviu Rebreanu & Aleea Sănătăţii', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.713050029999984, 21.19271429], popup='Calea Șagului & Strada Ovidiu Cotruș', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.77512131000001, 21.300971879999995], popup='Calea Lugojului & Strada Victoria', icon=folium.Icon(color='green')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class CO2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - DIOXID DE CARBON')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.786601, 21.238378], zoom_start=12.49999)
        folium.Marker(location=[45.765177040000005, 21.202405090000003], popup='Strada Cloșca Strada Herța', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.77269334, 21.2165856], popup='Strada Liege & Calea Torontalului', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.76643873, 21.242551319999997], popup='Strada Divizia 9 Cavalerie & Strada Aristide Demetriade', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.77512131000001, 21.300971879999995], popup='Calea Lugojului & Strada Victoria', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.75802495, 21.23284987], popup='Piața Ionel I. C. Brătianu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.75324373, 21.2222366], popup='Bulevardul Republicii & Spitalul de Copii', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.7532, 21.232271190000002], popup='Strada Michelangelo & Bulevardul Ion C. Brătianu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.74781517000002, 21.225506240000005], popup='Bulevardul Vasile Pârvan & Bulevardul Mihai Viteazu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.765177040000005, 21.202405090000003], popup='Strada Cloșca Strada Herța', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.74818005882353, 21.253157352941177], popup='Senzor mobil instalat pe autobuz', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.74048983, 21.222777360000002], popup='Strada Alexandru Odobescu & Strada Ciprian Porumbescu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.72812850999998, 21.205470030000004], popup='Calea Șagului & Strada Ana Ipătescu', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[45.713050029999984, 21.19271429], popup='Calea Șagului & Strada Ovidiu Cotruș', icon=folium.Icon(color='green')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class PM1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - PM1.0')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.786601, 21.238378], zoom_start=12.49999)
        folium.Marker(location=[45.77269334, 21.2165856], popup='Strada Liege & Calea Torontalului', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.765177040000005, 21.202405090000003], popup='Strada Cloșca Strada Herța', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.75802495, 21.23284987], popup='Piața Ionel I. C. Brătianu', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.75324373, 21.2222366], popup='Bulevardul Republicii & Spitalul de Copii', icon=folium.Icon(color='lightred')).add_to(m)
        folium.Marker(location=[45.7532, 21.232271190000002], popup='Strada Michelangelo & Bulevardul Ion C. Brătianu', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.74781517000002, 21.225506240000005], popup='Bulevardul Vasile Pârvan & Bulevardul Mihai Viteazu', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.74803599999997, 21.268859999999993], popup='ASOCIAȚIA CRIES', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.74048983, 21.222777360000002], popup='Strada Alexandru Odobescu & Strada Ciprian Porumbescu', icon=folium.Icon(color='lightred')).add_to(m)
        folium.Marker(location=[45.713050029999984, 21.19271429], popup='Calea Șagului & Strada Ovidiu Cotruș', icon=folium.Icon(color='pink')).add_to(m)
        folium.Marker(location=[45.72812850999998, 21.205470030000004], popup='CCalea Șagului & Strada Ana Ipătescu', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.73771499999999, 21.244698], popup='Bulevardul Liviu Rebreanu & Aleea Sănătăţii', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.74791899999995, 21.26514999999997], popup='ASOCIAȚIA CRIES', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.728525, 21.31213899999998], popup='Mosnita Noua, Strada Bolero', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.75829999999998, 21.293959999999977], popup='Ghiroda, Strada Sf.Andrei', icon=folium.Icon(color='lightgreen')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class PM2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - PM2.5')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.786601, 21.238378], zoom_start=12.49999)
        folium.Marker(location=[45.765177040000005, 21.202405090000003], popup='Strada Cloșca Strada Herța', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.76062700000007, 21.250988000000003], popup='Strada Timocului', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.772581, 21.281521], popup='24-Calea Lugojului', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.79047230000001, 21.22835129999999], popup='Dumbrăvița, Strada Parcului', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.755948, 21.245462], popup='29-CET Centru', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.75238638983051, 21.240014813559327], popup='Senzor mobil instalat pe autobuz', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.73908, 21.20977], popup='Budai Deleanu', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.77464800000001, 21.240483000000008], popup='Senzor mobil instalat pe autobuz', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.77512131000001, 21.300971879999995], popup='Calea Lugojului & Strada Victoria', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.74807699999998, 21.253285], popup='Senzor mobil instalat pe autobuz', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[445.74048983, 21.222777360000002], popup='Strada Alexandru Odobescu & Strada Ciprian Porumbescu', icon=folium.Icon(color='orange')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class PM10(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - PM10')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.786601, 21.238378], zoom_start=12.49999)
        folium.Marker(location=[45.74542868999999, 21.25433565], popup='Calea Stan Vidrighin & Strada Batania', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.73771499999999, 21.244698], popup='Bulevardul Liviu Rebreanu & Aleea Sănătăţii', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.72812850999998, 21.205470030000004], popup='Calea Șagului & Strada Ana Ipătescu', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.702602, 21.207354], popup='21-Chisoda', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.74542868999999, 21.25433565], popup='Calea Stan Vidrighin & Strada Batania', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.765177040000005, 21.202405090000003], popup='Strada Cloșca Strada Herța ', icon=folium.Icon(color='lightred')).add_to(m)
        folium.Marker(location=[45.76062700000006, 21.250988000000003], popup='Strada Timocului', icon=folium.Icon(color='lightred')).add_to(m)
        folium.Marker(location=[45.802535, 21.221965], popup='20-Dumbravita', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.77472, 21.22146], popup='06-C.Aradului_Liege', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.7701, 21.24926], popup='16-St. Aristide Demetriade', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.7532, 21.232271190000002], popup='Strada Michelangelo & Bulevardul Ion C. Brătianu', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.748360000000034, 21.267372000000016], popup='ASOCIAȚIA CRIES', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker(location=[45.74303, 21.2429], popup='03-St. Surorile Martir Caceu', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.74781517000002, 21.225506240000005], popup='Bulevardul Vasile Pârvan & Bulevardul Mihai Viteazu', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.755948, 21.245462], popup='29-CET Centru', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.75324373, 21.2222366], popup='Bulevardul Republicii & Spitalul de Copii', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.75174, 21.21601], popup='09-Pasajul Jiul', icon=folium.Icon(color='orange')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

class AQI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calitatea Aerului in Timisoara - AQI')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[45.786601, 21.238378], zoom_start=12.49999)
        folium.Marker(location=[45.75002, 21.20511], popup='15-St. Garii', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.77472, 21.22146], popup='06-C.Aradului_Liege', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.7701, 21.24926], popup='16-St. Aristide Demetriade', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.76062700000006, 21.250988000000003,], popup='Strada Timocului', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.76003, 21.21837], popup='07-St. Gh.Lazar', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.75174, 21.21601], popup='09-Pasajul Jiul', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.73771499999999, 21.244698], popup='Bulevardul Liviu Rebreanu & Aleea Sănătăţii', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.73293, 21.2191], popup='02-Bd. L. Rebreanu', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.755948, 21.245462], popup='29-CET Centru', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.758015, 21.223886], popup='23-HUB 700', icon=folium.Icon(color='lightgreen')).add_to(m)
        folium.Marker(location=[45.73771499999999, 21.244698], popup='Bulevardul Liviu Rebreanu & Aleea Sănătăţii', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.73305,21.25929], popup='13-Calea Buziasului_AEM', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.7626,21.24761], popup='04-Bd. Take Ionescu', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.77008,21.22317], popup='05-C.Aradului_Miresei', icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(location=[45.76952,21.23034], popup='12-St. Divizia 9 Cavalerie', icon=folium.Icon(color='orange')).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

#Legatura dintre interfata grafica si hartile generate
def perform():
    choice = site.get()
    if choice == 1:
        app1 = QApplication(sys.argv)
        app1.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp1 = Temperatura()
        myApp1.show()
        tkinter.mainloop()
        try:
            sys.exit(app1.exec_())
        except SystemExit:
            print()

    elif choice == 2:
        app2 = QApplication(sys.argv)
        app2.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp2 = Presiunea()
        myApp2.show()
        tkinter.mainloop()
        try:
            sys.exit(app2.exec_())
        except SystemExit:
            print()

    elif choice == 3:
        app3 = QApplication(sys.argv)
        app3.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp3 = Umiditatea()
        myApp3.show()
        tkinter.mainloop()
        try:
            sys.exit(app3.exec_())
        except SystemExit:
            print()


    elif choice == 4:
        app4 = QApplication(sys.argv)
        app4.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp4 = Comp_vol()
        myApp4.show()
        tkinter.mainloop()
        try:
            sys.exit(app4.exec_())
        except SystemExit:
            print()


    elif choice == 6:
        app5 = QApplication(sys.argv)
        app5.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp5 = Formal()
        myApp5.show()
        tkinter.mainloop()
        try:
            sys.exit(app5.exec_())
        except SystemExit:
            print()


    elif choice == 7:
        app6 = QApplication(sys.argv)
        app6.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp6 = CO2()
        myApp6.show()
        tkinter.mainloop()
        try:
            sys.exit(app6.exec_())
        except SystemExit:
            print()


    elif choice == 8:
        app7 = QApplication(sys.argv)
        app7.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp7 = PM1()
        myApp7.show()
        tkinter.mainloop()
        try:
            sys.exit(app7.exec_())
        except SystemExit:
            print()


    elif choice == 9:
        app8 = QApplication(sys.argv)
        app8.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp8 = PM2()
        myApp8.show()
        tkinter.mainloop()
        try:
            sys.exit(app8.exec_())
        except SystemExit:
            print()


    elif choice == 10:
        app9 = QApplication(sys.argv)
        app9.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp9 = PM10()
        myApp9.show()
        tkinter.mainloop()
        try:
            sys.exit(app9.exec_())
        except SystemExit:
            print()

    elif choice == 11:
        app10 = QApplication(sys.argv)
        app10.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp10 = AQI()
        myApp10.show()
        tkinter.mainloop()
        try:
            sys.exit(app10.exec_())
        except SystemExit:
            print()

    elif choice == 12:
        app11 = QApplication(sys.argv)
        app11.setStyleSheet('''QWidget {font-size: 35px; }''')

        myApp11 = AQI()
        myApp11.show()
        tkinter.mainloop()
        try:
            sys.exit(app11.exec_())
        except SystemExit:
            print()


def intefata():
    pass


frame_title.grid(row=0, column=2, padx=(20, 0))
title = tkinter.Label(frame_title, text="CALITATEA AERULUI", font=("helvetica", 24))
title.grid(pady=(30, 10))
frame_site.grid(row=1, column=1)
site = tkinter.IntVar(value=0)
tkinter.Radiobutton(frame_site, text='Temperatura', variable=site, value=1, font=("Helvetica", 16)).grid(column=2, row=0, sticky='W')
tkinter.Radiobutton(frame_site, text='Presiunea', variable=site, value=2, font=("Helvetica", 18)).grid(column=2, row=1, sticky='W')
tkinter.Radiobutton(frame_site, text='Umiditatea', variable=site, value=3, font=("Helvetica", 18)).grid(column=2, row=2, sticky='W')
tkinter.Radiobutton(frame_site, text='Compuși Volatili', variable=site, value=4, font=("Helvetica", 18)).grid(column=2, row=3, sticky='W')
tkinter.Radiobutton(frame_site, text='Formaldehida', variable=site, value=6, font=("Helvetica", 18)).grid(column=2, row=5, sticky='W')
tkinter.Radiobutton(frame_site, text='Dioxid de Carbon', variable=site, value=7, font=("Helvetica", 18)).grid(column=2, row=6, sticky='W')
tkinter.Radiobutton(frame_site, text='PM1.0', variable=site, value=8, font=("Helvetica", 18)).grid(column=2, row=7, sticky='W')
tkinter.Radiobutton(frame_site, text='PM2.5', variable=site, value=9, font=("Helvetica", 18)).grid(column=2, row=8, sticky='W')
tkinter.Radiobutton(frame_site, text='PM10', variable=site, value=10, font=("Helvetica", 18)).grid(column=2, row=9, sticky='W')
tkinter.Radiobutton(frame_site, text='AQI', variable=site, value=11, font=("Helvetica", 18)).grid(column=2, row=10, sticky='W')

frame_change.grid(row=7, column=7, padx=20, pady=8)
change_btn = tkinter.Button(frame_change, text="OK", height=2, width=8, font=("Helvetica", 16), command=perform)
change_btn.grid(column=8, row=8)
root.mainloop()

if __name__ == '_main_':
    app = QApplication(sys.argv)
    app.setStyleSheet('''QWidget {font-size: 35px; }''')

    myApp = Umiditatea()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print()
