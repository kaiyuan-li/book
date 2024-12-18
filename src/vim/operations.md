# Operations

## Quick Start

1. Whenever you are not sure where to start, just keep hitting the <ESC> key.
1. Modes
  1. `i`: insert mode
  1. `<ESC>`: into normal (navigation) mode
  1. `v`: view mode
1. Insert: `i` insert before, `a` insert after
1. Normal mode: `y`: copy, `p`: paste, `d`: delete
  1. `yy`: copy whole line, `yaw`: copy all word, `2yy`: copy the next 2 lines
  1. `p`: paste after, `P`: paste before
  1. `2dd`: delete the next 2 lines

## Cheatsheet


| Command | Discription |
|---|---|
| `:h [` | show manual/options for `[` |
| `:ls` | list buffers |
| `:b N` | go to buffer `N` |
| `C-w s/v` | split window |
| `C-w c` | close current window |
| `C-w o` | close all other windows |
| `C-w =` | make all windows equally sized |
| `C-w _`/`\|` | max current window horizontally/vertically |
| `C-w T` | move current window into new tab |
| `:tabc` | close current tab |
| `:tabo` | close other tabs |
| `gt` | next tab |
| `:e %:h[TAB]` | start editing from current file's dir |
| `` | position before last jump |
| `:ju` | list of jumps |
| `C-o C-i` | forward / backward around jumps |




## LazyVim

1. close buffer: `:bd` or `<leader>bd`, where `<leader>` is the space key
1. `<leader>ss` to jump to a function
1. `<c-o>`, `<c-i>` and `gd` to navigate the code
