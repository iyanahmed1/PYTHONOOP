import time
# use the notification function from the plyer module
#run pip install to install it
from plyer import notification

if __name__ =='__main__':
    while True:
        notification.notify(
            title='Ama namna gani my friend',
            message='Tume tenga shilingi billioni mia saba ya hawa kina mama mboga',
            timeout=10
        )
        time.sleep(100)