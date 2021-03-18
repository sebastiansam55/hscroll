# hscroll
Neovim python plugin for horizontal scrolling

This at its core just passes through the scroll wheel signals to nvim. 
I have not tested it with gvim or neovim qt which seem to already read the scroll wheel signals.
To make it actually go I added these lines to my `init.vim`;

```
map <ScrollWheelLeft> 5z<Left>
map <ScrollWheelRight> 5z<Right>
```


## Requirements
Uses the `evdev` library, you can check out detailed installation instructions [here](https://python-evdev.readthedocs.io/en/latest/install.html)

Make sure that the user running the program is in the `input` user group.

Obviously this plugin is linux only, there is probably some library that supports similar functions, if you know about one feel free to open an pr or issue :)



## Installation
I use vim-plugged and had no issues installing via git.

`Plug 'sebastiansam55/hscroll'`



