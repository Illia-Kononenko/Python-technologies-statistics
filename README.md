## Analyzing Technologies Statistics from djinni.co Using Python

This application was made to scrap data about Python jobs
from djinni.co (Ukrainian job agency web resource) and make
statistics analyse of this data.
With it, You can find out what technologies You have to know to receive a dev job


## Installing / Getting started

A quick introduction of the minimal setup you need to get the data and make analyse.

### Python3 must be already installed!

```shell
git clone https://github.com/Illia-Kononenko/Python-technologies-statistics.git
cd Python-technologies-statistics
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
scrapy crawl djinni -O job_listings.csv
```



## Read statistics
To see the statistics just start djinni.ipynb.
Run all cells one by one to see the plots.




## Features:
- scraping data from djinni.co by "Python" search word
- possibility to scrap info by any other search word
- what technologies You have to know to receive a python-dev job
