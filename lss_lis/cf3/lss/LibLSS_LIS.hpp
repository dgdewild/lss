// Copyright (C) 2014 Vrije Universiteit Brussel, Belgium
//
// This software is distributed under the terms of the
// GNU Lesser General Public License version 3 (LGPLv3).
// See doc/lgpl.txt and doc/gpl.txt for the license text.


#ifndef cf3_lss_LibLSS_LIS_hpp
#define cf3_lss_LibLSS_LIS_hpp


#define SANDBOX
//#undef SANDBOX


#include "cf3/common/Library.hpp"
#include "../../../lss/cf3/lss/LibLSS.hpp"


namespace cf3 {
namespace lss {


/**
 * @brief LibLSS_LIS class: Interface to LIS Library of Iterative Solvers for linear systems.
 * @author Pedro Maciel
 */
struct lss_API LibLSS_LIS :
  public cf3::common::Library
{
  /// Constructor
  LibLSS_LIS(const std::string& name) : cf3::common::Library(name) {}

  /// @return library namespace, name, description and class name
  static std::string library_namespace()    { return "cf3.lss.lis"; }
  static std::string library_name()         { return "lis"; }
  static std::string library_description()  { return "Interface to LIS Library of Iterative Solvers for linear systems."; }
  static std::string type_name()            { return "LibLSS_LIS"; }

  /// Initiate library
  void initiate();
};


}  // lss
}  // cf3


#endif // cf3_lss_LibLSS_LIS_hpp

