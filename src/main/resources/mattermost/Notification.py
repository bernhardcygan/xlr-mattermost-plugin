#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json
from xlrelease.HttpRequest import HttpRequest

STATUS_OK = 200

httpRequest = HttpRequest( server, username=None, password=None)

# Initialize variables & check parameters
response = ''
url = server['url']
if not url.strip():
    print 'Error!'
    print 'Server configuration url undefined\n'
    sys.exit(100)
hook = server['hook']
if not hook.strip():
    print 'Error!'
    print 'Hook configuration path undefined\n'
    sys.exit(100)
if not message.strip():
    print 'Error!'
    print 'Parameter message undefined\n'
    sys.exit(200)

# Call Mattermost Incoming WebHook
optionHeader = {"Content-Type" : "application/json"}
data = "text=%s" % message
path = "/hooks/%s" % (hook)

print "\nsending text to server at: %s/%s" % ( url, path )  

response = httpRequest.post(path, data, headers=optionHeader)
reqStatus = response.getStatus()
data = response.getResponse()

print "\nresponse data:\n" + data 
 
if reqStatus != STATUS_OK:
    raise ValueError('Error sending notification', reqStatus, data)

print 'Message sent successfully\n'
sys.exit(0)
