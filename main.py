from PageManager import PageManager
from RequestsHelper import RequestsHelper

helper = RequestsHelper()
pageManager = PageManager("http://www.jeuxvideo.com", helper)
pageManager.SearchLinks()
print("Beginning of html downloaded")
print(pageManager.ContentPage)
print("End of html downloaded")