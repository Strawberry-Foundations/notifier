<div align="center">
  <br>
  <h1>Notifier</h1>
  <i>A simple Python library that simplifies the sending of desktop notifications!</i>
  <br>
  <br>
  <p align="center">
    <a href="https://pypi.org/project/notifier.py"><img src="https://img.shields.io/badge/Available-on%20PyPi-blue?logoColor=white&logo=Python"></a>
    <img src="https://img.shields.io/badge/Python-3.6%2B-blue?logo=python">
  </p>
</div>

## What is that?
Notifier (pynotifier) is a Python library that allows you to easily send desktop notifications. <br>
This project originally came from https://github.com/ms7m/notify-py (huge thanks), but we decided to fork this project, actively maintain it and add more features. 

## Supported Platforms

- Windows 10/11
- Windows 8.1 (*Balloon tips*)
- macOS 10 >=10.10
- Linux (*libnotify*)

| Windows 7 | Windows 8.1               | Windows 10                  | Windows 11                   | Linux                       | macOS 10 >=10.10         |
| --------- |-------------------------- | --------------------------- | ---------------------------- | --------------------------- | -----------------------  | 
| ❓       | ✅ <br>(Balloon tips)     | ✅ <br>(Toast notification) | ✅ <br>(Toast notification) | ✅ <br>(requires libnotify) | ✅ <br>(No custom icon) |


## Installation
You can install notifier with pip
```
pip install notifier.py
```

## Usage
### Send Simple Notification

```python
from notifier import Notifier

notifier = Notifier()
notifier.title = "Some title"
notifier.message = "Some message"

notifier.send()
```


### Send Notification With Icon

```python
from notifier import Notifier

notifier = Notifier()
notifier.title = "Some title"
notifier.message = "Some message"
notifier.icon = "path/to/icon.png" # .png is not supported under windows 8.1

notifier.send()
```

### Send Notification With Sound

```python
from notifier import Notifier

notifier = Notifier()
notifier.title = "Some title"
notifier.message = "Some message"
notifier.audio = "path/to/audio/file.wav" # we currently only support wav files

notifier.send()
```

### Sending with Default Notification Titles/Messages/Icons

```python
from notifier import Notifier

notifier = Notifier(
  default_notification_title="Function Message",
  default_application_name="Great Application",
  default_notification_icon="path/to/icon.png",
  default_notification_audio="path/to/sound.wav"
)

def your_function():
  # stuff happening here.
  notifier.message = "Function Result"
  notifier.send()
```

### Disabling Windows Version Detection
```python
from notifier import Notifier

notifier = Notifier(override_windows_version_detection=True)
notifier.title = "Some title"
notifier.message = "Some message"

notifier.send()
```

### Changing Windows Override Version
```python
from notifier import Notifier

notifier = Notifier(override_windows_version="8.1") # Available values: 10, 8.1
notifier.title = "Some title"
notifier.message = "Some message"

notifier.send()
```

## Inspiration and Special Thanks
- Thanks to [ms7m](https://github.com/ms7m/) for creating https://github.com/ms7m/notify-py 
- Also thanks to [jithurjacob](https://github.com/jithurjacob) for creating https://github.com/jithurjacob/Windows-10-Toast-Notifications

## Side notes
- macOS does **not** support custom icons on the fly.. You will need to bundle a customized version of the notifier embedded with your custom icon.