#!/bin/bash
MAPPER=$1
REDUCER=$2
./${MAPPER} | sort -k 1,1 | ./${REDUCER}
