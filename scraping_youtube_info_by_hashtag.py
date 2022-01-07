from bs4 import BeautifulSoup as bs
import requests
import json
import pandas as pd
from scraping_youtube_api import youtube, get_video_details, get_video_infos

my_url = "https://www.youtube.com/hashtag/lkbbppilamongan"

r = requests.get(my_url)
page = (r.text)
soup=bs(page,'html.parser')

data = soup.find_all('script')
hasil = data[33].string

hasil2 = hasil.split(' = ')
hasil_text = hasil2[1].replace(";", "")

hasil_obj = json.loads(hasil_text)
# print(hasil_obj)

d1 = []
for d in hasil_obj['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['richGridRenderer']['contents']:
    # print(d.get('richItemRenderer')['content']['videoRenderer']['videoId'])
    # print(d.get('richItemRenderer')['content']['videoRenderer']['title']['runs'][0]['text'])
    # print(d.get('richItemRenderer')['content']['videoRenderer']['viewCountText']['simpleText'])
    video_id = d.get('richItemRenderer')['content']['videoRenderer']['videoId']
    response = get_video_details(youtube, id=video_id)
    result = get_video_infos(response)

    snippet = result["snippet"]
    statistics = result["statistics"]

    judul = snippet["title"]
    jml_view = statistics["viewCount"]
    jml_like = statistics["likeCount"]

    try:
        jml_dislike = statistics["dislikeCount"]
    except:
        jml_dislike = 0

    try:
        jml_comment = statistics["commentCount"]
    except:
        jml_comment = 0


    # judul = d.get('richItemRenderer')['content']['videoRenderer']['title']['runs'][0]['text']
    # jml_view = d.get('richItemRenderer')['content']['videoRenderer']['viewCountText']['simpleText'].split()

    d1.append(
        {
            'Judul': judul,
            # 'View': jml_view[0].replace(".",""),
            'View': jml_view,
            'Comment': jml_comment,
            'Like': jml_like,
            'Dislike': jml_dislike,
            'Total': (int(jml_like)-int(jml_dislike))
        }
    )

marks_data = pd.DataFrame(d1)
file_name = 'MarksData.xlsx'

# saving the excel
marks_data.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')


