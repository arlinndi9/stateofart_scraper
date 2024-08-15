
# Scrapy Project: State of Art Jacket Scraper

This project is a web scraper built using Scrapy and Python to extract data about jackets from the State of Art website. It collects information such as product names, URLs, prices, sizes, and images.

## Project Structure

- `scrapers.py`: Contains the main code for scraping data.
- `items.py`: Defines the data structure for the scraped items.
- `pipelines.py`: Contains logic to process and store the scraped data.
- `settings.py`: Configures Scrapy settings.
- `middlewares.py`: Contains custom middlewares for the project.
- `scrapy.cfg`: Configuration file for Scrapy.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `README.md`: This file.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/arlinndi9/stateofartscraper.git
   cd stateofart-scraper
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the spider**:

   ```bash
   scrapy crawl stateofart_jackets
   ```

   Replace `stateofart_jackets` with the name of your spider if different.

## Configuration

- **Settings**: Adjust settings in `settings.py` to configure user agents, download delays, and other Scrapy settings.
- **Item Pipelines**: Define how scraped data is processed and stored in `pipelines.py`.

## Development

To make changes to the scraper or add new features:

1. **Modify the spider**: Edit the spider code in `scrapers.py`.
2. **Update items**: Change the data model in `items.py`.
3. **Adjust pipelines**: Update data processing logic in `pipelines.py`.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to adapt the README to fit the specific details of your project, including the correct repository URL, specific configuration details, and any additional sections you find necessary.