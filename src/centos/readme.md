# Setup CentOS machine

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
  1. tmux
      1. `git clone https://github.com/gpakosz/.tmux.git ~/.tmux`
      1. `ln -s ~/.tmux/.tmux.conf ~/.tmux.conf`
      1. add to zshrc: `work() { tmux new-session -A -s ${1:-work}; }`
