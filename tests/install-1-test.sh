#!/usr/bin/env roundup
#
# This file contains the test plan for the `install` command.
#    
#/ usage:  rerun stubbs:test -m mongodb -p install [--answers <>]
#

# Helpers
#
[[ -f ./functions.sh ]] && . ./functions.sh

# The Plan
# --------

describe "install"


# ------------------------------
# Want to be idempotent
# Start by getting pkg out
it_get_mongopkg_out_of_system() {
  if [[ $(rpm -q mongodb) -eq 0 ]]; then
    rerun mongodb: uninstall
    test "$(rpm -q mongodb)" = "1" 
  fi
}

# Check to see if package is there
it_check_pkg() {
  DIST="$(rpm --eval %{?dist})"
  if [[ ! -f /tmp/rerun.mongodb.mkpkg.0/RPMS/x86_64/mongodb-2.2.2${DIST}-0.x86_64.rpm ]]
  then
    rerun mongodb: mkpkg --build-number 0
    test -f /tmp/rerun.mongodb.mkpkg.0/RPMS/x86_64/mongodb-2.2.2${DIST}-0.x86_64.rpm
  fi
}

# Install the pkg
it_install_pkg() {
  DIST="$(rpm --eval %{?dist})"
  rerun mongodb: install --pkgurl /tmp/rerun.mongodb.mkpkg.0/RPMS/x86_64/mongodb-2.2.2${DIST}-0.x86_64.rpm
  test $(rpm -q mongodb)
  test -f /usr/bin/mongod
}

# Double install should be fine
it_double_install_pkg() {
  DIST="$(rpm --eval %{?dist})"
  rerun mongodb: install --pkgurl /tmp/rerun.mongodb.mkpkg.0/RPMS/x86_64/mongodb-2.2.2${DIST}-0.x86_64.rpm
  test $(rpm -q mongodb)
  test -f /usr/bin/mongod
}
# ------------------------------

