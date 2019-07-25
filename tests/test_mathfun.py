import numpy.testing as npt
from pyfoo.mathfun import scale

def test_scale():
    npt.assert_allclose([-1,  1], scale([-2, 0]))
