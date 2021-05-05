
import os
import sys

import numpy as np

PDV_ROOT = "/Users/rusu1/pydv"

sys.path.append(os.path.join(PDV_ROOT, "pydv"))
import pdv

main = pdv.Command()
main.app = pdv.QApplication()
main.plotter = pdv.pdvplot.Plotter(main)

def test_read():
    main.do_read(os.path.join(PDV_ROOT, 'tests/testData.txt'))
    assert len(main.curvelist) == 2
    assert main.curvelist[0].name == 'darkness'
    np.testing.assert_array_equal(main.curvelist[0].x, np.array([0, 1, 2, 3, 4]))
    np.testing.assert_array_equal(main.curvelist[0].y, np.array([0, 1, 4, 9, 16]))
    assert main.curvelist[1].name == 'lightness'
    np.testing.assert_array_equal(main.curvelist[1].x, np.array([0, 1, 2, 3, 4]))
    np.testing.assert_array_equal(main.curvelist[1].y, np.array([5, 4, 2.5, 2.1, 2]))

test_read()

x = []