# Custom scripts
Some scripts I've made, some really long ago (the ugly ones, I hope) and some more recently.
Many of them depends on other packages, configurations, etc; that I haven't organized here.

- adu
  +  Shortcuts to enter docker containers & execute a command.
- amb
  +  Basically my IDE. The `template.session` is in the `resources/` folder.
- denoiser
  +  Clean up an audio file.
- dlt
  +  Download a song from Youtube and change the pitch. Useful for Karaoke.
- jrnl
  +  Journaling. Simple and pratical.
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
- pgg
  +  Python git grep. Many improvements could be made to this one, but it works surprinsingly well.
- pudbtry
  +  Remote debugging with `pudb`. 
- setbg
  +  The command to set the background, used by other scripts/configuration files.
- sethdmi
  +  Utility to change monitors. Would be better if it could change the `layout.css.devPixelsPerPx` setting on firefox.
- swapkbr
  +  Toggle between russian & portuguese keyboard layouts.
- tv
  +  Python git grep. Many improvements could be made to this one, but it works surprinsingly well.
- vss
  +  Python git grep. Many improvements could be made to this one, but it works surprinsingly well.
