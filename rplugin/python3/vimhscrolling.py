#!/usr/bin/python3

import pynvim

import evdev
from evdev import ecodes as e

import threading
import logging

@pynvim.plugin
class HScroll(object):
    def __init__(self, nvim):
        self.nvim = nvim
        rightscroll = nvim.replace_termcodes('<ScrollWheelRight>')
        leftscroll = nvim.replace_termcodes('<ScrollWheelLeft>')

        mouse = self.nvim.vars['hscroll_wheel']

        print("grabbing mouse device")
        m = grab_device(get_devices(), mouse)
        print("grabbed device, starting thread")
        eventthread = threading.Thread(target=event_loop, args=(self.nvim,m, rightscroll, leftscroll))
        print("thread created")
        eventthread.start()
        print("thread started")

    @pynvim.autocmd('VimEnter', pattern='*')
    def on_vim_start(self):
        print("testing")


def get_devices():
    return [evdev.InputDevice(path) for path in evdev.list_devices()]

def grab_device(devices, descriptor):
    #determine if descriptor is a path or a name
    return_device = None
    if len(descriptor) <= 2: #assume that people don't have more than 99 input devices
        descriptor = "/dev/input/event"+descriptor
    if "/dev/" in descriptor: #assume function was passed a path
        for device in devices:
            if descriptor==device.path:
                device.close()
                return_device = evdev.InputDevice(device.path)
            else:
                device.close()
    else: #assume that function was passed a plain text name
        for device in devices:
            if descriptor==device.name:
                device.close()
                return_device = evdev.InputDevice(device.path)
            else:
                device.close()

    return return_device



def event_loop(nvim, m, rightscroll, leftscroll):
    for ev in m.read_loop():
        if ev.type == e.EV_REL and ev.code == e.REL_HWHEEL:
            print(ev)
            try:
                if ev.value == 1: # scroll left
                    #nvim.command('z<Left>')
                    nvim.async_call(nvim.feedkeys, rightscroll)
                elif ev.value == -1:
                    # nvim.command('z<Right>')
                    nvim.async_call(nvim.feedkeys, leftscroll)
            except:
                pass
