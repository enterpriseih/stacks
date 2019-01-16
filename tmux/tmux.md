# tmux

```bash
# install
brew install tmux

# check version
tmux -V

# new session
tmux new

# new session with names
tmux new -s <session_name>

# exit session
exit

# show session list
tmux ls

# attach latest session
tmux a #

# attach specific session
tmux a -t <session zero-based id>
tmux a -t <session_name>
```
