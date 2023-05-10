# Unit Testing

One very crucial state whenever building some code or package is to debug errors.
While there are many debugging methods, creating a unit test is very reliable for your current code and for any future changes.

The most known packages for unit tests are [`unittest`](https://docs.python.org/3/library/unittest.html) and [`pytest`](https://docs.pytest.org/en/latest/contents.html).
This document is based for `pytests`, although the first section will show you the differences among them.

**Content**
- [Pytest Vs Unittest](#pytest-vs-unittest)

## Pytest Vs Unittest

[`unittest`](https://docs.python.org/3/library/unittest.html) is a great package to understand unit test codes.
It is designed to organize everything within classes, with easy "set_up" and "tear_down" functions.
However, the decision of orienting the documentation on [`pytest`](https://docs.pytest.org/en/latest/contents.html) is because it is faster and allows easy multiple iterations for the same test (among many other characteristics).

As an example, let us suppose a python class named `Drawing`, which can draw squares and circles in blue and red colors. 

A `unittest` file for this example would be the following:

```python
import unittest
from drawing_pkg.drawing import Drawing


class TestDrawing(unittest.TestCase):
    def test_draw_square(self):
        """
        Test that a polygon with 4 sides is drawn
        """
        square = Drawing.draw_square()
        self.assertEqual(4, square.nof_sides)
        
    def test_colored_circle(self):
        """
        Test for checking the color argument works on the circles
        """
        circle = Drawing.draw_circle(color="blue")
        self.assertTrue(circle.is_blue)
        self.assertFalse(circle.is_red)

        circle = Drawing.draw_circle(color="red")
        self.assertTrue(circle.is_red)
        self.assertFalse(circle.is_blue)


if __name__ == "__main__":
    """ Code to run all tests within the file """
    unittest.main()
```

In this example, it is fairly clear what is being tested at every line. 
That is a very big advantage, but on the other side, it might be annoying to add many cases within the "test_colored_circle" method.

`pytest` allows to easily perform these tasks, at a faster rate too. Taking again only the "test_colored_circle" method, this should be the resulting code.

````python
import pytest
from drawing_pkg.drawing import Drawing

@pytest.mark.parametrize(
    "color, expected_blue",
    (
        ("red", "blue"),
        (False, True)
    )
)
def test_colored_circle(color, expected_blue):
    circle = Drawing.draw_circle(color=color)
    assert circle.is_blue is expected_blue
    assert circle.is_red is not expected_blue
````

This was a very small example, but `pytest.mark.parametrize` allows to set up values for different parameters in functions, meaning the current code will run twice:
1. color="red", expected_blue=False
2. color="blue", expected_blue=True

If instead of using once "parametrize" with all the arguments it would have been several (one for each argument), the total number of tests would have been the multiplication of the cases at each "parametrize".
