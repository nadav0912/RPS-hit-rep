# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
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
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5

# Include any dependencies generated for this target.
include src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/compiler_depend.make

# Include the progress variables for this target.
include src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/progress.make

# Include the compile flags for this target's objects.
include src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/flags.make

src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o: src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/flags.make
src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o: src/bin/exrmultipart/exrmultipart.cpp
src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o: src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o"
	cd /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o -MF CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o.d -o CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o -c /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart/exrmultipart.cpp

src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/exrmultipart.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/exrmultipart.dir/exrmultipart.cpp.i"
	cd /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart/exrmultipart.cpp > CMakeFiles/exrmultipart.dir/exrmultipart.cpp.i

src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/exrmultipart.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/exrmultipart.dir/exrmultipart.cpp.s"
	cd /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart/exrmultipart.cpp -o CMakeFiles/exrmultipart.dir/exrmultipart.cpp.s

# Object files for target exrmultipart
exrmultipart_OBJECTS = \
"CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o"

# External object files for target exrmultipart
exrmultipart_EXTERNAL_OBJECTS =

bin/exrmultipart: src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/exrmultipart.cpp.o
bin/exrmultipart: src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/build.make
bin/exrmultipart: src/lib/OpenEXR/libOpenEXR-3_1.so.30.5.1
bin/exrmultipart: /home/nadav/.local/share/mamba/envs/RPS-env/lib/libImath.so.29.11.0
bin/exrmultipart: src/lib/IlmThread/libIlmThread-3_1.so.30.5.1
bin/exrmultipart: src/lib/Iex/libIex-3_1.so.30.5.1
bin/exrmultipart: /usr/lib/aarch64-linux-gnu/libz.so
bin/exrmultipart: src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../../bin/exrmultipart"
	cd /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/exrmultipart.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/build: bin/exrmultipart
.PHONY : src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/build

src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/clean:
	cd /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart && $(CMAKE_COMMAND) -P CMakeFiles/exrmultipart.dir/cmake_clean.cmake
.PHONY : src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/clean

src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/depend:
	cd /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5 /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5 /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/bin/exrmultipart/CMakeFiles/exrmultipart.dir/depend

