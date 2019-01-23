# tmux

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
ctrl+b c

# close window
ctrl+b &

# rename window
ctrl+b ,

# previous window
ctrl+b p

# next window
ctrl+b n
```

## panes
```bash
# split horizontal
ctrl+b \"

# split vertical
ctrl+b %

# convert to a window
ctrl+b !

# close pane
ctrl+b x
```
