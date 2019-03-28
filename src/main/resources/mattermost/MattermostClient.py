#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

# see https://api.mattermost.com/ for documentation
import sys, traceback, time
from xlrelease.HttpRequest import HttpRequest
from httplib import HTTPConnection

STATUS_OK = 200
STATUS_ACCEPTED = 202

class MattermostClient( object ):
   def __init__(self, mattermostCI, username=None, password=None):
      self.httpConnection = mattermostCI
      self.httpRequest = HttpRequest( mattermostCI, username, password)
   # End def
      
   @staticmethod
   def create_mattermostClient( mattermostCI, username=None, password=None ):
      return MattermostClient( mattermostCI, username, password )
   # End def
      
   def sendNotification(self, text ):
      optionHeader = {"Content-Type" : "application/json"}
      data = '{"text": "%s"}' % message
      path = "/hooks/%s" % (httpConnection.server['hook'])
       
      response = httpRequest.post(path, data, contentType="application/json", headers=optionHeader)
      reqStatus = response.getStatus()
      data = response.getResponse()
      
      if reqStatus == STATUS_OK or reqStatus == STATUS_ACCEPTED:
         return data
      raise ValueError('Error sending notification', reqStatus, data)
   # End def
      

# End Class