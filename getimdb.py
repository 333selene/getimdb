from bs4 import BeautifulSoup
import argparse
import requests

def get_rank_type_str(rank_type):
    sort_options = ['&sort=rank%2Casc', 'sort=user_rating%2Cdesc']
    rank_str = sort_options[rank_type]
    return rank_str
   
def get_url(base_url, rank_str):
    url = base_url + rank_str
    return(url)

def get_titles(url, n):
    session = requests.Session()
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all("div", class_='ipc-metadata-list-summary-item__c')[:n]
    for div in divs:
        title = div.find('h3').text
        print(title)

def argparser(parser):
    parser.add_argument("-rank",default=0, help='0 for rank by user rating, 1 for rank by IMDB rating. Default = 0.')
    parser.add_argument('-n', default=10, help='Number of titles to scrape')
    args = parser.parse_args()
    return args
   
def main():
    base_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    parser = argparse.ArgumentParser(description="Gets top n films on IMDB")
    args = argparser(parser)
    rank_type = int(args.rank)
    rank_str = get_rank_type_str(rank_type)
    url = get_url(base_url, rank_str)
    n = int(args.n)
    get_titles(url,n )    
   
if __name__ == "__main__":
    main()