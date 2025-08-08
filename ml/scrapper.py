# https://github.com/Mahdisadjadi/arxivscraper

import arxivscraper
import pandas as pd

scraper = arxivscraper.Scraper(category='cs', date_from='2024-05-27',date_until='2024-06-07')
output = scraper.scrape()

data = pd.DataFrame(output)

data.to_csv('data/raw.csv', index=False)
