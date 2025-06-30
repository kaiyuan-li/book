# Linux

Linux commands. From the book of A Practical Guild to Linux Commands, Editors and Shells.

## stdio

File descriptor 0 (stdin), 1 (stdout), 2 (stderr).

* `>` is short for `1>`, meaning redirecting standard output.
* `<` is short for `0<` redirects standard input.
* `2>` redirects stardard error.

Example
```
$ cat y
This is y

$ cat x
cat: x: No such file or directory

$ cat x y
This is y
cat: x: No such file or directory
```

pipe only sends stdout not stderr
```
$ cat x y | tr "[a-z]" "[A-Z]"
cat: x: No such file or directory
THIS IS Y
```

In the next example, `1>` redirects stdout to hold, then `2>&1` declares file descriptor 2 to be a duplicate of file descriptor 1, so both stdout and stderr are redirected to hold. Notice that `1>` should happen first.
```
$ cat x y 1> hold 2>&1
$ cat hold
cat: x: No such file or directory
This is y
```
In the next example, `2>&1` means also send stderr to stdout. Then pipes stdout to `tr`

```
$ cat x y 2>&1 | tr "[a-z]" "[A-Z]"
CAT: X: NO SUCH FILE OR DIRECTORY
THIS IS Y
```

`2>&1 |` can be shortened as `|&`

pipe `|` - tunnels the output (stdout only) of left to right.

Example:
```
$ cat abstract
cab

$ cat abstract | tr abc ABC
CAB

$ tr abc ABC < abstract
CAB
```

`&&` and `||`, `cmd1 && cmd2` means run `cmd2` if `cmd1` succeeds. `cmd1 || cmd2` means run `cmd2` if `cmd1` fails.

adding `&` means running the command in the background.

`kill` can kill a job with PID or job number.
```
$ ps

11829 pts/10

$ kill 11829

$ jobs
[1]

$ kill %1
```

## Bash
`./whoson` the `./` tells the shell to look for an executable file in the working dir.

`#!/bin/bash` tells the system which shell to use. `#!` is called *hashbang* or *shebang*

`-e` will cause bash to exit when command fails. `-u` will cause bash to display a message and exit when it tries to expand an unset variable.


`d & e & f` will run `d` and `e` in the background and run `f` in the foreground.

```
[1]- Done  d
[2]+ Done  e
```
The `+` means it's the last job. `-` means it's the job before the last one.


