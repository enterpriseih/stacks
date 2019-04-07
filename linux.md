# centos

## basic

```bash
# check disk
df -h

# check dir size
du -sh my_dir
du -h --max-depth=1


# check port
netstat -tulpn

# check cpu
cat /proc/cpuinfo | grep processor
lscpu

# check memory
cat /proc/meminfo

# check kernel
uname -a

# check ip
hostname -i

# show ip
ip addr show

# show filesystem hierachy
man hier

# list of all available encodings
iconv --list

# find file
find / -name <file_name_prefix>*.jar
```

## cat

concatenate files

```bash
# print file w/ line number
cat -n <file>

# show file1 and file2 content
cat <input_file> <output_file>

# copy file1 to file2
cat <input_file> > <output_file>

# append file1 to the end of file2
cat <input_file> >> <output_file>

# omit the repeated empty
cat -s <file>

# display TAB
cat -T <file>

# display end-of-line
cat -e <file>
```

## grep

general regular expression print

```bash
# invert search result
grep -v <pattern> <file>

# show line number
grep -n <pattern> <file>

# recursive search, skip symlinks, show only filenames
grep -lr <pattern> <file_pattern>

# multiple search pattern, use basic regex joined by \|
grep 'pattern1\|pattern2' <file>

# basic regex feature with meta-characters
# ^   start of line
# $   end of line
# .   any single character
# []  any single character enclosed
# [^] any single character except enclosed
# \  escape meta character
grep "^patt.[^r]n$" <file>

# extended regex
grep -E "pattern1|pattern2" <file>

# search lines end with ,
grep ',[[:cntrl:]]*$' <file>

# basic regex
# char * . ^ $ [] [^]
grep <file>

# extended regex
# ? + () {} |
grep -E <file>
```

## sed

a stream editor

```bash

```

## hexdump

display  file contents in hexadecimal, decimal, octal, or ascii

```bash
# 0a -> LF
# 0d -> CR
hexdump -e '"%08_ad (0x%08_ax)    "8/1 "%02x ""   "8/1 "%02x "' -e '"    "8/1 "%_p""|"8/1 "%_p""\n"'  <file>
```

## curl

```bash
# download file
curl -O <address>

# post
curl <address> -H "Content-Type: application/json" -X POST -d '{"key1":"value1", "key2":"value2"}'
curl <address> -H "Content-Type: application/json" -X POST -d '@data.json'
```
