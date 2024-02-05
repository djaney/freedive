import unittest
from freediving.dive import Dive


class TestManuallyCreated(unittest.TestCase):
    def test_read(self):
        dive = Dive.generate(30, 1, 1)
        dive.annotate_by_meters(10, "Charge")
        dive.annotate_by_meters(24, "Freefall")
        dive.annotate_by_meters(5, "Relax", ascend=True)
        dive.peak_to_annotation("Grab tag")
        x_points, y_points, annotations = dive.get_plot_data()
        self.assertEqual([float(i) for i in range(62)], x_points)
        self.assertEqual([float(-i) for i in range(31)] + [-30 + float(i) for i in range(31)], y_points)
        self.assertEqual([
            ('Charge', (11.0, -11.0)),
            ('Freefall', (25.0, -25.0)),
            ('Grab tag', (30.0, -30.0)),
            ('Relax', (57.0, -4.0))
        ], annotations)
