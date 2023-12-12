from notifier import Notifier
""
notifier = Notifier(override_windows_version_detection=True, override_windows_version="8.1")
notifier.send()