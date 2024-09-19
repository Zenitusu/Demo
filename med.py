from bs4 import BeautifulSoup

with open('debi.html') as fp:
    soup = BeautifulSoup(fp,'lxml')

container = soup.find('iframe',class_='youtube_link')
print(container)
# content in the iframe
Split_Iframe = container['src'].split('/')
print(Split_Iframe)
Iframe = container['src'].split('/')[3]
vid_id = Iframe.split('?')[0]
print(f'The Iframe of the splitted is {Iframe}')
print(f'The source code of the video: {vid_id}')
yt_link = f'https://www.youtube.com/watch?v={vid_id}'
print('\n\n\n')
print(yt_link)