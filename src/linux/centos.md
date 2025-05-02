# Setup CentOS machine (AWS Amazon Linux 2023)

## Installations
  1. [VIM](https://book.fib1123.com/vim/install.html)
  1. zsh
      1. `sudo yum install zsh`
      1. set zsh as default by editing `/etc/passwd`
      1. `sudo yum install git`
      1. install OhMyZsh `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
      1. install PowerLevel10k: `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k`
      1. change theme to it in `~/.zshrc`: `ZSH_THEME="powerlevel10k/powerlevel10k"`
      1. `source ~/.zshrc`
      1. install zsh-autosuggestions: [ref](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)
      1. install zsh-syntax-highlighting: [ref](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md#oh-my-zsh)
<<<<<<< Updated upstream
=======
  1. tmux
      1. `git clone https://github.com/gpakosz/.tmux.git ~/.tmux`
      1. `ln -s ~/.tmux/.tmux.conf ~/.tmux.conf`
      1. add to zshrc: `work() { tmux new-session -A -s ${1:-work}; }`
```
# ~/.tmux.conf

# make delay shorter
set -sg escape-time 0

### key bindings ###
bind r source-file ~/.tmux.conf \; display ".tmux.conf reloaded!"

# quickly open a new window
bind N new-window

# synchronize all panes in a window
bind y setw synchronize-panes

# pane movement shortcuts
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# enable mouse support for switching panes/windows
set -g mouse on
#### copy mode : vim ####
# set vi mode for copy mode
setw -g mode-keys vi
# copy mode using 'Esc'
unbind [
bind Escape copy-mode
# paste using 'p'
unbind p
bind p paste-buffer

set-option -g default-shell "/bin/zsh"
```

  1. github
      1. `curl -Lo gh-cli.rpm https://github.com/cli/cli/releases/download/v2.30.0/gh_2.30.0_linux_arm64.rpm`
      1. `sudo yum install -y ./gh-cli.rpm`

  1. docker
      1. `sudo dnf update -y`
      1. `sudo dnf install -y docker`
      1. `sudo systemctl enable docker`
      1. `sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
      1. `sudo chmod +x /usr/local/bin/docker-compose`
      1. `docker-compose --version`
