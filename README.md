# Latest Indonesia Earthquake Information
This is will get the latest information of earthquake in Indonesia ([BMKG Indonesia](https://www.bmkg.go.id/))

## How It Work?
This package will scrape data from 	[BMKG Indonesia](https://www.bmkg.go.id/) and [BMKG Indonesia Pages](https://www.bmkg.go.id/gempabumi-dirasakan.html) to get latest information of earhquake in Indonesia 

This Package use BeautifulSoup4 and Request to produce output in the form of JSON that is ready to be used in web ora mobile applications

## How to Use


Install package Requests & Beautifulsoap4
```
pip install Requests
pip install beautifulsoup4
```

to use earthquake_data in main.py
```
import earthquake_data

if __name__ == "__main__":
    earthquake_data.get_data_earthquake()
```
to use earthquake_recent in main.py
```
import earthquake_recent

if __name__ == "__main__":
    data = earthquake_recent.extraction_data()
    earthquake_recent.show_data(data)
```

# Author
Muhammad Iqbal ([Miqbal20](https://github.com/miqbal20))