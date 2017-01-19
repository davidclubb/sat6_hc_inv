#!/usr/bin/python
import json
import sys
try:
    import requests
except ImportError:
    print "Please install the python-requests module."
    sys.exit(-1)

HOST = 'satellite6.example.com' # Change this
USERNAME = 'username'           # Change this
PASSWORD = 'password'           # Change this
ORG_ID=1                        # Change this

SAT_API = 'https://' + HOST + '/api/v2/'
KATELLO_API = 'https://' + HOST + '/katello/api/'
SSL_VERIFY = False

def get_json(url):
    r = requests.get(url, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
    return r.json()

def get_results(url):
    jsn = get_json(url)
    if jsn.get('error'):
        print "Error: " + jsn['error']['message']
    else:
        if jsn.get('results'):
            return jsn['results']
        elif 'results' not in jsn:
            return jsn
        else:
            print "No results found"
    return None

def get_host_collections(org_id):
    url = KATELLO_API + 'organizations/' + str(org_id) + "/host_collections"
    host_collections = []
    results = get_results(url)
    if results:
         for result in results:
            host_collections.append(result['name'])
    return host_collections

def get_hosts_from_host_collection(host_collection):
    hosts = []
    url = SAT_API + 'hosts?search=host_collection=' + host_collection
    results = get_results(url)
    if results:
        for result in results:
                hosts.append(result)
    return hosts

def display_all_hosts_in_host_collections(org_id):
    hostlist = {}
    host_collections = get_host_collections(org_id)
    if host_collections:
        for host_collection in host_collections:
            hostlist[host_collection] = []
            hosts = get_hosts_from_host_collection(host_collection)
            if hosts:
                for host in hosts:
                    hostlist[host_collection].append(host['name'])

    print json.dumps(hostlist, indent=4, sort_keys=True)

def main():
    org_id = 1 
    display_all_hosts_in_host_collections(org_id)

if __name__ == "__main__":
    main()
