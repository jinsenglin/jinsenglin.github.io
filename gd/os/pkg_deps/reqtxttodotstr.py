import urllib

from pip.req import parse_requirements


NAME = 'nova'
GITHUB = 'https://raw.githubusercontent.com'
PROJECT = 'openstack/nova'
BRANCH = 'stable/mitaka'
REQTXT = 'requirements.txt'

pkgs = [
    ('keystone', 'openstack/keystone', 'stable/mitaka'),
    ('nova', 'openstack/nova', 'stable/mitaka'),
]

for pkg in pkgs:
    NAME, PROJECT, BRANCH = pkg
    url = '/'.join([GITHUB, PROJECT, BRANCH, REQTXT])

    txt = '-'.join([NAME, REQTXT])
    urllib.urlretrieve(url, txt)

    reqs = parse_requirements(txt, session=False)
    deps = [str(req.req.name) for req in reqs]
    for dep in deps:
        print NAME + '->' + dep.replace('-', '_') + ';\\'
