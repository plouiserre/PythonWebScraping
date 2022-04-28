import re 

class PageManager : 
    def __init__(self, url, requestsHelper) :
        self.Url = url
        #TODO voir si on supprime ici
        self.ContentPage = None
        self.Links = []
        self.helper = requestsHelper


    def SearchLinks(self) :
        r = self.helper.Get(self.Url)
        self.ContentPage = r.text
        links = re.findall("href=\"(.*?)\"", self.ContentPage)
        limit = len(links)
        i = 0 
        while i < limit :
            isValid = self.ValidLink(links[i])
            if isValid : 
                self.Links.append(links[i])
            i += 1


    def ValidLink(self, link) :
        isValidLink = True
        forbidden_extension = [".png", ".json", ".css", ".js"]
        for ext in forbidden_extension : 
            if ext in link :
                isValidLink = False
                break
        if isValidLink and "https://" in link :
            if ("www.jeuxvideo.com" in link) == False :
                isValidLink = False
        return isValidLink