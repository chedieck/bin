# Custom scripts
Some scripts I've made, some really long ago (the ugly ones, I hope) and some more recently.
Some of them depends on other packages, configurations, etc; that I haven't organized here.

- amb
  +  Basically my IDE launcher. The `template.session` is in the `resources/` folder.
- dca
  +  Shortcuts to enter docker containers & execute a command.
- denoiser
  +  Clean up an audio file.
- dlt
  +  Download a song from Youtube and change the pitch. Useful for Karaoke.
- jrnl
  +  Journaling. Simple and pratical, just add the `resources/.jrnl.vim` to the journaling folder.
- mine
  +  Script to start mining. I keep this in my `.bash_profile`, to execute it automatically on `tty2`:
  ```
      if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty2 ]]; then
      read -r -p "Start mining [Y/n]?" bool
      case $bool in
      [Nn]* ) echo "Ok.";;
      * )  exec mine;;
      esac
      fi
  ```
- hey
  + Play bell and show message. Used with `remind.service`, that can be found on `resources/` together with `remind-daemon`.
- pgg
  +  Python git grep. Many improvements could be made to this one, I don't use it anymore.
- pudbtry
  +  Remote debugging with `pudb`. 
- setbg
  +  The command to set the background, used by other scripts/configuration files.
- sethdmi
  +  Utility to change monitors. Would be better if it could change the `layout.css.devPixelsPerPx` setting on firefox.
- swapkbr
  +  Toggle between russian & portuguese keyboard layouts.
- tv
  +  Search for a file and send it to the vim server created by `vss`.
- vss
  +  Create a vim server with the node id, works only with BSPWM
