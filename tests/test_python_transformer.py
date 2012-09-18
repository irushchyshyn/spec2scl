import pytest

from spec2scl.transformers.python import PythonTransformer

from transformer_test_case import TransformerTestCase

class TestPythonTransformer(TransformerTestCase):
    def setup_method(self, method):
        self.t = PythonTransformer('', {})

    @pytest.mark.parametrize(('spec', 'expected'), [
        ('%{__python} setup.py test\n', '%{?scl:scl enable %{scl} "}\n%{__python} setup.py test\n%{?scl:"}\n'),
    ])
    def test_python_specific_commands_matching(self, spec, expected):
        patterns = self.t.handle_python_specific_commands.matches
        assert self.t.handle_python_specific_commands(self.get_pattern_for_spec(patterns, spec), spec) == expected