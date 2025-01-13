Second Hand Car Application

📋 Project Description

This application is designed to manage and analyze car-related data. It provides functionalities to view, edit, and analyze information stored in a SQLite database. With a user-friendly graphical interface implemented in Python, the application allows importing/exporting data, database management, and visual analysis of car data.

⚙️ Features

User-friendly graphical interface built with PyQt5.

Manage car data stored in an SQLite database:

Add, update, and delete records.

Import/export car data in CSV format.

Analyze trends and summaries with graphs and charts.

Advanced data analysis with the included Jupyter Notebook.

Customizable interface appearance via ui_style.py.

🔧 Requirements

Python 3.8 or later

Required Libraries:

PyQt5

pandas

sqlite3

matplotlib

🛠️ Installation and Setup

Extract the program files from the ZIP archive.

Navigate to the extracted folder.

Install Python dependencies:

pip install PyQt5 pandas matplotlib

Ensure the following files are in the same directory:

main.py

cars.sqlite

Additional scripts and resources (e.g., main_ui.ui, ui_style.py).

🚀 How to Use

1. Running the Program

To launch the application, run the following command:

python main.py

The graphical interface will appear.

2. User Interface Overview

Dashboard: View a summary of car-related data.

Data Import/Export:

Import new data from data.csv.

Export database records to CSV format.

Database Management:

Add new car entries.

Update existing records.

Delete records.

Analysis Tools: Visualize trends and summaries with graphs and charts.

3. Importing/Exporting Data

Import Data: Select a CSV file (e.g., data.csv) to upload data.

Export Data: Save database contents to a CSV file for external use.

4. Data Analysis

Graphical Analysis: Generate graphs and charts for car data trends.

Advanced Analysis: Use the Jupyter Notebook (cars.ipynb) for detailed analysis.

⚛️ Folder Structure

main.py: Main script to run the application.

main_ui.ui: Graphical interface file.

cars.py: Contains database-related operations.

ui_style.py: Customizable styles and themes.

data.csv: Sample CSV file for data import/export.

cars.sqlite: SQLite database with preloaded car data.

cars.ipynb: Jupyter Notebook for advanced analysis.

🎨 Customization

Modify the application's appearance using ui_style.py:

Change color schemes.

Adjust button styles.
