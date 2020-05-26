from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import re
print("Name the movie")
movie = input()
new_movie=""
for i in movie:
    if i.isspace():
        new_movie=new_movie+'+'
    else:
        new_movie=new_movie+i
#print(new_movie)
meurl="https://www.imdb.com/find?q="+new_movie+"&ref_=nv_sr_sm"
print(meurl)
uclient=ureq(meurl)
page=uclient.read()  # Download the page
uclient.close()
pagesoup=soup(page,"html.parser")
main=pagesoup.find("div",{"id":"main"})
#print(main)
#print("type of main is")
#print(type(main))
links=main.findAll("a", href=re.compile("(/title/)+"))
#print("\nlength of link is ")
#print(len(links))

mainlink=links[0]
mainlink=mainlink['href']
#print(mainlink)

print("\nNow the final link is ")
new_url = "https://imdb.com"+mainlink
print(new_url)
try:
    new_uclient = ureq(new_url)
    new_page = new_uclient.read()
    new_uclient.close()
    new_pagesoup = soup(new_page,"html.parser")
    rating = new_pagesoup.find("div",{"class":"ratingValue"})
    print("\nRating of this movie on IMDB is " + rating.get_text())

    try:
        trailer = new_pagesoup.find("div",{"class":"slate"})
        #print(trailer)
        newlink=trailer.findAll("a", href=re.compile("(/video/)+"))
        newlink = newlink[0]
        newlink=newlink['href']
        #print("newlink")
        print("\nWant to see Trailer of this movie, Here it is ")
        print("https://www.imdb.com"+newlink)
    except:
        print("\nSorry, Trailer not available")


    title = new_pagesoup.find("div",{"class":"title_wrapper"})
    #print(title)

    newlink=title.get_text()

    newtext = newlink.partition('\n')[2]

    print("\nFull name of the movie is " + newtext.partition('   ')[0])
    #print(newtext.partition('   ')[1])
    #print(newtext.partition('   ')[2])

    print("How long the movie is ")
    time_movie = title.find("time")
    time_movie=time_movie.get_text()
    time_movie.replace(" ","")
    print(str(time_movie[25])+"hours and "+ str(time_movie[28])+str(time_movie[29]) + "min")
    
except:
    print(" We could not find movie, Please check above link")
print("end")




