
list( APPEND lis_files
  LibLSS_LIS.cpp
  LibLSS_LIS.hpp
  LIS.cpp
  LIS.hpp )


if(CF3_HAVE_LIS)
  coolfluid3_add_library(
    TARGET   coolfluid_lss_lis
    LIBS     coolfluid_lss ${LIS_LIBRARIES}
    SOURCES  ${lis_files}
    INCLUDES ${LIS_INCLUDE_DIRS} )
else()
  coolfluid_mark_not_orphan( ${lis_files} )
endif()

