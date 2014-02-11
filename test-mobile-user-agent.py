#!/usr/bin/env python

from user_agents import parse
import httplib
httplib.HTTPConnection.debuglevel = 1                             
import urllib2

#servers = ['http://www.gifts.com/']
servers = ['http://www.gifts.com/']

#add user-agents from Device Atlas - https://deviceatlas.com/device-data/devices/
samsung_note2_ua = 'Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; SCH-R950 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
samsung_note1_ua = 'Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; GT-I9220 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
samsung_galaxyS3_ua = 'Mozilla/5.0 (Linux; U; Android 4.1.1; sv-se; GT-I9305N Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
google_nexus10_ua = 'Mozilla/5.0 (Linux; U; Android 4.2; en-us; Nexus 10 Build/JOP31) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'
google_nexus7_ua = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
apple_iPad1_ua = 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
apple_iPhone5_ua = 'Instagram 3.4.1 (iPhone5,1; iPhone OS 6.0.2; en_US; en) AppleWebKit/420+'
firefox_ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0'
google_nexus_v5_ua = 'Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/KRT16C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.102 Mobile Safari/537.36'

#key-value pair dictionary
samsung_note2 = {'user_agent':samsung_note2_ua,'mobile':'True'}
samsung_note1 = {'user_agent':samsung_note1_ua,'mobile':'True'}
samsung_galaxyS3 = {'user_agent':samsung_galaxyS3_ua,'mobile':'True'}
google_nexus10 = {'user_agent':google_nexus10_ua,'mobile':'False'}
google_nexus7 = {'user_agent':google_nexus7_ua,'mobile':'False'}
apple_iPad1 = {'user_agent':apple_iPad1_ua,'mobile':'False'}
apple_iPhone5 = {'user_agent':apple_iPhone5_ua,'mobile':'True'}
firefox = {'user_agent':firefox_ua,'mobile':'False'}
google_nexus_v5 = {'user_agent':google_nexus_v5_ua, 'mobile':'True'}

agents = [samsung_note2,samsung_note1,samsung_galaxyS3,google_nexus10,google_nexus7,apple_iPad1,apple_iPhone5,firefox, google_nexus_v5]


#urllib2 library pushes the user to the final destination
#stop at the point of redirection
#custom Redirect Handler
class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    
    def http_error_302(self,req, fp, code, msg, headers):
        self.headers = headers
        print "Redirection: 302"
        return urllib2.HTTPRedirectHandler.http_error_302(self,req, fp, code, msg, headers)
    
    
    def http_error_301(self,req, fp, code, msg, headers):
        self.headers = headers
        print "Redirection: 301"
        return urllib2.HTTPRedirectHandler.http_error_301(self,req, fp, code, msg, headers)
    
    def http_error_303(self,req, fp, code, msg, headers):
        self.headers = headers
        print "Redirection Carried Out"
        return urllib2.HTTPRedirectHandler.http_error_303(self,req, fp, code, msg, headers)
    
    http_error_307 = http_error_303 

cookieprocessor = urllib2.HTTPCookieProcessor()
redirect_handler = MyHTTPRedirectHandler() #creating an instance of the class object
opener = urllib2.build_opener(redirect_handler, cookieprocessor)
urllib2.install_opener(opener)

for server in servers:
    for agent in agents:
        request = urllib2.Request(server)
        request.add_header('User-agent',agent['user_agent'])
        response = urllib2.urlopen(request)
           
        if agent['mobile'] == 'True':
            headers = redirect_handler.headers
            #if headers: - do we need this? if Firefox = Mobile True then it doesn't enter this and throw an error
            #print agent['user_agent']
            #assert headers['Location'] == 'http://m.gifts.com/'
            print headers['Location']
            print 'mobile device', agent['user_agent'] ,'is redirected correctly '
            assert response.getcode() == 200
            print '200 OK'
            redirect_handler.headers = None
            
        else:
            headers = redirect_handler.headers
            assert headers == None
        
        #library to determine type of device
        #useragent_check = parse(agent['user_agent'])
        #print 'mobile?',useragent_check.is_mobile 
        #print 'tablet?',useragent_check.is_tablet 
        #print 'pc?',useragent_check.is_pc
        #print '\n'
        

    

#create an object, store the info and assert against
# create a dictionary with the user agent and the key which has mobile True/False
# do your request and check if a redirect happened or not





