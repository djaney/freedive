import unittest
from freediving.dive import Dive


class TestManuallyCreated(unittest.TestCase):
    def test_read(self):
        dive = Dive.generate(30, 0.7, 1)
        dive.annotate_by_meters(10, "Charge")
        dive.annotate_by_meters(24, "Freefall")
        dive.annotate_by_meters(5, "Relax", ascend=True)
        dive.peak_to_annotation("Grab tag")
        x_points, y_points, annotations = dive.get_plot_data()
        self.assertEqual([0.0,
                          1.428571,
                          2.857142,
                          4.285713,
                          5.714284,
                          7.142855,
                          8.571426,
                          9.999997,
                          11.428568,
                          12.857139,
                          14.28571,
                          15.714281,
                          17.142852,
                          18.571423,
                          19.999994,
                          21.428565,
                          22.857136,
                          24.285707,
                          25.714278,
                          27.142849,
                          28.57142,
                          29.999991,
                          31.428562,
                          32.857133,
                          34.285704,
                          35.714275,
                          37.142846,
                          38.571417,
                          39.999988,
                          41.428559,
                          42.85713,
                          44.285701,
                          45.285701,
                          46.285701,
                          47.285701,
                          48.285701,
                          49.285701,
                          50.285701,
                          51.285701,
                          52.285701,
                          53.285701,
                          54.285701,
                          55.285701,
                          56.285701,
                          57.285701,
                          58.285701,
                          59.285701,
                          60.285701,
                          61.285701,
                          62.285701,
                          63.285701,
                          64.285701,
                          65.285701,
                          66.285701,
                          67.285701,
                          68.285701,
                          69.285701,
                          70.285701,
                          71.285701,
                          72.285701,
                          73.285701], x_points)
        self.assertEqual([0.0,
                          -1.0,
                          -2.0,
                          -3.0,
                          -4.0,
                          -5.0,
                          -6.0,
                          -7.0,
                          -8.0,
                          -9.0,
                          -10.0,
                          -11.0,
                          -12.0,
                          -13.0,
                          -14.0,
                          -15.0,
                          -16.0,
                          -17.0,
                          -18.0,
                          -19.0,
                          -20.0,
                          -21.0,
                          -22.0,
                          -23.0,
                          -24.0,
                          -25.0,
                          -26.0,
                          -27.0,
                          -28.0,
                          -29.0,
                          -30.0,
                          -29.0,
                          -28.0,
                          -27.0,
                          -26.0,
                          -25.0,
                          -24.0,
                          -23.0,
                          -22.0,
                          -21.0,
                          -20.0,
                          -19.0,
                          -18.0,
                          -17.0,
                          -16.0,
                          -15.0,
                          -14.0,
                          -13.0,
                          -12.0,
                          -11.0,
                          -10.0,
                          -9.0,
                          -8.0,
                          -7.0,
                          -6.0,
                          -5.0,
                          -4.0,
                          -3.0,
                          -2.0,
                          -1.0,
                          0.0], y_points)
        self.assertEqual([('Charge', (14.28571, -10.0)),
                          ('Freefall', (34.285704, -24.0)),
                          ('Grab tag', (42.85713, -30.0)),
                          ('Relax', (68.285701, -5.0))], annotations)
