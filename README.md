# sat6_hc_inv
Satellite 6 inventory based on host collections.

The script produces a json-formatted list of host collections and their associated hosts.
It can for example be used as an inventory script in Ansible Tower.
Quick and dirty based on the official documentation:
https://access.redhat.com/documentation/en/red-hat-satellite/6.2/paged/api-guide/43-api-examples-using-python

Tested with Red Hat Satellite 6.2.4, Tower 3.0.3 and Python 2.7.5


Example output:

{
    "Host collection 1": [
        "host1.example.com", 
        "host2.example.com"
        "host3.example.com"
    ], 
    "Host collection 2": [
        "host3.example.com", 
        "host4.example.com"
        "host5.example.com"
    ]
}


