import urllib

from pip.req import parse_requirements


NAME = 'nova'
GITHUB = 'https://raw.githubusercontent.com'
PROJECT = 'openstack/nova'
BRANCH = 'stable/mitaka'
REQTXT = 'requirements.txt'

pkgs = [
    ('keystone', 'openstack/keystone', 'stable/mitaka'),
    ('glance', 'openstack/nova', 'stable/mitaka'),
    ('nova', 'openstack/nova', 'stable/mitaka'),
    ('cinder', 'openstack/nova', 'stable/mitaka'),
    ('neutron', 'openstack/nova', 'stable/mitaka'),
    ('horizon', 'openstack/nova', 'stable/mitaka'),
    ('swift', 'openstack/nova', 'stable/mitaka'),
    ('ceilometer', 'openstack/nova', 'stable/mitaka'),
]

with open('docstr.js', 'w') as js_file:
    js_file.write("var DOTstring = 'dinetwork { \\\n")

    for pkg in pkgs:
        NAME, PROJECT, BRANCH = pkg
        url = '/'.join([GITHUB, PROJECT, BRANCH, REQTXT])

        txt = '-'.join([NAME, REQTXT])
        urllib.urlretrieve(url, txt)

        reqs = parse_requirements(txt, session=False)
        deps = [str(req.req.name) for req in reqs]
        for dep in deps:
            js_file.write(NAME + '->' + dep.replace('-', '_') + ';\\\n')
            print NAME + '->' + dep.replace('-', '_') + ';\\'

    js_file.write("}';")
