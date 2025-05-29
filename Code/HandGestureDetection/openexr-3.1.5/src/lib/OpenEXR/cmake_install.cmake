# Install script for directory: /home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR

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
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so.30.5.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so.30"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "\$ORIGIN/../lib:/usr/local/lib:/home/nadav/.local/share/mamba/envs/RPS-env/lib")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/libOpenEXR-3_1.so.30.5.1"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/libOpenEXR-3_1.so.30"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so.30.5.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so.30"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/home/nadav/.local/share/mamba/envs/RPS-env/lib:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/IlmThread:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex:"
           NEW_RPATH "\$ORIGIN/../lib:/usr/local/lib:/home/nadav/.local/share/mamba/envs/RPS-env/lib")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so"
         RPATH "\$ORIGIN/../lib:/usr/local/lib:/home/nadav/.local/share/mamba/envs/RPS-env/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/libOpenEXR-3_1.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so"
         OLD_RPATH "/home/nadav/.local/share/mamba/envs/RPS-env/lib:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/IlmThread:/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/Iex:"
         NEW_RPATH "\$ORIGIN/../lib:/usr/local/lib:/home/nadav/.local/share/mamba/envs/RPS-env/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libOpenEXR-3_1.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/OpenEXR" TYPE FILE FILES
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfAcesFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfArray.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfBoxAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfChannelList.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfChannelListAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfChromaticities.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfChromaticitiesAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfCompositeDeepScanLine.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfCompression.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfCompressionAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfConvert.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfCRgbaFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepCompositing.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepFrameBuffer.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepImageState.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepImageStateAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepScanLineInputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepScanLineInputPart.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepScanLineOutputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepScanLineOutputPart.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepTiledInputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepTiledInputPart.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepTiledOutputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDeepTiledOutputPart.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfDoubleAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfEnvmap.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfEnvmapAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfExport.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfFloatAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfFloatVectorAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfForward.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfFrameBuffer.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfFramesPerSecond.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfGenericInputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfGenericOutputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfHeader.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfHuf.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfIDManifest.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfIDManifestAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfInputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfInputPart.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfInt64.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfIntAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfIO.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfKeyCode.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfKeyCodeAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfLineOrder.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfLineOrderAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfLut.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfMatrixAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfMultiPartInputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfMultiPartOutputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfMultiView.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfName.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfNamespace.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfOpaqueAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfOutputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfOutputPart.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfPartHelper.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfPartType.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfPixelType.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfPreviewImage.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfPreviewImageAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfRational.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfRationalAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfRgba.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfRgbaFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfRgbaYca.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfStandardAttributes.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfStdIO.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfStringAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfStringVectorAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTestFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfThreading.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTileDescription.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTileDescriptionAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTiledInputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTiledInputPart.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTiledOutputFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTiledOutputPart.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTiledRgbaFile.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTimeCode.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfTimeCodeAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfVecAttribute.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfVersion.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfWav.h"
    "/home/nadav/RPS-hit-rep/Code/HandGestureDetection/openexr-3.1.5/src/lib/OpenEXR/ImfXdr.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND /usr/bin/cmake -E chdir "$ENV{DESTDIR}/usr/local/lib" /usr/bin/cmake -E create_symlink libOpenEXR-3_1.so libOpenEXR.so)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  message(STATUS "Creating symlink /usr/local/lib/libOpenEXR.so -> libOpenEXR-3_1.so")
endif()

