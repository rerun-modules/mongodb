# Generated by stubbs:add-option. Do not edit, if using stubbs.
# Created: Thu Jan 24 12:44:33 PST 2013
#
#/ usage: mongodb:mkpkg  --build-number <>  --mongo-version <2.2.2>  --target </tmp> 

# _rerun_options_parse_ - Parse the command arguments and set option variables.
#
#     rerun_options_parse "$@"
#
# Arguments:
#
# * the command options and their arguments
#
# Notes:
# 
# * Sets shell variables for any parsed options.
# * The "-?" help argument prints command usage and will exit 2.
# * Return 0 for successful option parse.
#
rerun_options_parse() {

    while [ "$#" -gt 0 ]; do
        OPT="$1"
        case "$OPT" in
            --build-number) rerun_option_check $# $1; BUILD_NUMBER=$2 ; shift ;;
            --mongo-version) rerun_option_check $# $1; MONGO_VERSION=$2 ; shift ;;
            --target) rerun_option_check $# $1; TARGET=$2 ; shift ;;
            # help option
            -?)
                rerun_option_usage
                exit 2
                ;;
            # end of options, just arguments left
            *)
              break
        esac
        shift
    done

    # Set defaultable options.
    [ -z "$MONGO_VERSION" ] && MONGO_VERSION="$(rerun_property_get $RERUN_MODULE_DIR/options/mongo-version DEFAULT)"
    [ -z "$TARGET" ] && TARGET="$(rerun_property_get $RERUN_MODULE_DIR/options/target DEFAULT)"
    # Check required options are set
    [ -z "$BUILD_NUMBER" ] && { echo >&2 "missing required option: --build-number" ; return 2 ; }
    [ -z "$MONGO_VERSION" ] && { echo >&2 "missing required option: --mongo-version" ; return 2 ; }
    [ -z "$TARGET" ] && { echo >&2 "missing required option: --target" ; return 2 ; }
    # If option variables are declared exportable, export them.

    #
    return 0
}


# Initialize the options variables to null.
BUILD_NUMBER=
MONGO_VERSION=
TARGET=


