import re 

class PageManager : 
    def __init__(self, requestsHelper, baseUrl) :
        self.ContentPage = None
        self.helper = requestsHelper
        self.BaseUrl = baseUrl
        self.Url = None
        self.Links = []


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
        

    def ValidLink(self, link) :
        isValidLink = True
        forbidden_extension = [".png", ".json", ".css", ".js",'@','.ico']
        for ext in forbidden_extension : 
            if ext in link :
                isValidLink = False
                break
        if link == '' or link == ' ' :
            isValidLink = False
        if isValidLink and ("https://" in link or "http://" in link) : #TODO add unit test pour http://web2day.co/
            if (self.Url in link) == False :
                isValidLink = False
        if isValidLink and (self.BaseUrl in link) == False : 
                baseUrlLength = len(self.BaseUrl)
                if link[0] == "/" and self.BaseUrl[baseUrlLength - 1] == "/" :
                    baseUrl = self.BaseUrl[: baseUrlLength - 1]
                    link = baseUrl + link
                else :
                    link = self.BaseUrl + link
        return isValidLink, link