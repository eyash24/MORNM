#notification
class Notification:
    '''
    Notification facade.
    '''
    def notify(self, title='', message='', app_name='', app_icon='',
               timeout=10, ticker='', toast=False):
        '''
        Send a notification.
        :param title: Title of the notification
        :param message: Message of the notification
        :param app_name: Name of the app launching this notification
        :param app_icon: Icon to be displayed along with the message
        :param timeout: time to display the message for, defaults to 10
        :param ticker: text to display on status bar as the notification
                       arrives
        :param toast: simple Android message instead of full notification
        :type title: str
        :type message: str
        :type app_name: str
        :type app_icon: str
        :type timeout: int
        :type ticker: str
        :type toast: bool
        .. note::
           When called on Windows, ``app_icon`` has to be a path to
           a file in .ICO format.
        .. versionadded:: 1.0.0
        .. versionchanged:: 1.4.0
           Add 'toast' keyword argument
        '''

        self._notify(
            title=title, message=message,
            app_icon=app_icon, app_name=app_name,
            timeout=timeout, ticker=ticker, toast=toast
        )

'''
Module of MacOS API for plyer.notification.
'''

from plyer.facades import Notification

from pyobjus import (
    autoclass, protocol, objc_str, ObjcBOOL
)
from pyobjus.dylib_manager import (
    load_framework, INCLUDE
)

load_framework(INCLUDE.AppKit)
load_framework(INCLUDE.Foundation)

NSUserNotification = autoclass('NSUserNotification')
NSUserNotificationCenter = autoclass('NSUserNotificationCenter')


class OSXNotification(Notification):
    '''
    Implementation of MacOS notification API.
    '''

    def _notify(self, **kwargs):
        title = kwargs.get('title', '')
        message = kwargs.get('message', '')
        app_name = kwargs.get('app_name', '')
        # app_icon, timeout, ticker are not supported (yet)

        notification = NSUserNotification.alloc().init()
        notification.setTitle_(objc_str(title))
        notification.setSubtitle_(objc_str(app_name))
        notification.setInformativeText_(objc_str(message))

        usrnotifctr = NSUserNotificationCenter.defaultUserNotificationCenter()
        usrnotifctr.setDelegate_(self)
        usrnotifctr.deliverNotification_(notification)

    @protocol('NSUserNotificationCenterDelegate')
    def userNotificationCenter_shouldPresentNotification_(
            self, center, notification):
        return ObjcBOOL(True)


def instance():
    '''
    Instance for facade proxy.
    '''
    return OSXNotification()


'''
Notification
============

The :class:`Notification` provides access to public methods to create
notifications.

Simple Examples
---------------

To send notification::

    >>> from plyer import notification
    >>> title = 'plyer'
    >>> message = 'This is an example.'
    >>> notification.notify(title=title, message=message)

Android toast notification::

    >>> from plyer import notification
    >>> notification.notify(message='hello', toast=True)

Android simple notification::

    >>> from plyer import notification
    >>> notification.notify(message='hello', toast=True)

Notification with custom icon::

    >>> from plyer import notification
    >>> notification.notify(title='title', message='hello', app_icon=<path>)

.. versionadded:: 1.0.0

.. versionadded:: 1.4.0
   Add implementation of primitive Android popup-like notification (toast)

.. versionchanged:: 1.4.0
   Android implementation now supports custom icons for notifications.
'''


class Notification:
    '''
    Notification facade.
    '''

    def notify(self, title='', message='', app_name='', app_icon='',
               timeout=10, ticker='', toast=False):
        '''
        Send a notification.

        :param title: Title of the notification
        :param message: Message of the notification
        :param app_name: Name of the app launching this notification
        :param app_icon: Icon to be displayed along with the message
        :param timeout: time to display the message for, defaults to 10
        :param ticker: text to display on status bar as the notification
                       arrives
        :param toast: simple Android message instead of full notification
        :type title: str
        :type message: str
        :type app_name: str
        :type app_icon: str
        :type timeout: int
        :type ticker: str
        :type toast: bool

        .. note::
           When called on Windows, ``app_icon`` has to be a path to
           a file in .ICO format.

        .. versionadded:: 1.0.0

        .. versionchanged:: 1.4.0
           Add 'toast' keyword argument
        '''

        self._notify(
            title=title, message=message,
            app_icon=app_icon, app_name=app_name,
            timeout=timeout, ticker=ticker, toast=toast
        )

    # private

    def _notify(self, **kwargs):
        raise NotImplementedError("No usable implementation found!")
'''
Battery
=======
The :class:`Battery` provides information about the battery of your device.
.. note::
        On Android the `BATTERY_STATS` permission is needed.
Simple Example
---------------
To get battery status::
    >>> from plyer import battery
    >>> battery.status
    {'percentage': 82.0, 'isCharging': False}
Supported Platforms
-------------------
Android, iOS, Windows, OS X, Linux
'''


class Battery:
    '''
    Battery info facade.
    '''

    @property
    def status(self):
        '''
        Property that contains a dict with the following fields:
             * **isCharging** *(bool)*: Battery is charging
             * **percentage** *(float)*: Battery charge remaining
            .. warning::
                If any of the fields is not readable, it is set as
                None.
        '''
        return self.get_state()

    def get_state(self):
        '''
        Public method for filling battery.status via platform-specific
        API in plyer.platforms.
        '''
        return self._get_state()

    # private

    def _get_state(self):
        raise NotImplementedError()