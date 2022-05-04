import logging

from Timer import Timer
from BrowseSite import BrowseSite
from PageManager import PageManager
from RequestsHelper import RequestsHelper
from logger import Logger

log = Logger(logging.DEBUG, '%(levelname)s: %(asctime)s | %(message)s ', 'utf-8', 'webscraping.log')
time = Timer()
        
#pour comprendre le bug analyser la page https://www.jeuxvideo.com/forums/0-3019601-0-1-0-1-0-tiny-tina-s-wonderlands.htm 
#baseUrl = "https://www.jeuxvideo.com"
#baseUrl = "https://www.excalibur-comics.fr/"
baseUrl = "https://code-garage.fr/"
helper = RequestsHelper()
pgManager = PageManager(helper, baseUrl)
browseSite = BrowseSite(baseUrl, pgManager, log)
browseSite.Browse()

time.EndTimer()
duration = time.GetDurationBrowsing()
log.Log_Debug_Level("Time to scroll all website %.2f secondes" % duration)