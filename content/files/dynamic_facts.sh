#!/bin/bash

# this is an arbitrary example of how to write a dynamic executable fact
# see user_facts.py in this repo for an example of usage.

DATE=`date`

echo '{ "user_date" : "${date}" }'

