import pathlib
import os
import subprocess
import tempfile
import uuid
import codecs

from loguru import logger
from ._base import BaseNotifier

from win10toast import ToastNotifier


class WindowsLegacyNotifier(BaseNotifier):
    """Main Notification System for Windows (8.1). Uses win10toast"""
    def __init__(self, **kwargs):
        self._notifier = ToastNotifier()
        

    def send_notification(self, notification_title, notification_subtitle, notification_icon, application_name, notification_audio, **kwargs,):
        self._notifier.show_toast(notification_title, notification_subtitle, icon_path=notification_icon, duration=10)