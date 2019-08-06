import win32api, win32con, ctypes, time

class functions():
     
    def go_to_desktop(self):
        ctypes.windll.user32.keybd_event(0x5B, 0, 0, 0)         # Press Windows Key
        ctypes.windll.user32.keybd_event(0x44, 0, 0, 0)         # Press D Key
        ctypes.windll.user32.keybd_event(0x44, 0, 0x0002, 0)    # Release D Key
        ctypes.windll.user32.keybd_event(0x5B, 0, 0x0002, 0)    # Release Windows Key

    def open_start_menu(self):
        ctypes.windll.user32.keybd_event(0x5B, 0, 0, 0)         # Press Windows Key
        ctypes.windll.user32.keybd_event(0x5B, 0, 0x0002, 0)    # Release Windows Key

    def type_paint(self):
        ctypes.windll.user32.keybd_event(0x50, 0, 0, 0)         # Press P Key
        ctypes.windll.user32.keybd_event(0x50, 0, 0x0002, 0)    # Release P Key
        ctypes.windll.user32.keybd_event(0x41, 0, 0, 0)         # Press A Key
        ctypes.windll.user32.keybd_event(0x41, 0, 0x0002, 0)    # Release A Key
        ctypes.windll.user32.keybd_event(0x49, 0, 0, 0)         # Press I Key
        ctypes.windll.user32.keybd_event(0x49, 0, 0x0002, 0)    # Release I Key
        ctypes.windll.user32.keybd_event(0x4E, 0, 0, 0)         # Press N Key
        ctypes.windll.user32.keybd_event(0x4E, 0, 0x0002, 0)    # Release N Key
        ctypes.windll.user32.keybd_event(0x54, 0, 0, 0)         # Press T Key
        ctypes.windll.user32.keybd_event(0x54, 0, 0x0002, 0)    # Release T Key

    def press_enter(self):
        ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)         # Press ENTER Key
        ctypes.windll.user32.keybd_event(0x0D, 0, 0x0002, 0)    # Release ENTER Key

    def press_alt_f4(self):
        ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)         # Press Alt Key
        ctypes.windll.user32.keybd_event(0x73, 0, 0, 0)         # Press F4 Key
        ctypes.windll.user32.keybd_event(0x73  , 0, 0x0002, 0)  # Release F4 Key
        ctypes.windll.user32.keybd_event(0x12 , 0, 0x0002, 0)   # Release Alt Key