#!/usr/bin/env roundup
#
# This file contains the test plan for the `mkpkg` command.
#    
#/ usage:  rerun stubbs:test -m mongodb -p mkpkg [--answers <>]
#

# Helpers
#
[[ -f ./functions.sh ]] && . ./functions.sh

# The Plan
# --------

describe "mkpkg"


# ------------------------------
# Replace this test. 
it_make_rpm() {
  DIST="$(rpm --eval %{?dist})"
  rerun mongodb: mkpkg --build-number 0
  test -f /tmp/rerun.mongodb.mkpkg.0/RPMS/x86_64/mongodb-2.2.2${DIST}-0.x86_64.rpm
}
# ------------------------------

