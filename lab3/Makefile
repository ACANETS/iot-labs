# This is needed only for *compiling* the dotstar.so file (Python module).
# Not needed for just running the Python code with a precompiled .so file.

all: dotstar.so

CFLAGS=-Ofast -fomit-frame-pointer \
 -I/opt/vc/include \
 -L/opt/vc/lib

dotstar.so: dotstar.o
	gcc -s -shared -Wl,-soname,libdotstar.so,-L/opt/vc/lib,-lbcm_host -o $@ $<

.c.o:
	gcc $(CFLAGS) -c $<

clean:
	rm -f dotstar.o dotstar.so
