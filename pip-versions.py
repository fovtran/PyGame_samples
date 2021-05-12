import json
import urllib3
from distutils.version import StrictVersion

def versions(package_name):
    url = "https://pypi.org/pypi/%s/json" % (package_name,)
    http = urllib3.PoolManager()
    data = json.loads(http.request('GET', url).data)
    versions = data["releases"].keys()
    return versions

print ("\n".join(versions("ipython")))