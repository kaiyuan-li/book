# Install

NeoVim installation reference: https://gist.github.com/kawaz/393c7f62fe6e857cc3d9

## Install NeoVim on Amazon Liux 3

```
sudo yum groups install -y Development\ tools
sudo yum install -y cmake
sudo yum install -y python34-{devel,pip}
sudo pip-3.4 install neovim --upgrade
(
cd "$(mktemp -d)"
git clone https://github.com/neovim/neovim.git
cd neovim
make CMAKE_BUILD_TYPE=Release
sudo make install
)
```

## Install NeoVim on Amazon Linux 2

```
sudo yum install openssl-devel
# Find latest version of cmake at https://cmake.org/download/
wget https://github.com/Kitware/CMake/releases/download/v3.31.4/cmake-3.31.4.tar.gz
tar -xvzf cmake-3.31.4.tar.gz
cd cmake-3.31.4
# optional to keep long running process alive:
tmux new
./bootstrap
make
sudo make install


export PATH="/usr/local/bin:$PATH"

# Updated build instructions: https://github.com/neovim/neovim/blob/master/BUILD.md#quick-start
git clone https://github.com/neovim/neovim
cd neovim
git checkout stable
make CMAKE_BUILD_TYPE=RelWithDebInfo
sudo make install
```

Then install LazyVim and add support for rust.

## Installation and Configuration

Install [vundle](https://github.com/VundleVim/Vundle.vim).

```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

Create `~/.vimrc` with the following content.

```
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'scrooloose/nerdtree'
Plugin 'kien/ctrlp.vim'
Plugin 'google/vim-colorscheme-primary'
Plugin 'vim-airline/vim-airline'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

nmap <C-h> <C-w>h
nmap <C-j> <C-w>j
nmap <C-k> <C-w>k
nmap <C-l> <C-w>l

nmap <C-n> :NERDTree<CR>
nmap <C-p> :CtrlP<CR>

syntax on
set t_Co=256
set background=dark
colorscheme primary
set number
set paste
```

