#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from mattermost.MattermostClient import MattermostClient


try:
   mattermostClient = MattermostClient.create_mattermostClient( mattermostServer )
   data = mattermostClient.checkConnection()
   print data
except :
   traceback.print_exc(file=sys.stdout)
   sys.exit(1)

