from src.graphics.track_annotations import Dot, Line, Cone, Route, RoutePoint, WorldDot

# Annotate each track with your personal indications for best route etc.
# Copy the syntax from the example shown here for the original DeepRacer track



reinvent_2018_annotations = [
    Dot(7, "L", 0, "green"),
    Dot(7, "L", 0.1, "yellow"),
    Dot(7, "R", 0.1, "yellow"),
    Dot(7, "L", 0.2, "red"),
    Dot(7, "R", 0.2, "red"),
    Line(22, "L", 0.25, "magenta", 154, 5),
    Cone(50, "R", 0.1, "orange", -100, 3, 10),
    WorldDot(6, 2, "white"),

    Route("grey", [
        RoutePoint(8, "L", 0.15, "R", 0.15),
        RoutePoint(10, "L", 0.2, "R", 0.1),
        RoutePoint(11, "L", 0.22, "R", 0.08),
        RoutePoint(12, "L", 0.24, "R", 0.06),
        RoutePoint(13, "L", 0.26, "R", 0.04),
        RoutePoint(14, "L", 0.28, "R", 0.02),
        RoutePoint(15, "L", 0.30, "R", 0.00),
        RoutePoint(16, "L", 0.30, "R", 0.00),
        RoutePoint(17, "L", 0.30, "R", 0.00),
        RoutePoint(18, "L", 0.30, "L", 0.05),
        RoutePoint(21, "L", 0.30, "L", 0.10),

    ])

    # 160 to 145    from wp 25




]

championship_cup_2019_annotations = []

roger_raceway_annotations = []

fumiaki_loop_annotations = []

summit_raceway_annotations = []

sola_2020_annotations = []

baadal_2020_annotations = []

barcelona_annotations = []

yun_speedway_annotations = []

cumulo_turnpike_annotations = []

stratus_loop_annotations = []

bowtie_annotations = []

american_speedway_annotations = []

asia_pacific_bay_loop_annotations = []

european_seaside_circuit_annotations = []
