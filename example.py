from notifier import Notifier

notifier = Notifier()
notifier.override(windows_version_detection=True)
notifier.send()