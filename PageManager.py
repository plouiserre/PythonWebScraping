class PageManager : 
    def __init__(self, url, requestsHelper) :
        self.Url = url
        #TODO voir si on supprime ici
        self.ContentPage = None
        self.helper = requestsHelper


    def DownloadHtml(self) :
        r = self.helper.Get(self.Url)
        self.ContentPage = r.text