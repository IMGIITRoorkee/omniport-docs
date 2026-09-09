"""
Sphinx extension linking each page to the source it was written from.

Pages declare their sources in a field list above the title, one
``<repo>/<path>`` per line.
"""

import os
import warnings


def html_page_context(app, pagename, templatename, context, doctree):
    if templatename != 'page.html':
        return

    declared = app.env.metadata.get(pagename, {}).get('sourcefiles')
    if not declared:
        return

    sources = []
    for entry in declared.split('\n'):
        entry = entry.strip()
        if not entry:
            continue
        repo, _, path = entry.partition('/')
        if not path:
            warnings.warn(
                f'{pagename}: sourcefiles entry "{entry}" names no path'
            )
            continue
        sources.append({
            'repo': repo,
            'path': path,
            'name': os.path.basename(path),
            'url': 'https://github.com/{org}/{repo}/blob/{branch}/{path}'.format(
                org=app.config.source_files_org,
                repo=repo,
                branch=app.config.source_files_branch,
                path=path,
            ),
        })

    context['source_files'] = sources


def setup(app):
    app.add_config_value('source_files_org', 'IMGIITRoorkee', True)
    app.add_config_value('source_files_branch', 'master', True)
    app.connect('html-page-context', html_page_context)

    return {'parallel_read_safe': True, 'parallel_write_safe': True}
