import unittest
import datetime
from freediving.fitfiles import fit_to_session


class TestReadFromFit(unittest.TestCase):
    def test_read(self):
        session = fit_to_session("samples/sample.fit")
        dive = session.get_dive(0)
        dive.clean()
        dive.annotate_by_meters(5, "Charge")
        dive.annotate_by_meters(10, "Freefall")
        dive.annotate_by_meters(5, "Relax", ascend=True)
        dive.peak_to_annotation("Grab tag")
        x_points, y_points, annotations = dive.get_plot_data()

        self.assertEqual(
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0,
             19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0,
             37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0],
            x_points)
        self.assertEqual(
            [0.0, -2.169, -2.441, -2.344, -3.284, -4.092, -4.887, -4.687, -5.193, -6.44, -7.386, -7.356, -7.698, -8.809,
             -9.454, -10.542, -10.366, -10.629, -11.238, -11.337, -11.089, -10.994, -10.86, -10.969, -11.204, -11.959,
             -11.578, -11.414, -11.18, -11.023, -10.801, -10.718, -10.322, -9.983, -9.595, -9.408, -9.246, -8.879,
             -8.537, -8.117, -7.69, -7.211, -6.692, -6.139, -5.544, -4.971, -4.344, -3.856, -3.516, -3.074, -2.349,
             -1.925, -1.173, 0.0], y_points)
        self.assertEqual([('Charge', (8.0, -5.193)), ('Freefall', (15.0, -10.542)), ('Grab tag', (25.0, -11.959)),
                          ('Relax', (45.0, -4.971))], annotations)

    def test_read_with_ts(self):
        session = fit_to_session("samples/sample.fit")
        dive = session.get_dive(0)
        dive.clean()
        dive.annotate_by_meters(5, "Charge")
        dive.annotate_by_meters(10, "Freefall")
        dive.annotate_by_meters(5, "Relax", ascend=True)
        dive.peak_to_annotation("Grab tag")
        ts_points, x_points, y_points, annotations = dive.get_plot_data(with_ts=True)

        self.assertEqual(
            [datetime.datetime(2024, 1, 13, 0, 41, 25, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 26, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 27, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 28, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 29, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 30, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 31, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 32, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 33, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 34, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 35, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 36, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 37, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 38, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 39, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 40, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 41, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 42, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 43, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 44, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 45, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 46, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 47, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 48, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 49, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 50, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 51, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 52, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 53, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 54, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 55, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 56, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 57, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 58, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 41, 59, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 1, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 2, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 3, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 4, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 5, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 6, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 7, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 8, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 9, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 10, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 11, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 12, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 13, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 14, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 15, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 16, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 17, tzinfo=datetime.timezone.utc),
             datetime.datetime(2024, 1, 13, 0, 42, 18, tzinfo=datetime.timezone.utc)],
            ts_points)

    def test_get_dive_by_time(self):
        session = fit_to_session("samples/sample.fit")
        dive_expected = session.get_dive(0)
        dive_actual = session.get_dive_by_time(datetime.datetime(2024, 1, 13, 0, 41, 20, tzinfo=datetime.timezone.utc))
        self.assertIs(dive_expected, dive_actual)
