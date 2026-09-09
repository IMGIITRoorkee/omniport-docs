"""
Sphinx extension adding "Show on GitHub" and "Edit on GitHub" links to the
sidebar.

Based on https://gist.github.com/mgedmin/6052926 by Marius Gedminas, BSD
3-clause, with a prefix added because this project's sources do not sit at the
root of its repository.
"""

import os
import warnings


def get_github_url(app, view, path):
    return 'https://github.com/{project}/{view}/{branch}/{path}'.format(
        project=app.config.edit_on_github_project,
        view=view,
        branch=app.config.edit_on_github_branch,
        path=os.path.join(app.config.edit_on_github_prefix, path),
    )


def html_page_context(app, pagename, templatename, context, doctree):
    if templatename != 'page.html':
        return

    if not app.config.edit_on_github_project:
        warnings.warn('edit_on_github_project not specified')
        return

    path = os.path.relpath(doctree.get('source'), app.builder.srcdir)
    context['show_on_github_url'] = get_github_url(app, 'blob', path)
    context['edit_on_github_url'] = get_github_url(app, 'edit', path)


def setup(app):
    app.add_config_value('edit_on_github_project', '', True)
    app.add_config_value('edit_on_github_branch', 'master', True)
    # The sources live in docs/source/, not at the repository root
    app.add_config_value('edit_on_github_prefix', '', True)
    app.connect('html-page-context', html_page_context)

    return {'parallel_read_safe': True, 'parallel_write_safe': True}
