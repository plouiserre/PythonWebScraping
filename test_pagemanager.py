import unittest
import mock
from RequestsHelper import RequestsHelper
from PageManager import PageManager

class PageManagerTest(unittest.TestCase):
    
    def test_html_page(self) : 
        html = "<html><h1>Big title of the page</h1></html>"
        mockHtml =  type('',(object,),{"text":html })() 
        url = "http://www.jeuxvideo.com"
        helper = RequestsHelper()
        helper.Get = mock.MagicMock(return_value = mockHtml)
        pageManager = PageManager(url, helper)
        
        pageManager.DownloadHtml()

        self.assertEqual(pageManager.Url, url)
        self.assertEqual(pageManager.ContentPage, html)

    if __name__ == "__main__":
        unittest.main()