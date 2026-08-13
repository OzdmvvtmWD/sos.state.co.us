Colorado UCC Records — Web Scraping & Database Integration

Purpose:
Automates searching and collecting UCC records from the Colorado Secretary of State website using Playwright.

Main tasks:

1. Launch Firefox using Playwright.
2. Open the Colorado UCC advanced search page.
3. Search for records by debtor/owner name.
4. Collect search results from the results table.
5. Open individual document records and capture their URLs.
6. Extract document, record, debtor, secured party, dates, and record type information.
7. Save collected records to a Django database.
8. Skip records that already exist in the database.

Technologies:

* Python
* Playwright
* Django
* Django ORM
* PostgreSQL / SQLite
* asyncio
* Docker

Setup and Launch:

1. Create a virtual environment:
   python -m venv .venv

2. Activate the virtual environment:
   .venv\Scripts\activate

3. Install the required dependencies:
   pip install -r requirements.txt

4. Start the database using Docker:
   docker compose up -d

5. Configure the database connection in the .env file.

6. Apply Django migrations:
   python manage.py makemigrations
   python manage.py migrate

7. Run the scraper:
   python modules/1_fill_page.py

Requirements:

* A VPN or proxy may be required to access the website.


* A video demonstrating the scraper's operation is available in the results/ directory.
