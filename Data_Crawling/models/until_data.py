host = '127.0.0.1'
user_name = "root"
password = "root"
database = "tiki"
port = '3306'
link_api='https://tiki.vn/api/v2/products'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/?src=header_tiki',
    'x-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}
params = {
    'limit': '50',
    'include': 'sale-attrs,badges,product_links,brand,category,stock_item,advertisement',
    'aggregations': '2',
    'trackity_id': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
    'category': '1846',
    'page': '50',
    'src': 'c1846',
    'urlKey':  'laptop-may-vi-tinh-linh-kien',
}