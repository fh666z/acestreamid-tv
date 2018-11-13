'''
Created on 9 Nov 2018

@author: MStanchev
'''

from Player import SiteGrabber


if __name__ == '__main__':

    print "Main Program"
    
    SG = SiteGrabber.Grabber()
    
    SG.get_channel_list()
    
    