from spec2scl import settings
from spec2scl.decorators import matches
from spec2scl.transformer import Transformer

class RTransformer(Transformer):
    def __init__(self, options={}):
        super(RTransformer, self).__init__(options)

    @matches(r'R\s+CMD', one_line=False, sections=settings.RUNTIME_SECTIONS)
    def handle_R_specific_commands(self, original_spec, pattern, text):
        return self.sclize_all_commands(pattern, text)
