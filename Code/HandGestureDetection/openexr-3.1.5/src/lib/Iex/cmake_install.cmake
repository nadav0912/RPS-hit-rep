# Install script for directory: /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so.30.5.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so.30"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "\$ORIGIN/../lib:/usr/local/lib")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/libIex-3_1.so.30.5.1"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/libIex-3_1.so.30"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so.30.5.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so.30"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "::::::::::::::::::::::::::::::"
           NEW_RPATH "\$ORIGIN/../lib:/usr/local/lib")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so"
         RPATH "\$ORIGIN/../lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/libIex-3_1.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so"
         OLD_RPATH "::::::::::::::::::::::::::::::"
         NEW_RPATH "\$ORIGIN/../lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libIex-3_1.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/OpenEXR" TYPE FILE FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/Iex.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexBaseExc.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexErrnoExc.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexExport.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexForward.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexMacros.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexMathExc.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexMathFloatExc.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexMathIeeeExc.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexNamespace.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex/IexThrowErrnoExc.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND /usr/bin/cmake -E chdir "$ENV{DESTDIR}/usr/local/lib" /usr/bin/cmake -E create_symlink libIex-3_1.so libIex.so)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  message(STATUS "Creating symlink /usr/local/lib/libIex.so -> libIex-3_1.so")
endif()

