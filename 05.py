import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

key = os.environ.get('api_key')

def recommendation(title):
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
        url2 = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key={key}'
        param_2 = {
            'language' : 'ko-KR',
            'region' : 'KR'
        }
        info_2 = requests.get(url2,params=param_2).json()
        movies = info_2['results']
        recommendations = []
        for i in movies:
            if i['title'] not in recommendations:
                recommendations.append(i['title'])
        
        return recommendations
    except:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
