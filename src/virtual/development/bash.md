# Bash Command Reference

Essential bash commands, flags, and operators for daily development work.

## find - Search for Files

Search the filesystem using various criteria.

### Basic Syntax
```bash
find [path] [options] [expression]
```

### By Name
```bash
# Find files by exact name
find . -name "config.json"

# Case-insensitive name search
find . -iname "readme.md"

# Find files matching pattern
find . -name "*.log"
find . -name "test_*.py"
```

### By Type
```bash
# Find only files
find . -type f

# Find only directories
find . -type d

# Find symbolic links
find . -type l
```

### By Size
```bash
# Files larger than 100MB
find . -type f -size +100M

# Files smaller than 1KB
find . -type f -size -1k

# Files exactly 50 bytes
find . -type f -size 50c

# Size units: c (bytes), k (KB), M (MB), G (GB)
```

### By Time
```bash
# Modified in last 60 minutes
find . -mmin -60

# Modified more than 24 hours ago
find . -mmin +1440

# Modified in last 7 days
find . -mtime -7

# Accessed in last day
find . -atime -1
```

### Combining Conditions
```bash
# AND (both conditions must match)
find . -type f -name "*.log" -size +10M

# OR (either condition matches)
find . -type f \( -name "*.log" -o -name "*.txt" \)

# NOT (invert condition)
find . -type f ! -name "*.md"
```

### Actions on Results
```bash
# Delete found files (careful!)
find . -name "*.tmp" -delete

# Execute command on each result
find . -name "*.txt" -exec cat {} \;

# Execute with confirmation
find . -name "*.bak" -ok rm {} \;

# Pass multiple files to command
find . -name "*.log" -exec grep "ERROR" {} +
```

### Practical Examples
```bash
# Find and remove old log files
find ./logs -name "*.log" -mtime +30 -delete

# Find large files taking up space
find . -type f -size +100M -exec ls -lh {} \;

# Find empty directories
find . -type d -empty

# Find recently modified source files
find ./src -name "*.js" -mmin -60
```

## grep - Search File Contents

Search for patterns in text files.

### Basic Usage
```bash
# Search for pattern in file
grep "error" app.log

# Search in multiple files
grep "TODO" *.js

# Recursive search in directory
grep -r "function" ./src
```

### Common Flags
```bash
# Case-insensitive search
grep -i "error" app.log

# Show line numbers
grep -n "import" main.py

# Show only filenames with matches
grep -l "const" *.js

# Show files without matches
grep -L "test" *.py

# Count matching lines
grep -c "ERROR" app.log
```

### Context Lines
```bash
# Show 2 lines after match
grep -A 2 "Exception" error.log

# Show 3 lines before match
grep -B 3 "crash" debug.log

# Show 2 lines before and after
grep -C 2 "warning" app.log
```

### Invert and Exclude
```bash
# Invert match (lines NOT matching)
grep -v "debug" app.log

# Exclude files/directories
grep -r "error" --exclude="*.min.js" ./src
grep -r "TODO" --exclude-dir="node_modules" .
```

### Regular Expressions
```bash
# Extended regex (use +, ?, |, etc.)
grep -E "error|warning|fatal" app.log

# Match whole word only
grep -w "log" app.js  # won't match "logger"

# Match start of line
grep "^Error" app.log

# Match end of line
grep "done$" output.txt
```

### Practical Examples
```bash
# Find all function definitions
grep -n "function.*{" script.js

# Find imports from specific module
grep -r "from 'react'" ./src

# Find TODO comments with context
grep -rn -C 1 "TODO" --exclude-dir="node_modules" .

# Find environment variables
grep -E "^[A-Z_]+=" .env

# Check which files use a deprecated API
grep -rl "oldFunction" ./src
```

## ps - Process Management

View running processes.

### ps aux
```bash
# Show all processes with detailed info
ps aux

# Columns: USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
# USER: process owner
# PID: process ID
# %CPU: CPU usage percentage
# %MEM: memory usage percentage
# STAT: process state (R=running, S=sleeping, Z=zombie)
```

### Filtering Processes
```bash
# Find specific process
ps aux | grep node

# Show processes for user
ps aux | grep "^username"

# Sort by CPU usage (highest first)
ps aux --sort=-%cpu | head -10

# Sort by memory usage
ps aux --sort=-%mem | head -10
```

### Other Useful ps Options
```bash
# Tree view of processes
ps auxf

# Show process hierarchy
ps -ejH

# Custom output format
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head
```

## Pipes and Redirection

### Pipe (|)
Send output from one command to another.

```bash
# Chain commands
cat access.log | grep "404" | wc -l

# Multiple pipes
ps aux | grep node | grep -v grep | awk '{print $2}'

# Process large output page by page
find . -type f | less
```

