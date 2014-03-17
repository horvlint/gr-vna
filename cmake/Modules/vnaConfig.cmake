INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_VNA vna)

FIND_PATH(
    VNA_INCLUDE_DIRS
    NAMES vna/api.h
    HINTS $ENV{VNA_DIR}/include
        ${PC_VNA_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    VNA_LIBRARIES
    NAMES gnuradio-vna
    HINTS $ENV{VNA_DIR}/lib
        ${PC_VNA_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(VNA DEFAULT_MSG VNA_LIBRARIES VNA_INCLUDE_DIRS)
MARK_AS_ADVANCED(VNA_LIBRARIES VNA_INCLUDE_DIRS)

