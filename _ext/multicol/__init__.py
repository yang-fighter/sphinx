# -*- coding: utf-8 -*-
"""
Multiple columns specs
=================
"""
import os
from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from sphinx.util.osutil import copyfile
from sphinx.util import logging

CSS_FILE = 'multicol.css'

class multicol(nodes.General, nodes.Element):
    pass

class MultiColDirective(SphinxDirective):
    """
    Directive for a list that gets compacted horizontally.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'columns': int,
    }

    def run(self):
        node = multicol()
        node['columns'] = self.options.get('columns', 2)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

def html_visit_multicol_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='multicol', STYLE='column-count: %s' % self.encode(node['columns']).strip()))
    
def html_depart_multicol_node(self, node):
    self.body.append("</div>")

def latex_visit_multicol_node(self, node):
    self.body.append('\\begin{multicols}{%s}' % self.encode( str(node['columns'])).strip())
    
def latex_depart_multicol_node(self, node):
    self.body.append('\\end{multicols}')

def builder_inited(app):
    app.add_stylesheet(CSS_FILE)
    if app.builder.name == "latex":
        app.add_latex_package("multicol")

def copy_assets(app, exception):
    if app.builder.name not in ['html', 'readthedocs'] or exception:
        return
    logger = logging.getLogger(__name__)
    logger.info('Copying multicol stylesheet... ', nonl=True)
    dest = os.path.join(app.builder.outdir, '_static', CSS_FILE)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), CSS_FILE)
    copyfile(source, dest)
    logger.info('done')

def setup(app):

    app.add_node(multicol,
                 html=(html_visit_multicol_node, html_depart_multicol_node),
                 latex=(latex_visit_multicol_node, latex_depart_multicol_node)
                )

    app.add_directive('multicol', MultiColDirective)

    app.connect('builder-inited', builder_inited)
    app.connect('build-finished', copy_assets)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }