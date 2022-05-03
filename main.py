from email.mime import base
from BrowseSite import BrowseSite
import logging
from PageManager import PageManager
from RequestsHelper import RequestsHelper
from logger import Logger

log = Logger(logging.DEBUG, '%(levelname)s: %(asctime)s | %(message)s ', 'utf-8', 'webscraping.log')

baseUrl = "https://www.jeuxvideo.com"
helper = RequestsHelper()
pgManager = PageManager(helper, baseUrl)
browseSite = BrowseSite(baseUrl, pgManager, log)
browseSite.Browse()