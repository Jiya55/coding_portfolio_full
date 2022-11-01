from datetime import *
import time
from plyer import *
import plyer
 
'''notification.notify(title (str) – Title of the notification
message (str) – Message of the notification
app_name (str) – Name of the app launching this notification
app_icon (str) – Icon to be displayed along with the message
timeout (int) – time to display the message for, defaults to 10
ticker (str) – text to display on status bar as the notification arrives
toast (bool) – simple Android message instead of full notification)
'''
'''send_time = datetime.strptime('Jul 14 2022 7:27pm',  '%b %d %Y %I:%M%p')
if send_time == datetime.today():
        '''
plyer.notification.notify(title='Hello', message='hello this is a notification', timeout=5)

    