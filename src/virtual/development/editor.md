# Editor Configuration & Usage

This guide covers setup and usage for various editors, primarily focusing on Vim/Neovim with VSCode as an alternative.

## Vim/Neovim Setup

### Installation

#### Amazon Linux 3
```bash
sudo yum groups install -y Development\ tools
sudo yum install -y cmake python34-{devel,pip}
sudo pip-3.4 install neovim --upgrade
(
cd "$(mktemp -d)"
git clone https://github.com/neovim/neovim.git
cd neovim
make CMAKE_BUILD_TYPE=Release
sudo make install
)
```

#### Amazon Linux 2
```bash
sudo yum install openssl-devel
wget https://github.com/Kitware/CMake/releases/download/v3.31.4/cmake-3.31.4.tar.gz
tar -xvzf cmake-3.31.4.tar.gz
cd cmake-3.31.4
./bootstrap && make && sudo make install
export PATH="/usr/local/bin:$PATH"

git clone https://github.com/neovim/neovim
cd neovim
git checkout stable
make CMAKE_BUILD_TYPE=RelWithDebInfo
sudo make install
```

### Configuration

#### Basic Vim with Vundle
```bash
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

Basic `~/.vimrc`:
```vim
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'kien/ctrlp.vim'
Plugin 'google/vim-colorscheme-primary'
Plugin 'vim-airline/vim-airline'

call vundle#end()
filetype plugin indent on

" Navigation shortcuts
nmap <C-h> <C-w>h
nmap <C-j> <C-w>j
nmap <C-k> <C-w>k
nmap <C-l> <C-w>l
nmap <C-n> :NERDTree<CR>
nmap <C-p> :CtrlP<CR>

" Appearance
syntax on
set t_Co=256
set background=dark
colorscheme primary
set number
```

#### LazyVim
- Add Rust support: run `:LazyExtra`
- Check missed notifications: `:messages`
- Close buffer: `<leader>bd` (where `<leader>` is space)
- Jump to function: `<leader>ss`
- Navigation: `<c-o>`, `<c-i>`, `gd`

## Essential Operations

### Basic Commands
| Mode | Command | Description |
|------|---------|-------------|
| Normal | `i` / `a` | Insert before/after cursor |
| Normal | `v` | Visual mode |
| Any | `<ESC>` | Return to normal mode |

### Copy/Paste/Delete
| Command | Description |
|---------|-------------|
| `yy` | Copy whole line |
| `yaw` | Copy all word |
| `2yy` | Copy next 2 lines |
| `p` / `P` | Paste after/before |
| `2dd` | Delete next 2 lines |
| `"+` | System clipboard register |

### Window & Buffer Management
| Command | Description |
|---------|-------------|
| `:ls` | List buffers |
| `:b N` | Go to buffer N |
| `C-w s/v` | Split window horizontally/vertically |
| `C-w c` | Close current window |
| `C-w o` | Close all other windows |
| `C-w =` | Make all windows equal size |
| `C-w T` | Move window to new tab |
| `gt` | Next tab |
| `:tabc` | Close current tab |

### Navigation
| Command | Description |
|---------|-------------|
| `:e %:h[TAB]` | Edit from current file's directory |
| `C-o` / `C-i` | Navigate jump list backward/forward |
| `:ju` | Show jump list |
| `gd` | Go to definition (LazyVim) |

## VSCode Configuration

### Rust Integration
Update `settings.json`:
```json
{
  "rust-analyzer.server.path": "/Users/lky/.cargo/bin/rust-analyzer"
}
```

## Quick Reference

### Getting Started
1. Hit `<ESC>` when confused
2. Use `i` to insert, `<ESC>` to navigate
3. Basic workflow: navigate → edit → save → repeat

### Essential Help
- `:h [command]` - Show help for command
- `:q` - Quit
- `:w` - Save
- `:wq` - Save and quit

## References
- [Practical Vim Guide](https://github.com/eposts/Rich/blob/master/blog/Linux/Practical%20Vim%20Edit%20Text%20at%20the%20Speed%20of%20Thought.pdf)
- [LazyVim Documentation](https://www.lazyvim.org/)
- [Neovim Installation](https://gist.github.com/kawaz/393c7f62fe6e857cc3d9) 