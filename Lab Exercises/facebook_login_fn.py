'''
	This program file must be edited with a new temporary FaceBook access token every hour.
	The function is called to make the facebook connection.
'''

import facebook

# login to FaceBook to gain access to the graph API
def fb_login():
  # get an access token from the Graph Explorer web page
  #   https://developers.facebook.com/tools/explorer
    ACCESS_TOKEN = 'EAAxqQOPdBIQBAH90DXEGKo4A7DVLIZChQezD47ihnQAZB6ttjqIm4ZAFBp65nb72zMODWIS0btfEMby1QpcT4RGkjVJv0mlDY7UiW0AZCuaC03x5jtSbrAcrYQgHzTcUnLOuG7KR6mq61Nchd83ST3hiZC00psPEWJxPexxPKFIYYbtMEKQfUTr03EAZAla6cMZCzJXerXAvJ53C75wSMUU'
    # get the authorization from facebook and return
    fb  = facebook.GraphAPI(ACCESS_TOKEN)
    return fb