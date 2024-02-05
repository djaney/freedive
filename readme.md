## Generate dive data
```
from freediving import Dive
dive = Dive.generate(30, 1, 1)
dive.annotate_by_meters(10, "Charge")
dive.annotate_by_meters(24, "Freefall")
dive.annotate_by_meters(5, "Relax", ascend=True)
dive.peak_to_annotation("Grab tag")
x_points, y_points, annotations = dive.get_plot_data()
```

## Import from garmin FIT file
```
from freediving import fit_to_session
session = fit_to_session("samples/sample.fit")
dive = session.get_dive(0)
dive.clean()
dive.annotate_by_meters(5, "Charge")
dive.annotate_by_meters(10, "Freefall")
dive.annotate_by_meters(5, "Relax", ascend=True)
dive.peak_to_annotation("Grab tag")
x_points, y_points, annotations = dive.get_plot_data()
```
