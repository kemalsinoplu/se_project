import sys
import pandas as pd
import sqlite3
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton,
    QWidget, QLabel, QComboBox, QLineEdit, QHBoxLayout
)
import subprocess

class CarApp(QMainWindow):
    def __init__(self, car_data):
        super().__init__()

        car_data['Price'] = car_data['Price'].str.replace(r"[^\d]", "", regex=True).astype(float)
        self.car_data = car_data
        self.filtered_data = car_data.copy()

        self.setWindowTitle("Second-Hand Cars")
        self.setGeometry(100, 100, 1000, 600)

        self.initUI()

    def initUI(self):

        main_layout = QVBoxLayout()

        # Filtreleme alanları
        filter_layout = QHBoxLayout()

        self.brand_filter = QComboBox()
        self.brand_filter.addItem("All")
        self.brand_filter.addItems(sorted(self.car_data['Brand'].dropna().unique()))
        self.brand_filter.currentIndexChanged.connect(self.apply_filters)
        filter_layout.addWidget(QLabel("Brand:"))
        filter_layout.addWidget(self.brand_filter)

        self.city_search = QLineEdit()
        self.city_search.setPlaceholderText("Enter City Name")
        filter_layout.addWidget(QLabel("City Search:"))
        filter_layout.addWidget(self.city_search)

        self.city_search_button = QPushButton("Search")
        self.city_search_button.clicked.connect(self.apply_filters)
        filter_layout.addWidget(self.city_search_button)

        self.min_price_filter = QLineEdit()
        self.min_price_filter.setPlaceholderText("Min Price")
        self.min_price_filter.textChanged.connect(self.apply_filters)
        filter_layout.addWidget(QLabel("Price Range:"))
        filter_layout.addWidget(self.min_price_filter)

        self.max_price_filter = QLineEdit()
        self.max_price_filter.setPlaceholderText("Max Price")
        self.max_price_filter.textChanged.connect(self.apply_filters)
        filter_layout.addWidget(self.max_price_filter)

        main_layout.addLayout(filter_layout)

        # Tablo
        self.table = QTableWidget()
        self.table.setColumnCount(len(self.car_data.columns))
        self.table.setHorizontalHeaderLabels(self.car_data.columns)
        self.load_table_data(self.car_data)
        main_layout.addWidget(self.table)

        # Sahibinden linkine git
        self.link_button = QPushButton("Go to Sahibinden")
        self.link_button.clicked.connect(self.open_sahibinden_link)
        main_layout.addWidget(self.link_button)

        # Scraping başlatma butonu
        self.scrape_button = QPushButton("Start Scraping")
        self.scrape_button.clicked.connect(self.start_scraping)
        main_layout.addWidget(self.scrape_button)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def load_table_data(self, data):
        self.table.setRowCount(len(data))
        self.table.clearContents()
        for row_idx, row in data.reset_index(drop=True).iterrows():
            for col_idx, value in enumerate(row):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def apply_filters(self):
        filtered_data = self.car_data.copy()

        selected_brand = self.brand_filter.currentText()
        if selected_brand != "All":
            filtered_data = filtered_data[filtered_data['Brand'].str.lower() == selected_brand.lower()]

        city_query = self.city_search.text().strip().lower()
        if city_query:
            filtered_data = filtered_data[filtered_data['City'].str.lower().str.contains(city_query)]

        min_price = self.min_price_filter.text()
        max_price = self.max_price_filter.text()

        try:
            if min_price:
                filtered_data = filtered_data[filtered_data['Price'] >= float(min_price)]
            if max_price:
                filtered_data = filtered_data[filtered_data['Price'] <= float(max_price)]
        except ValueError:
            pass  

        self.filtered_data = filtered_data.reset_index(drop=True)
        self.load_table_data(self.filtered_data)

    def open_sahibinden_link(self):
        url = "https://www.sahibinden.com/otomobil"
        webbrowser.open(url)

    def start_scraping(self):
        # Scraping işlemini başlat
        try:
            subprocess.run(["jupyter", "nbconvert", "--to", "script", "cars.ipynb"])
            subprocess.run(["python", "cars.py"])
            print("Scraping işlemi tamamlandı.")
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    # SQLite veritabanından veri yüklenmesi
    db_path = 'cars.sqlite'  # Aynı klasördeki veritabanı dosyası
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM carsdata"

    car_data = pd.read_sql_query(query, conn)
    conn.close()

    if 'City' not in car_data.columns:
        car_data['City'] = 'Unknown'

    app = QApplication(sys.argv)
    main_window = CarApp(car_data)
    main_window.show()
    sys.exit(app.exec_())

