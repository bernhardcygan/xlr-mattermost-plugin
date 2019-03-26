#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json
from xlrelease.HttpRequest import HttpRequest

STATUS_OK = 200


# Initialize variables & check parameters
response = ''
url = server['url']
if not url.strip():
    print 'Error!'
    print 'Server configuration url undefined\n'
    sys.exit(100)
if not message.strip():
    print 'Error!'
    print 'Parameter message undefined\n'
    sys.exit(200)

# Call Mattermost Incoming WebHook
optionHeader = {"Content-Type" : "application/json"}
data = "text=%s" % message
response = self.httpRequest.post( url, data, headers=optionHeader)
reqStatus = response.getStatus()
data = response.getResponse()
if reqStatus != STATUS_OK:
    raise ValueError('Error sending notification', reqStatus, data)

print 'Message sent successfully\n'
sys.exit(0)
