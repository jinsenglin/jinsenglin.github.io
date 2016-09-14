import urllib

from pip.req import parse_requirements


NAME = 'nova'
GITHUB = 'https://raw.githubusercontent.com'
PROJECT = 'openstack/nova'
BRANCH = 'stable/mitaka'
REQTXT = 'requirements.txt'
COLOR = '#97C2FC'

pkgs = [
    ('keystone', 'openstack/keystone', 'stable/mitaka', '#97C2FC'),
    ('glance', 'openstack/nova', 'stable/mitaka', '#FFFF00'),
    ('nova', 'openstack/nova', 'stable/mitaka', '#FB7E81'),
    ('cinder', 'openstack/nova', 'stable/mitaka', '#7BE141'),
    ('neutron', 'openstack/nova', 'stable/mitaka', '#6E6EFD'),
    ('horizon', 'openstack/nova', 'stable/mitaka', '#C2FABC'),
    ('swift', 'openstack/nova', 'stable/mitaka', '#FFA807'),
    ('ceilometer', 'openstack/nova', 'stable/mitaka', '#9400D3'),
]

with open('nodes.js', 'w') as nodes_file, open('edges.js', 'w') as edges_file:
# with open('docstr.js', 'w') as js_file:
    nodes_file.write("var nodes = new vis.DataSet([\n")
    edges_file.write("var edges = new vis.DataSet([\n")
    # js_file.write("var DOTstring = 'dinetwork { \\\n")

    nodes = set()
    for pkg in pkgs:
        NAME, PROJECT, BRANCH, COLOR = pkg
        url = '/'.join([GITHUB, PROJECT, BRANCH, REQTXT])

        txt = '-'.join([NAME, REQTXT])
        urllib.urlretrieve(url, txt)

        reqs = parse_requirements(txt, session=False)
        deps = [str(req.req.name) for req in reqs]

        nodes_file.write("{id: '" + NAME + "', label: '" + NAME + "', color:'" + COLOR + "'},\n")
        for dep in deps:
            renamed_dep = dep.replace('-', '_')
            nodes.add(renamed_dep)
            edges_file.write("{from: '" + NAME + "', to: '" + renamed_dep + "', color:{highlight:'" + COLOR + "'}},\n")
            # js_file.write(NAME + '->' + dep.replace('-', '_') + ';\\\n')
            print NAME + '->' + renamed_dep + ';\\'

    for dep in nodes:
        nodes_file.write("{id: '" + dep + "', label: '" + dep + "'},\n")

    nodes_file.write("]);")
    edges_file.write("]);")
    # js_file.write("}';")