### Redirection (>, >>)
```bash
# Overwrite file with output
echo "Hello" > output.txt
ls -la > filelist.txt

# Append to file
echo "World" >> output.txt
date >> log.txt

# Redirect stderr to stdout
command 2>&1

# Redirect stdout and stderr to file
command &> output.log
command > output.log 2>&1

# Discard output
command > /dev/null 2>&1
```

### Input Redirection (<)
```bash
# Read from file as input
wc -l < input.txt

# Here document
cat << EOF > config.txt
line 1
line 2
EOF
```

## Additional Useful Commands

### xargs - Build Commands from Input
```bash
# Delete files from find results
find . -name "*.tmp" | xargs rm

# Run command on each line
cat urls.txt | xargs -I {} curl {}

# Parallel execution (4 jobs)
find . -name "*.jpg" | xargs -P 4 -I {} convert {} {}.png
```

### wc - Count Lines, Words, Bytes
```bash
# Count lines
wc -l file.txt

# Count words
wc -w file.txt

# Count characters
wc -m file.txt

# Count bytes
wc -c file.txt
```

### sort and uniq
```bash
# Sort lines alphabetically
sort file.txt

# Sort numerically
sort -n numbers.txt

# Reverse sort
sort -r file.txt

# Remove duplicate lines (requires sorted input)
sort file.txt | uniq

# Count occurrences
sort access.log | uniq -c

# Show only duplicates
sort file.txt | uniq -d
```

### head and tail
```bash
# First 10 lines (default)
head file.txt

# First 20 lines
head -n 20 file.txt

# Last 10 lines
tail file.txt

# Last 50 lines
tail -n 50 app.log

# Follow file (watch for new content)
tail -f app.log

# Follow with retry (useful for rotating logs)
tail -F app.log
```

### sed - Stream Editor
```bash
# Replace first occurrence per line
sed 's/old/new/' file.txt

# Replace all occurrences (global)
sed 's/old/new/g' file.txt

# Replace in-place (edit file directly)
sed -i 's/old/new/g' file.txt

# Delete lines matching pattern
sed '/pattern/d' file.txt

# Print only matching lines
sed -n '/pattern/p' file.txt

# Replace in specific line range
sed '10,20s/old/new/g' file.txt
```

### awk - Text Processing
```bash
# Print first column
awk '{print $1}' file.txt

# Print multiple columns
awk '{print $1, $3}' file.txt

# Filter and print
awk '$3 > 100 {print $1}' data.txt

# Sum a column
awk '{sum += $2} END {print sum}' numbers.txt

# Custom field separator
awk -F: '{print $1}' /etc/passwd
```

### tar - Archive Files
```bash
# Create archive
tar -czf archive.tar.gz directory/

# Extract archive
tar -xzf archive.tar.gz

# List contents
tar -tzf archive.tar.gz

# Extract to specific directory
tar -xzf archive.tar.gz -C /target/path

# Flags: c=create, x=extract, z=gzip, v=verbose, f=file
```

### curl - Transfer Data
```bash
# GET request
curl https://api.example.com/data

# Save to file
curl -o output.html https://example.com

# Follow redirects
curl -L https://example.com

# Send POST request
curl -X POST -d "key=value" https://api.example.com

# Send JSON
curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"test"}' https://api.example.com

# Show headers
curl -I https://example.com

# Download with progress bar
curl -# -O https://example.com/file.zip
```

## Practical Combinations

### Find and process files
```bash
# Find large log files and compress them
find ./logs -name "*.log" -size +100M -exec gzip {} \;

# Find source files and count total lines
find ./src -name "*.js" | xargs wc -l

# Find and replace across files
find . -name "*.txt" -exec sed -i 's/old/new/g' {} \;
```

### Log analysis
```bash
# Count unique IPs in access log
awk '{print $1}' access.log | sort | uniq -c | sort -rn

# Find most common errors
grep "ERROR" app.log | sort | uniq -c | sort -rn | head -10

# Monitor log for errors in real-time
tail -f app.log | grep --line-buffered "ERROR"
```

### System monitoring
```bash
# Find top CPU consumers
ps aux --sort=-%cpu | head -10

# Find which process uses port 8080
lsof -i :8080

# Monitor disk usage of directories
du -sh */ | sort -h

# Watch command output (refresh every 2s)
watch -n 2 'ps aux | grep node'
```

### File cleanup
```bash
# Remove files older than 30 days
find /tmp -type f -mtime +30 -delete

# Find and remove empty directories
find . -type d -empty -delete

# Remove duplicate lines from file
sort file.txt | uniq > cleaned.txt
```
