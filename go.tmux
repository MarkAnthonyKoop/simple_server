shopt -s expand_aliases
source /c/z/personal/.bashrc.aliases
# Name of the tmux session
SESSION_NAME="MySession"

# Create a new detached tmux session
tmux new-session -d -s "$SESSION_NAME"

# Send multiple commands to the new session
tmux send-keys -t "$SESSION_NAME" "echo launching server" C-m
tmux send-keys -t "$SESSION_NAME" "pw server.py &" C-m
tmux send-keys -t "$SESSION_NAME" "tail -f command_logs.log" C-m
tmux attach -t "$SESSION_NAME"
# You can send as many commands as you need using additional `tmux send-keys` lines
