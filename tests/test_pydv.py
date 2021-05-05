
import os
import sys

import numpy as np

PDV_ROOT = "/Users/rusu1/pydv"
TEST_ROOT = os.path.join("/Users/rusu1/pydv", "tests")

sys.path.append(os.path.join(PDV_ROOT, "pydv"))
import pdv

main = pdv.Command()
main.app = pdv.QApplication()
main.plotter = pdv.pdvplot.Plotter(main)

def test_read():
    main.do_read(os.path.join(TEST_ROOT, 'testData.txt'))
    assert len(main.curvelist) == 2
    assert main.curvelist[0].name == 'darkness'
    np.testing.assert_array_equal(main.curvelist[0].x, np.array([0, 1, 2, 3, 4]))
    np.testing.assert_array_equal(main.curvelist[0].y, np.array([0, 1, 4, 9, 16]))
    assert main.curvelist[1].name == 'lightness'
    np.testing.assert_array_equal(main.curvelist[1].x, np.array([0, 1, 2, 3, 4]))
    np.testing.assert_array_equal(main.curvelist[1].y, np.array([5, 4, 2.5, 2.1, 2]))

def test_debug():
    main.do_debug('on')
    assert main.debug
    main.do_debug('0')
    assert not main.debug

def test_cur():
    main.do_cur('1 2')
    assert len(main.plotlist) == 2
    assert main.plotlist[0].name == 'darkness'
    np.testing.assert_array_equal(main.plotlist[0].x, np.array([0, 1, 2, 3, 4]))
    np.testing.assert_array_equal(main.plotlist[0].y, np.array([0, 1, 4, 9, 16]))
    assert main.plotlist[1].name == 'lightness'
    np.testing.assert_array_equal(main.plotlist[1].x, np.array([0, 1, 2, 3, 4]))
    np.testing.assert_array_equal(main.plotlist[1].y, np.array([5, 4, 2.5, 2.1, 2]))
    assert main.plotedit

def test_L1():
    main.do_L1('a b')
    assert len(main.plotlist) == 3
    assert main.plotlist[2].name == 'L1 of A and B'
    np.testing.assert_array_equal(main.plotlist[2].x, np.array([0, 1, 2, 3, 4]))
    np.testing.assert_array_equal(main.plotlist[2].y, np.array([0, 4, 6.25, 10.45, 20.9]))

def test_L2():
    main.do_L2('a b 3.0 5.5')
    assert len(main.plotlist) == 4
    assert main.plotlist[3].name == 'L2 of A and B'
    np.testing.assert_array_equal(main.plotlist[3].x, np.array([3, 4]))
    np.testing.assert_allclose(main.plotlist[3].y, np.array([0, 11.03653025]))

def test_delete():
    main.do_del('c d')
    assert len(main.plotlist) == 2
    assert main.plotedit

# def test_erase():
#     main.do_erase('')
#     assert not main.plotlist
#     assert not main.usertexts
#     assert main.plotedit

# main.app.quit()

# test_read()
# test_debug()
# test_cur()
# test_L1()
# test_L2()


x = []