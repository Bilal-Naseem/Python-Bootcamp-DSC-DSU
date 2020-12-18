import requests
import csv
from bs4 import BeautifulSoup

def getLikes(Complete_Url):
    response = requests.get(Complete_Url)
    soup = BeautifulSoup(response.content,'html.parser')
    try:
        LikeCount = soup.select_one("#PagesLikesCountDOMID span").text[1:-9]
    except AttributeError:
        print('Page Request Not Successfull')
        exit()
    return int(LikeCount.replace(',',''))

    
def main():
    Url_List = ["LaLiga","RealMadrid","ChampionsLeague"]
    Base_Url = "https://www.facebook.com/"
    with open('LikesCount.csv',"a") as CountFile:
        filePointer = csv.DictWriter(CountFile,fieldnames=['url','Like_Count'])
        filePointer.writeheader()
        for url in Url_List:
            likes = ""
            likes = getLikes(Base_Url+url)
            data = {'url' : url, 'Like_Count' : likes}
            filePointer.writerow(data)

if __name__ == "__main__":
    main()



#            print(len(likes))
#            for each in likes:
#                print(each)

 #           likes_2 = likes.strip()
 #           print(len(likes.strip()))
  #          for each in likes_2:
   #             print(each)

    #        print(likes.replace(' ','-'))
