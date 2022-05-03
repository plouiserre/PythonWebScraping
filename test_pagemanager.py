import unittest
import mock
from RequestsHelper import RequestsHelper
from PageManager import PageManager

class PageManagerTest(unittest.TestCase):
    
    def test_html_page(self) : 
        html = "<html><h1>Big title of the page</h1></html>"
        url = "http://www.jeuxvideo.com"
        pageManager = self.init_pageManager_unittest(html, url)
        
        pageManager.SearchLinks(url)

        self.assertEqual(pageManager.Url, url)
        self.assertEqual(pageManager.ContentPage, html)


    def test_get_links (self) :
        html = "<a class=\"stretched-link card__link\" href=\"/test/1566617/motogp-2022-le-jeu-video-de-moto-accelere-mais-pas-a-fond.htm\">MotoGP 2022 : le jeu vidéo de moto accélère, mais pas à fond !</a>                     <a class=\"stretched-link card__link\" href=\"/test/1564807/mlb-the-show-22-le-jeu-video-de-baseball-de-sony-dispo-sur-xbox-toujours-aussi-solide.htm\">MLB The Show 22 : Le jeu vidéo de Baseball de Sony dispo sur Xbox toujours aussi solide</a></h3>"
        url = "https://www.jeuxvideo.com"
        pageManager = self.init_pageManager_unittest(html, url)
        
        pageManager.SearchLinks(url)

        firstLinks = "https://www.jeuxvideo.com/test/1566617/motogp-2022-le-jeu-video-de-moto-accelere-mais-pas-a-fond.htm"
        secondLinks = "https://www.jeuxvideo.com/test/1564807/mlb-the-show-22-le-jeu-video-de-baseball-de-sony-dispo-sur-xbox-toujours-aussi-solide.htm"
        self.assertEqual(len(pageManager.Links), 2)
        self.assertEqual(pageManager.Links[0], firstLinks)
        self.assertEqual(pageManager.Links[1], secondLinks)


    def test_validLinks (self) :
        html = "<a class=\"stretched-link card__link\" href=\"/test/1566617/motogp-2022-le-jeu-video-de-moto-accelere-mais-pas-a-fond.htm\">MotoGP 2022 : le jeu vidéo de moto accélère, mais pas à fond !</a> <a class=\"stretched-link card__link\" href=\"https://sdk.privacy-center.org/\">Link1</a><a class=\"stretched-link card__link\" href=\"/favicon.png\">Link2</a><a class=\"stretched-link card__link\" href=\"/manifest.json\">Link3</a><a class=\"stretched-link card__link\" href=\"https://static.jvc.gg/22.6.1/css/skin-common.css\">Link4</a><a class=\"stretched-link card__link\" href=\"https://static.jvc.gg/22.6.1/js/hp.js\">Link5</a></h3>"
        url = "https://www.jeuxvideo.com"
        pageManager = self.init_pageManager_unittest(html, url)
        
        pageManager.SearchLinks(url)

        firstLinks = "https://www.jeuxvideo.com/test/1566617/motogp-2022-le-jeu-video-de-moto-accelere-mais-pas-a-fond.htm"
        self.assertEqual(len(pageManager.Links), 1)
        self.assertEqual(pageManager.Links[0], firstLinks)
        

    def init_pageManager_unittest(self, html, baseUrl) :
        mockHtml =  type('',(object,),{"text":html })() 
        helper = RequestsHelper()
        helper.Get = mock.MagicMock(return_value = mockHtml)
        pageManager = PageManager(helper, baseUrl)
        return pageManager
        

    if __name__ == "__main__":
        unittest.main()