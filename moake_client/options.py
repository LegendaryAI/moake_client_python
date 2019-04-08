valid_options = [
    'swap-idiom',
    'light-verb',
    'coref',
    'wsd',
    'word-scale',
    'entity-categories',
    'debug',
    'pos-classifier',
    'strip-pp',
    'triples-verbosity',
    'triples-lemma',
    'auto-correct',
    'wikifier',
    'synonym',
    'antonym'
]

default_options = {
    'swap-idiom': True,
    'light-verb': True,
    'coref': True,
    'wsd': True,
    'word-scale': True,
    'entity-categories': True,
    'debug': False,
    'pos-classifier': 'google',
    'strip-pp': True,
    'triples-verbosity': 'loose',
    'triples-lemma': False,
    'auto-correct': 'check',
    'wikifier': True,
    'synonym': False,
    'antonym': False
}

def parameterize_options(options):
    parameterized_options = ''
    for key in options:
        parameterized_options += '{}={}&'.format(key, str(options[key]).lower())
    return parameterized_options
