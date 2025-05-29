# Install script for directory: /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so.30.5.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so.30"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "\$ORIGIN/../lib:/usr/local/lib")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/libOpenEXRCore-3_1.so.30.5.1"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/libOpenEXRCore-3_1.so.30"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so.30.5.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so.30"
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
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so"
         RPATH "\$ORIGIN/../lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/libOpenEXRCore-3_1.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so"
         OLD_RPATH "::::::::::::::::::::::::::::::"
         NEW_RPATH "\$ORIGIN/../lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRCore-3_1.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/OpenEXR" TYPE FILE FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_attr.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_base.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_chunkio.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_coding.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_conf.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_context.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_decode.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_debug.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_encode.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_errors.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_part.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore/openexr_std_attr.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND /usr/bin/cmake -E chdir "$ENV{DESTDIR}/usr/local/lib" /usr/bin/cmake -E create_symlink libOpenEXRCore-3_1.so libOpenEXRCore.so)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  message(STATUS "Creating symlink /usr/local/lib/libOpenEXRCore.so -> libOpenEXRCore-3_1.so")
endif()

