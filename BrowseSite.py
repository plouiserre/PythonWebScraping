from Timer import Timer

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
            timer = Timer()
            self.Log.Log_Debug_Level("Page to analyzed %s" % self.AllLinks[i])
            links = self.PageManager.SearchLinks(self.AllLinks[i])
            for link in links :
                baseUrlWithSlash = self.baseUrl+"/"
                if (link in self.AllLinks) == False  and (link != baseUrlWithSlash) :
                    self.Log.Log_Debug_Level("Lien %s" % link)
                    self.AllLinks.append(link)
            timer.EndTimer()
            duration = timer.GetDurationBrowsing()
            self.LogTime(duration, self.AllLinks[i])
            i += 1
        self.Log.Log_Debug_Level("%d pages analyzed" % len(self.AllLinks))



    
    def LogTime(self, duration, link) : 
        duration =  float("{:.2f}".format(duration))
        log_message = "Page {namePage} put {time} secondes to get analyzed".format(namePage = link, time = str(duration))
        self.Log.Log_Debug_Level(log_message)