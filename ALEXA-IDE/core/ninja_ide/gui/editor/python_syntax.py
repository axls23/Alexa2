# Last Modified: 2013-09-16 by Alan Pipitone -> added lines for Al'exa-Ide

'''
('alexa', '#A', 'L'),
('alexaObj', 'App', '(ct|ge|xt):'),
('comment', '#', '\n'),
'''
syntax = {'formats': {'builtin': '%(syntax_builtin)s',
             'comment': '%(syntax_comment)s',
             'alexa_region': '%(syntax_alexa_region)s',
             'alexa_objects': '%(syntax_alexa_objects)s',
             'hexnumber': '%(syntax_number)s',
             'keyword': '%(syntax_keyword)s',
             'number': '%(syntax_number)s',
             'proper_object': '%(syntax_proper_object)s',
             'operators': '%(syntax_operators)s',
             'pending': '%(syntax_pending)s',
             'braces': '%(syntax_braces)s',
             'definition': '%(syntax_definition)s',
             'highlight_word': '%(syntax_highlight_word)s',
             'string': '%(syntax_string)s'},
 'partitions': [('pending', "#FIXME", "\n"),
                ('pending', "#TODO", "\n"),
                ('pending', "#WTF", "\n"),
                ('alexa_region', '#AppText:', '\n'),
                ('alexa_region', '#AppObject:', '\n'),
                ('alexa_region', '#AppImage:', '\n'),
                ('alexa_region', '#Alexa Log', '\n'),
                ('alexa_region', '#end...', '\n'),
                #('alexaObj', '#end App', '\n'),
                #('alexaObj', '#end Alexa', '\n'),
                ('comment', '#', '\n'),
                ('string', "[bruBRU]?'''", "(?<!\\\\)'''", True),
                ('string', "[bruBRU]?'", "(?<!\\\\)'"),
                ('string', '[bruBRU]?"""', '(?<!\\\\)"""', True),
                ('string', '[bruBRU]?"', '(?<!\\\\)"')],
 'scanner': {None: [('hexnumber', '(?<!\w)(0x|0X)([0-9a-fA-F])+'),
                    ('number', '(?<!\w)\\d+(\\.\\d*)?'),
                    ('definition',
                        ["(?<=def)\ +?\w+(?=\ *?\()",
                            "(?<=class)\ +?\w+(?=\ *?\()"]
                        ),
                    ('proper_object', ['self'],
                     '(^|[^\\.\\w])??(?<!\w|\\.)',
                     '[\\x08\\W]+?'),
                    ('braces', ['\\(', '\\)', '\\[', '\\]']),
                    ('operators',
                     ['\\+',
                      '\\=',
                      '\\-',
                      '\\<',
                      '\\>',
                     ]),
                    ('alexa_objects', 
                     ['NagiosUtils',
                      'Mouse',
                      'Log',
                      'AppObject',
                      'AppImage',
                      'AppText',
                      'Window',
                      'SearchRegion',
                      'Ocr',
                      'Process',
                      'Mail',
                      'Keyboard'],
                     '(^|[^\\.\\w])??(?<!\w|\\.)',
                     '[\\x08\\W]+?'),
                    ('keyword',
                     ['def',
                      'class',
                      'and',
                      'as',
                      'assert',
                      'break',
                      'class',
                      'continue',
                      'def',
                      'del',
                      'elif',
                      'else',
                      'except',
                      'exec',
                      'finally',
                      'for',
                      'from',
                      'global',
                      'if',
                      'import',
                      'in',
                      'is',
                      'lambda',
                      'not',
                      'or',
                      'pass',
                      'print',
                      'raise',
                      'return',
                      'try',
                      'while',
                      'with',
                      'yield'],
                     '(^|[^\\.\\w])??(?<!\w|\\.)',
                     '[\\x08\\W]'),
                    ('builtin',
                     ['ArithmeticError',
                      'AssertionError',
                      'AttributeError',
                      'BaseException',
                      'BufferError',
                      'BytesWarning',
                      'DeprecationWarning',
                      'EOFError',
                      'Ellipsis',
                      'EnvironmentError',
                      'Exception',
                      'False',
                      'FloatingPointError',
                      'FutureWarning',
                      'GeneratorExit',
                      'IOError',
                      'ImportError',
                      'ImportWarning',
                      'IndentationError',
                      'IndexError',
                      'KeyError',
                      'KeyboardInterrupt',
                      'LookupError',
                      'MemoryError',
                      'NameError',
                      'None',
                      'NotImplemented',
                      'NotImplementedError',
                      'OSError',
                      'OverflowError',
                      'PendingDeprecationWarning',
                      'ReferenceError',
                      'RuntimeError',
                      'RuntimeWarning',
                      'StandardError',
                      'StopIteration',
                      'SyntaxError',
                      'SyntaxWarning',
                      'SystemError',
                      'SystemExit',
                      'TabError',
                      'True',
                      'TypeError',
                      'UnboundLocalError',
                      'UnicodeDecodeError',
                      'UnicodeEncodeError',
                      'UnicodeError',
                      'UnicodeTranslateError',
                      'UnicodeWarning',
                      'UserWarning',
                      'ValueError',
                      'Warning',
                      'ZeroDivisionError',
                      '__import__',
                      'abs',
                      'all',
                      'any',
                      'apply',
                      'basestring',
                      'bin',
                      'bool',
                      'buffer',
                      'bytearray',
                      'bytes',
                      'callable',
                      'chr',
                      'classmethod',
                      'cmp',
                      'coerce',
                      'compile',
                      'complex',
                      'copyright',
                      'credits',
                      'delattr',
                      'dict',
                      'dir',
                      'divmod',
                      'enumerate',
                      'eval',
                      'execfile',
                      'exit',
                      'file',
                      'filter',
                      'float',
                      'format',
                      'frozenset',
                      'getattr',
                      'globals',
                      'hasattr',
                      'hash',
                      'help',
                      'hex',
                      'id',
                      'input',
                      'int',
                      'intern',
                      'isinstance',
                      'issubclass',
                      'iter',
                      'len',
                      'license',
                      'list',
                      'locals',
                      'long',
                      'map',
                      'max',
                      'memoryview',
                      'min',
                      'next',
                      'object',
                      'oct',
                      'open',
                      'ord',
                      'pow',
                      'print',
                      'property',
                      'quit',
                      'range',
                      'raw_input',
                      'reduce',
                      'reload',
                      'repr',
                      'reversed',
                      'round',
                      'set',
                      'setattr',
                      'slice',
                      'sorted',
                      'staticmethod',
                      'str',
                      'sum',
                      'super',
                      'tuple',
                      'type',
                      'unichr',
                      'unicode',
                      'vars',
                      'xrange',
                      'zip'],
                     '(^|[^\\.\\w])??(?<!\w|\\.)',
                     '[\\x08\\W]+?'),
                    #('ident', '[A-Za-z_][A-Za-z_0-9]*?')
                    ]}}
