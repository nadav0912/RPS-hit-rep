# Install script for directory: /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/doc/OpenEXR/examples" TYPE FILE FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/drawImage.cpp"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/drawImage.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/generalInterfaceExamples.cpp"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/generalInterfaceExamples.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/generalInterfaceTiledExamples.cpp"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/generalInterfaceTiledExamples.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/lowLevelIoExamples.cpp"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/lowLevelIoExamples.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/main.cpp"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/namespaceAlias.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/previewImageExamples.cpp"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/previewImageExamples.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/rgbaInterfaceExamples.cpp"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/rgbaInterfaceExamples.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/rgbaInterfaceTiledExamples.cpp"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/examples/rgbaInterfaceTiledExamples.h"
    )
endif()

