import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

key = os.environ.get('api_key')

def search_movie(title):    
    try:
        url = f'https://api.themoviedb.org/3/search/movie?api_key={key}'
        param = {
            'language' : 'ko-KR',
            'query' : {title},
            'region' : 'KR'
        }
        info = requests.get(url,params=param).json()
        movie = info['results']
        first = movie[0]['id']
        return first
    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
