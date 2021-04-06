import urllib.request
import urllib.parse
url = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=";
#start  limit
#start=1 limit=20

#page =int(input('亲输入想要的数据:'));
number = 20;
#构建get参数
data={
	'start': (3-1)*number,
	'limit': number,
}
#字典转化为get参数
query_string =  urllib.parse.urlencode(data);
url+=query_string;
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers);
response = urllib.request.urlopen(request);
print(response.read().decode())
