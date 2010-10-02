#!/bin/bash

# Defaults.
base_url='https://my.nrao.edu/nrao-2.0/secure/QueryFilter.htm'
dest_dir=coversheet
cookie=cookie.txt
service=${base_url}'?coversheetByLegacyId='
[[ -n "$PROPOSAL_ID" ]] && service=${base_url}'?coversheetByProposalId='

# Givens.
app=`basename $0`
project_id=$1
dest=${dest_dir}/${project_id/\//}.xml
target=${service}${project_id}

# Helpers.
function fail () {
    echo "$app: $@" 1>&2
    exit 1
}

function usage () {
    echo "usage: $app project_id" 1>&2
    exit 2
}

# Set up.
mkdir -p $dest_dir

# Flight check.
[[ -x `which curl` ]] || fail program curl not found
[[ -e $dest_dir ]] || fail destination directory $dest_dir not found
[[ -e $cookie ]] || fail cookie $cookie not found
[[ -e $dest ]] && fail destination file $dest already exists
[[ -n "$project_id" ]] || usage

# Ready for takeoff.
echo saving $target to $dest 1>&2
curl -b $cookie $target > $dest

# Test for empty output file.
# [[ ! -s $dest ]] tests for a file of non-zero size. Matches man page?
[[ ! -s $dest ]] && rm -f $dest && fail no coversheet. check input and cookie

echo "-> \`$dest'" 1>&2
