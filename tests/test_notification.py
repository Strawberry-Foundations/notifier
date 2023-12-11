import stbnotifications
import pytest
import pathlib
import platform


from stbnotifications import BaseNotifier


def test_normal_notification():
    n = stbnotifications.Notifier(enable_logging=True)
    assert n.send() == True


def test_multiline_notification():
    n = stbnotifications.Notifier(enable_logging=True)
    n.message = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
    assert n.send() == True


def test_notification_with_emoji():
    n = stbnotifications.Notifier(enable_logging=True)
    n.title = "🐐"
    n.message = "also known as Kanye West"


def test_notification_with_double_quotes():
    n = stbnotifications.Notifier(enable_logging=True)
    n.title = '" Yes "Yes"'
    assert n.send() == True


def test_notification_with_special_chars():
    n = stbnotifications.Notifier(enable_logging=True)
    n.message = '"""""; """ ;;# ##>>> <<>>< </>'
    assert n.send() == True


def test_blank_message_notification():
    n = stbnotifications.Notifier(enable_logging=True)
    n.message = ""
    assert n.send() == True


def test_blank_title_notification():
    n = stbnotifications.Notifier(enable_logging=True)
    n.title = ""
    assert n.send() == True


def test_rtl_language_notification():
    n = stbnotifications.Notifier(enable_logging=True)
    n.title = "مرحبا كيف الحال؟"
    assert n.send() == True


def test_blocking_notification():
    n = stbnotifications.Notifier(enable_logging=True)
    assert n.send(block=True) == True


def test_non_blocking_notification():
    n = stbnotifications.Notifier(enable_logging=True)
    thread_notify = n.send(block=False)
    assert thread_notify.wait()


def test_custom_audio():
    n = stbnotifications.Notifier(enable_logging=True)
    n.audio = "notifypy/example_notification_sound.wav"
    assert n.send() == True


def test_custom_audio_no_file():
    n = stbnotifications.Notifier(enable_logging=True)
    with pytest.raises(stbnotifications.exceptions.InvalidAudioFormat):
        n.audio = "not a file!"


def test_non_existant_icon():
    n = stbnotifications.Notifier(enable_logging=True)
    with pytest.raises(stbnotifications.exceptions.InvalidIconPath):
        n.icon = "ttt"


def test_invalid_icon_default():
    with pytest.raises(stbnotifications.exceptions.InvalidIconPath):
        n = stbnotifications.Notifier(default_notification_icon="sadfiasjdfisaodfj")


def test_invalid_audio_default():
    with pytest.raises(stbnotifications.exceptions.InvalidAudioPath):
        n = stbnotifications.Notifier(default_notification_audio="dsaiofj/sadf/vv.wav")


def test_invalid_audio_format_default():
    with pytest.raises(stbnotifications.exceptions.InvalidAudioFormat):
        n = stbnotifications.Notifier(default_notification_audio="asdfiojasdfioj")


def test_custom_notification():
    class CustomNotificator(BaseNotifier):
        def __init__(self, **kwargs):
            pass

    n = stbnotifications.Notifier(use_custom_notifier=CustomNotificator)
    assert n._notifier_detect == CustomNotificator


def test_invalid_custom_notification():
    class CustomNotificator:
        pass

    with pytest.raises(ValueError):
        stbnotifications.Notifier(use_custom_notifier=CustomNotificator)


def test_unexposed_inherit_baseNotifier():
    with pytest.raises(NotImplementedError):

        class CustomNotificator(BaseNotifier):
            pass

        CustomNotificator().send_notification()


@pytest.mark.skipif(platform.system() != "Darwin", reason="macOS only test.")
def test_macOS_custom_notificator():
    custom_notificator_path = str(
        pathlib.Path(__file__).resolve().parent / "Notificator.app"
    )
    n = stbnotifications.Notifier(custom_mac_notificator=custom_notificator_path)
    assert (
        n._notifier._notificator_binary
        == custom_notificator_path + "/Contents/Resources/Scripts/notificator"
    )
    assert n.send() == True
