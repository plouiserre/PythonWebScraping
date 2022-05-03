import unittest
import mock
from mock import patch
from BrowseSite import PageManager

from BrowseSite import BrowseSite

class BrowseSiteTest(unittest.TestCase) : 
    
    def getHtmlLinks(*args) :
        links = ""
        if(args[0] == "http://www.jeuxvideo.com") :
            links = ["/test/1566617/motogp-2022-le-jeu-video-de-moto-accelere-mais-pas-a-fond.htm","/test/1564807/mlb-the-show-22-le-jeu-video-de-baseball-de-sony-dispo-sur-xbox-toujours-aussi-solide.htm"]
        elif(args[0] == "/test/1566617/motogp-2022-le-jeu-video-de-moto-accelere-mais-pas-a-fond.htm") :
            links =["/cheats.htm", "/previews.htm"]
        elif(args[0] == "/test/1564807/mlb-the-show-22-le-jeu-video-de-baseball-de-sony-dispo-sur-xbox-toujours-aussi-solide.htm") :
            links=["/high-tech/guides/guide-1484272.htm", "/wikis-soluce-astuces/1062487/wiki-de-elden-ring.htm", "/wikis-soluce-astuces/1474855/lost-ark-guides-astuces.htm"]
        
        return links

    @patch.object(PageManager,'SearchLinks',side_effect=getHtmlLinks)
    def test_browse(self, mock_pagemanager) : 
        LogMock = mock.Mock()

        browseSite = BrowseSite("http://www.jeuxvideo.com", PageManager, LogMock)

        browseSite.Browse()                          
                                 
        self.assertEqual(len(browseSite.AllLinks),8)
        self.assertEqual(browseSite.AllLinks[0],"http://www.jeuxvideo.com")
        self.assertEqual(browseSite.AllLinks[1],"/test/1566617/motogp-2022-le-jeu-video-de-moto-accelere-mais-pas-a-fond.htm")
        self.assertEqual(browseSite.AllLinks[2],"/test/1564807/mlb-the-show-22-le-jeu-video-de-baseball-de-sony-dispo-sur-xbox-toujours-aussi-solide.htm")
        self.assertEqual(browseSite.AllLinks[3],"/cheats.htm")
        self.assertEqual(browseSite.AllLinks[4],"/previews.htm")
        self.assertEqual(browseSite.AllLinks[5],"/high-tech/guides/guide-1484272.htm")
        self.assertEqual(browseSite.AllLinks[6],"/wikis-soluce-astuces/1062487/wiki-de-elden-ring.htm")
        self.assertEqual(browseSite.AllLinks[7],"/wikis-soluce-astuces/1474855/lost-ark-guides-astuces.htm")

    if __name__ == "__main__":
        unittest.main()
