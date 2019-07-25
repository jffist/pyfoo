import numpy.testing as npt
from pyfoo.mathfun import scale

def test_scale():
    npt.assert_allclose([-1.22474487,  0.,  1.22474487], scale([-1, 0, 1]))
