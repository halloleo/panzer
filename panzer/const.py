""" constants for panzer code """
import os

DEBUG_TIMING = False

REQUIRE_PANDOC_ATLEAST = "1.12.1"

DEFAULT_SUPPORT_DIR = os.path.join(os.path.expanduser('~'), '.panzer')

ENCODING = 'utf8'

# keys to access type and content of metadata fields
T = 't'
C = 'c'

# list of 'kind' of items on runlist, in order they should run
RUNLIST_KIND = ['preflight', 'filter', 'postprocess', 'postflight', 'cleanup']

# 'status' of items on runlist
QUEUED = 'queued'
RUNNING = 'running'
FAILED = 'failed'
DONE = 'done'

# ast of an empty pandoc document
EMPTY_DOCUMENT = [{'unMeta': {}}, []]

# writers that give binary outputs
# these cannot be written to stdout
BINARY_WRITERS = ['odt', 'docx', 'epub', 'epub3']

# forbidden options for panzer command line
PANDOC_BAD_OPTS = ['--dump-args',
                   '--ignore-args',
                   '-D',
                   '--print-default-template',
                   '--print-default-data-file']

# forbidden options for 'commandline' metadata field
PANDOC_BAD_COMMANDLINE = ['write',
                          #'read', # read allowed in commandline metadata
                          'from',
                          'to',
                          'filter',
                          'template',
                          'output',
                          'variable',
                          'metadata',
                          'help',
                          'version',
                          'dump-args',
                          'ignore-args',
                          'print-default-template',
                          'print-default-data-file']

# additive command line options
PANDOC_OPT_ADDITIVE = ['metadata',
                       'variable',
                       'bibliography',
                       'include-in-header',
                       'include-before-body',
                       'include-after-body',
                       'css',
                       'latex-engine-opt']

# pandoc's command line options, divided by reader or writer
PANDOC_OPT_PHASE = {# general options
                    'data-dir':                'rw',
                    # reader options
                    'parse-raw':               'r',
                    'smart':                   'r',
                    'read':                    'r', # read allowed in commandline metadata
                    'old-dashes':              'r',
                    'base-header-level':       'r',
                    'indented-code-classes':   'r',
                    'default-image-extension': 'r',
                    'metadata':                'r',
                    'normalize':               'r',
                    'preserve-tabs':           'r',
                    'tab-stop':                'r',
                    'track-changes':           'r',
                    'extract-media':           'r',
                    # writer options
                    'standalone':              'w',
                    'variable':                'w',
                    'no-wrap':                 'w',
                    'columns':                 'w',
                    'table-of-contents':       'w',
                    'toc-depth':               'w',
                    'no-highlight':            'w',
                    'highlight-style':         'w',
                    'include-in-header':       'w',
                    'include-before-body':     'w',
                    'include-after-body':      'w',
                    'self-contained':          'w',
                    'offline':                 'w',
                    'html5':                   'w',
                    'html-q-tags':             'w',
                    'ascii':                   'w',
                    'reference-links':         'w',
                    'atx-headers':             'w',
                    'chapters':                'w',
                    'number-sections':         'w',
                    'number-offset':           'w',
                    'no-tex-ligatures':        'w',
                    'listings':                'w',
                    'incremental':             'w',
                    'slide-level':             'w',
                    'section-divs':            'w',
                    'email-obfuscation':       'w',
                    'id-prefix':               'w',
                    'title-prefix':            'w',
                    'css':                     'w',
                    'reference-odt':           'w',
                    'reference-docx':          'w',
                    'epub-stylesheet':         'w',
                    'epub-cover-image':        'w',
                    'epub-metadata':           'w',
                    'epub-embed-font':         'w',
                    'epub-chapter-level':      'w',
                    'latex-engine':            'w',
                    'latex-engine-opt':        'w',
                    'bibliography':            'w',
                    'csl':                     'w',
                    'citation-abbreviations':  'w',
                    'natbib':                  'w',
                    'biblatex':                'w',
                    'latexmathml':             'w',
                    'mathml':                  'w',
                    'jsmath':                  'w',
                    'mathjax':                 'w',
                    'gladtex':                 'w',
                    'mimetex':                 'w',
                    'webtex':                  'w',
                    'katex':                   'w',
                    'katex-stylesheet':        'w'}

# Adapted from https://github.com/jgm/pandoc/blob/master/pandoc.hs#L841
PANDOC_WRITER_MAPPING = {
    ""          : "markdown",
    ".tex"      : "latex",
    ".latex"    : "latex",
    ".ltx"      : "latex",
    ".context"  : "context",
    ".ctx"      : "context",
    ".rtf"      : "rtf",
    ".rst"      : "rst",
    ".s5"       : "s5",
    ".native"   : "native",
    ".json"     : "json",
    ".txt"      : "markdown",
    ".text"     : "markdown",
    ".md"       : "markdown",
    ".markdown" : "markdown",
    ".textile"  : "textile",
    ".lhs"      : "markdown+lhs",
    ".texi"     : "texinfo",
    ".texinfo"  : "texinfo",
    ".db"       : "docbook",
    ".odt"      : "odt",
    ".docx"     : "docx",
    ".epub"     : "epub",
    ".org"      : "org",
    ".asciidoc" : "asciidoc",
    ".pdf"      : "latex",
    ".fb2"      : "fb2",
    ".opml"     : "opml",
    ".1"        : "man",
    ".2"        : "man",
    ".3"        : "man",
    ".4"        : "man",
    ".5"        : "man",
    ".6"        : "man",
    ".7"        : "man",
    ".8"        : "man",
    ".9"        : "man"
}

