# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/balint/workspace/gr-vna

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/balint/workspace/gr-vna/build

# Include any dependencies generated for this target.
include swig/CMakeFiles/_vna_swig.dir/depend.make

# Include the progress variables for this target.
include swig/CMakeFiles/_vna_swig.dir/progress.make

# Include the compile flags for this target's objects.
include swig/CMakeFiles/_vna_swig.dir/flags.make

swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/tagged_stream_block.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gnuradio.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/realtime.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/block.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/block_detail.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/constants.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/sync_block.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_shared_ptr.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/block_gateway.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/sync_interpolator.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_types.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/basic_block.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_ctrlport.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/io_signature.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/top_block.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_extras.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/message.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/tags.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/msg_handler.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/runtime_swig.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/msg_queue.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/buffer.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_swig_block_magic.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/hier_block2.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/runtime_swig_doc.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/feval.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/sync_decimator.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_logger.i
swig/vna_swigPYTHON_wrap.cxx: swig/vna_swig_doc.i
swig/vna_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/prefs.i
swig/vna_swigPYTHON_wrap.cxx: ../swig/vna_swig.i
swig/vna_swigPYTHON_wrap.cxx: swig/vna_swig.tag
swig/vna_swigPYTHON_wrap.cxx: ../swig/vna_swig.i
	$(CMAKE_COMMAND) -E cmake_progress_report /home/balint/workspace/gr-vna/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Swig source"
	cd /home/balint/workspace/gr-vna/build/swig && /usr/bin/cmake -E make_directory /home/balint/workspace/gr-vna/build/swig
	cd /home/balint/workspace/gr-vna/build/swig && /usr/bin/swig2.0 -python -fvirtual -modern -keyword -w511 -module vna_swig -I/home/balint/workspace/gr-vna/build/swig -I/home/balint/workspace/gr-vna/swig -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/usr/include/python2.7 -I/usr/include/x86_64-linux-gnu/python2.7 -outdir /home/balint/workspace/gr-vna/build/swig -c++ -I/home/balint/workspace/gr-vna/lib -I/home/balint/workspace/gr-vna/include -I/home/balint/workspace/gr-vna/build/lib -I/home/balint/workspace/gr-vna/build/include -I/usr/include -I/usr/include -I/usr/local/include -I/home/balint/workspace/gr-vna/build/swig -I/home/balint/workspace/gr-vna/swig -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/usr/include/python2.7 -I/usr/include/x86_64-linux-gnu/python2.7 -o /home/balint/workspace/gr-vna/build/swig/vna_swigPYTHON_wrap.cxx /home/balint/workspace/gr-vna/swig/vna_swig.i

swig/vna_swig.py: swig/vna_swigPYTHON_wrap.cxx

swig/vna_swig.tag: swig/_vna_swig_swig_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /home/balint/workspace/gr-vna/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating vna_swig.tag"
	cd /home/balint/workspace/gr-vna/build/swig && ./_vna_swig_swig_tag
	cd /home/balint/workspace/gr-vna/build/swig && /usr/bin/cmake -E touch /home/balint/workspace/gr-vna/build/swig/vna_swig.tag

swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o: swig/CMakeFiles/_vna_swig.dir/flags.make
swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o: swig/vna_swigPYTHON_wrap.cxx
	$(CMAKE_COMMAND) -E cmake_progress_report /home/balint/workspace/gr-vna/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o"
	cd /home/balint/workspace/gr-vna/build/swig && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o -c /home/balint/workspace/gr-vna/build/swig/vna_swigPYTHON_wrap.cxx

swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.i"
	cd /home/balint/workspace/gr-vna/build/swig && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/balint/workspace/gr-vna/build/swig/vna_swigPYTHON_wrap.cxx > CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.i

swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.s"
	cd /home/balint/workspace/gr-vna/build/swig && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/balint/workspace/gr-vna/build/swig/vna_swigPYTHON_wrap.cxx -o CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.s

swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o.requires:
.PHONY : swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o.requires

swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o.provides: swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o.requires
	$(MAKE) -f swig/CMakeFiles/_vna_swig.dir/build.make swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o.provides.build
.PHONY : swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o.provides

swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o.provides.build: swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o

# Object files for target _vna_swig
_vna_swig_OBJECTS = \
"CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o"

# External object files for target _vna_swig
_vna_swig_EXTERNAL_OBJECTS =

swig/_vna_swig.so: swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o
swig/_vna_swig.so: swig/CMakeFiles/_vna_swig.dir/build.make
swig/_vna_swig.so: /usr/lib/x86_64-linux-gnu/libpython2.7.so
swig/_vna_swig.so: lib/libgnuradio-vna.so
swig/_vna_swig.so: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
swig/_vna_swig.so: /usr/lib/x86_64-linux-gnu/libboost_system.so
swig/_vna_swig.so: /usr/local/lib/libgnuradio-runtime.so
swig/_vna_swig.so: /usr/local/lib/libgnuradio-pmt.so
swig/_vna_swig.so: swig/CMakeFiles/_vna_swig.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX shared module _vna_swig.so"
	cd /home/balint/workspace/gr-vna/build/swig && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/_vna_swig.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
swig/CMakeFiles/_vna_swig.dir/build: swig/_vna_swig.so
.PHONY : swig/CMakeFiles/_vna_swig.dir/build

swig/CMakeFiles/_vna_swig.dir/requires: swig/CMakeFiles/_vna_swig.dir/vna_swigPYTHON_wrap.cxx.o.requires
.PHONY : swig/CMakeFiles/_vna_swig.dir/requires

swig/CMakeFiles/_vna_swig.dir/clean:
	cd /home/balint/workspace/gr-vna/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/_vna_swig.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/_vna_swig.dir/clean

swig/CMakeFiles/_vna_swig.dir/depend: swig/vna_swigPYTHON_wrap.cxx
swig/CMakeFiles/_vna_swig.dir/depend: swig/vna_swig.py
swig/CMakeFiles/_vna_swig.dir/depend: swig/vna_swig.tag
	cd /home/balint/workspace/gr-vna/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/balint/workspace/gr-vna /home/balint/workspace/gr-vna/swig /home/balint/workspace/gr-vna/build /home/balint/workspace/gr-vna/build/swig /home/balint/workspace/gr-vna/build/swig/CMakeFiles/_vna_swig.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/_vna_swig.dir/depend

