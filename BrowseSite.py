from email.mime import base

from PageManager import PageManager


class BrowseSite :
    def __init__ (self, baseUrl, PageManager, log):
        self.AllLinks = []
        self.baseUrl = baseUrl
        self.Log = log
        self.PageManager = PageManager


    def Browse(self) : 
        self.AllLinks.append(self.baseUrl)
        i = 0
        while i < len(self.AllLinks) :
            self.Log.Log_Debug_Level("Page to analyzed %s" % self.AllLinks[i])
            links = self.PageManager.SearchLinks(self.AllLinks[i])
            for link in links :
                baseUrlWithSlash = self.baseUrl+"/"
                if (link in self.AllLinks) == False  and (link != baseUrlWithSlash) :
                    self.Log.Log_Debug_Level("Lien %s" % link)
                    self.AllLinks.append(link)
            i += 1