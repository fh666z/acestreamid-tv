'''
Created on 13 Nov 2018

@author: MStanchev
'''

#from requests import get
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


class Grabber(object):
    '''
    classdocs
    '''

    def __init__(self, uri="https://acestreamid.com/stat/channels"):
        '''
        Constructor
        '''
        self.__grabberUri = uri
    
    def get_page(self):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(requests.get(self.__grabberUri, stream=True)) as resp:
                if self.check_response(resp):
                    html_content_file = open("content.html", 'w')
                    html_content_file.write(resp.content)
                    html_content_file.close()
                    return resp.content
                else:
                    return None
        except RequestException as e: 
            self.log_error("Error during requests to {0} : {1}".format(self.__grabberUri, str(e)))
            return None
        
            
    def check_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)
    
    def get_channel_list(self):
        web_content = self.get_page()
        html_content = BeautifulSoup(web_content, 'html.parser')
        
        html_content = html_content.select('div#acestreamids_main')
                
        for i, link in enumerate(html_content[0].select('a')):
            print (i, link)
        
        
    def log_error(self, msg):
        print msg
        
    