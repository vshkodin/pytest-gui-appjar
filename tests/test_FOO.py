import pytest



class TestClass:
    @pytest.mark.parametrize("x", [0, 1])
    def test_inclass(self,x):
        assert x==0


class TestClassSession:
    def test_inclass_zz(self):
        assert 0

    @pytest.mark.parametrize("x", [0, 1])
    def test_inclass_zz_bb(self,x):
        assert 0