from format_string import namelist

class TestFormatString:

    def test_0(self):
        assert namelist([
            {'name': 'Bart'},
            {'name': 'Lisa'},
            {'name': 'Maggie'},
            {'name': 'Homer'},
            {'name': 'Marge'}
        ]) == 'Bart, Lisa, Maggie, Homer & Marge'
    
    def test_1(self):
        assert namelist([
            {'name': 'Bart'},
            {'name': 'Lisa'},
            {'name': 'Maggie'}
        ]) == 'Bart, Lisa & Maggie'
    
    def test_2(self):
        assert namelist([
            {'name': 'Bart'},
            {'name': 'Lisa'}
        ]) == 'Bart & Lisa'

    def test_3(self):
        assert namelist([{'name': 'Bart'}]) == 'Bart'

    def test_4(self):
        assert namelist([]) == ''