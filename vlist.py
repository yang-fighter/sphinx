from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging


class vlist(nodes.General, nodes.Element):
    pass

class VListDirective(SphinxDirective):
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
        node = vlist()
        node['columns'] = self.options.get('columns', 2)
        # node['classes'].append('vlist')
        # content = vlist()
        # content['columns'] = self.options.get('columns', 2)
        self.state.nested_parse(self.content, self.content_offset, node)
        # node += content
        return [node]

def html_visit_vlist_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='vlist', STYLE='column-count: %s' % self.encode(node['columns']).strip()))
    
def html_depart_vlist_node(self, node):
    self.body.append("</div>")

def print_log(app, exception):
    if app.builder.name not in ['html', 'readthedocs'] or exception:
        return
    logger = logging.getLogger(__name__)
    logger.info('vlist ext work is done')

def setup(app):

    app.add_node(vlist,
                 html=(html_visit_vlist_node, html_depart_vlist_node)
                )

    app.add_directive('vlist', VListDirective)
    app.connect('build-finished', print_log)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }