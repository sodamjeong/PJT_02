import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get('api_key')

def popular_count():
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={key}&language=ko-KR'

    info = requests.get(url).json()
    data = info['results']
    return len(data)
        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
