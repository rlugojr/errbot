#!/usr/bin/env python3
from jinja2 import Template
template = Template(open('plugins.md').read())

blacklisted = [repo.strip() for repo in open('blacklisted.txt', 'r').readlines()]

with open('plugins.txt', 'r') as p:
    plugins = [eval(line) for line in p]
    # Removes the weird forks of errbot itself.
    plugins = [plugin for plugin in plugins if not plugin['path'].startswith('errbot')]

    # Be sure to remove the blacklisted ones.
    plugins = [plugin for plugin in plugins if plugin['repo'] not in blacklisted]

    # Removes dupes from the same repos.
    plugins = {(plugin['repo'], plugin['name']): plugin for plugin in plugins}.values()

    plugins = sorted(plugins, key=lambda plug: plug['name'])

    with open('Home.md', 'w') as out:
        out.write(template.render(plugins=plugins))
