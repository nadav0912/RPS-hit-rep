# Install script for directory: /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so.30.5.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so.30"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "\$ORIGIN/../lib:/usr/local/lib:/home/nadav/.local/share/mamba/envs/RPS-env/lib")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/libOpenEXRUtil-3_1.so.30.5.1"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/libOpenEXRUtil-3_1.so.30"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so.30.5.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so.30"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore:/home/nadav/.local/share/mamba/envs/RPS-env/lib:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/IlmThread:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex:"
           NEW_RPATH "\$ORIGIN/../lib:/usr/local/lib:/home/nadav/.local/share/mamba/envs/RPS-env/lib")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so"
         RPATH "\$ORIGIN/../lib:/usr/local/lib:/home/nadav/.local/share/mamba/envs/RPS-env/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/libOpenEXRUtil-3_1.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so"
         OLD_RPATH "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRCore:/home/nadav/.local/share/mamba/envs/RPS-env/lib:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/IlmThread:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex:"
         NEW_RPATH "\$ORIGIN/../lib:/usr/local/lib:/home/nadav/.local/share/mamba/envs/RPS-env/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXRUtil-3_1.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/OpenEXR" TYPE FILE FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfCheckFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfDeepImage.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfDeepImageChannel.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfDeepImageIO.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfDeepImageLevel.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfFlatImage.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfFlatImageChannel.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfFlatImageIO.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfFlatImageLevel.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfImage.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfImageChannel.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfImageChannelRenaming.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfImageDataWindow.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfImageIO.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfImageLevel.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfSampleCountChannel.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXRUtil/ImfUtilExport.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND /usr/bin/cmake -E chdir "$ENV{DESTDIR}/usr/local/lib" /usr/bin/cmake -E create_symlink libOpenEXRUtil-3_1.so libOpenEXRUtil.so)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  message(STATUS "Creating symlink /usr/local/lib/libOpenEXRUtil.so -> libOpenEXRUtil-3_1.so")
endif()

