import re 

#TODO delete self.Links because it is only in SearchLinks methods
class PageManager : 
    def __init__(self, requestsHelper, baseUrl) :
        self.ContentPage = None
        self.Links = []
        self.helper = requestsHelper
        self.BaseUrl = baseUrl
        self.Url = None


    def SearchLinks(self, urlToCrawl) :
        self.Url = urlToCrawl
        r = self.helper.Get(self.Url)
        self.ContentPage = r.text
        links = re.findall("href=\"(.*?)\"", self.ContentPage)
        limit = len(links)
        i = 0 
        while i < limit :
            isValid, links[i] = self.ValidLink(links[i])
            if isValid : 
                self.Links.append(links[i])
            i += 1
        return self.Links

    #soucis de référence pour code 35 36
    def ValidLink(self, link) :
        isValidLink = True
        forbidden_extension = [".png", ".json", ".css", ".js"]
        for ext in forbidden_extension : 
            if ext in link :
                isValidLink = False
                break
        if isValidLink and "https://" in link :
            if (self.Url in link) == False :
                isValidLink = False
        if isValidLink and (self.BaseUrl in link) == False : 
                link = self.BaseUrl + link
        return isValidLink, link