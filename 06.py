import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

key = os.environ.get('api_key')

def credits(title):
    try:
        url = f'https://api.themoviedb.org/3/search/movie?api_key={key}'
        param = {
            'language' : 'ko-KR',
            'query' : {title},
            'region' : 'KR'
        }
        info = requests.get(url,params=param).json()
        movie = info['results']
        id = movie[0]['id']
        url2 = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key={key}'
        param_2 = {
            'language' : 'ko-KR',
            'region' : 'KR'
        }        
        info_2 = requests.get(url2,params=param_2).json()
        movies = info_2['cast']
        movies_2 = info_2['crew']
        a = {'cast' : [], 'crew' : []}

        for x in movies:
            if int(x['cast_id']) < 10:
                a['cast'].append(x['name'])
        for y in movies_2:
            if y['department'] == 'Directing':
                a['crew'].append(y['name'])
        
        return a
                
            
    except:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
