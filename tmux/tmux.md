# tmux

<PREFIX> = <Ctrl+b> by default, my preference is <Ctrl-a>

```bash
# install
brew install tmux

# check version
tmux -V
```

## session
```bash
# new session
tmux new

# new session with names
tmux new -s <session_name>

# exit session
exit

# show session list
tmux ls
tmux list-sessions

# attach latest session
tmux a #
tmux attach-session

# attach specific session
tmux a -t <session zero-based id>
tmux a -t <session_name>

# kill session
tmux kill-session -t <session_name>
```

## window
```bash
# create new window
<PREFIX> c

# close window
<PREFIX> &

# rename window
<PREFIX> ,

# previous window
<PREFIX> p

# next window
<PREFIX> n
```

## panes
```bash
# split horizontal
<PREFIX> \"

# split vertical
<PREFIX> %

# convert to a window
<PREFIX> !

# close pane
<PREFIX> x

# copy
<PREFIX> [

# paste
<PREFIX> ]

# enable paste to clipboard
# in iTerm2 Preference > General, click
# applications in terminal may access clipboard
```
