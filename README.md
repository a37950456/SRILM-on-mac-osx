# SRILM-on-mac-osx
Speech recognition Spring 2018, NYUST

A. Make sure you had download :

homebrew -- The missing package manager for macOS   https://github.com/Homebrew/brew

1. C/C++ compiler：gcc 3.4.3 or latest version.

2. Tcl toolkit: 7.3 or latest，command tclsh to check, if output is % that mean you didn't need to clone.(http://www.tcl.tk/software/tcltk/）

3. GNU make  
```cmd
brew install make
```
4. GNU gawk

5. GNU gzip

6. bzip2（option）

7. P7zip（option）

8. xz(option）

9. csh：kinds of Unix shell

You can use command to check if you had already download or not.
```cmd
gawk  --v
```
http://www.speech.sri.com/projects/srilm/download.html

B. Download srilm  (I use srilm-1.7.2)

1. Find Makefile folder under srilm-1.7.2

Find the row:
```cmd
# SRILM = /home/speech/stolcke/project/srilm/devel 
```
Change to:  (xxx means your srilm location)
```cmd
SRILM = /usr/xxx/srilm-1.7.2  
```
2. Change /Users/xxx/srilm-1.7.2/common /Makefile.machine.macosx file

Find
```cmd
CC = cc $(GCC_FLAGS) 
CXX = c++ $(GCC_FLAGS) -DINSTANTIATE_TEMPLATES
```
Change to
```cmd
CC = /usr/bin/gcc $(GCC_FLAGS) 
CXX = /usr/bin/g++ $(GCC_FLAGS) -DINSTANTIATE_TEMPLATES 
```
Find
```cmd
TCL_INCLUDE = -I/usr/include 
TCL_LIBRARY = -L/usr/lib -ltcl 
```
Change to
```cmd
TCL_INCLUDE = -I/usr/include 
TCL_LIBRARY = /usr/lib/libtcl8.5.dylib 
NO_TCL = X
```
Find
```cmd
GAWK = /usr/bin/awk 
```
Change to
```cmd
GAWK = /usr/bin/gawk
```
C. Go to /Users/xxx/srilm-1.7.2
```cmd
TinadeMacBook-Air-2:srilm-1.7.2 tinatsai$ make World
```
