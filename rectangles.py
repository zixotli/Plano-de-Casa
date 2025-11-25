import numpy as np

TOTAL_AREA = 300
DECIMAL_ACCURACY = 2

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Structure():
    def __init__(self, origin: Point, height: float, width: float, name: str):
        self.name = name
        self.origin = origin
        self.height = height
        self.width = width
        self.limit = Point(round(origin.x + width, DECIMAL_ACCURACY), round(origin.y + height, DECIMAL_ACCURACY))

    @classmethod
    def from_origin_limit(cls, origin: Point, limit: Point, name: str):
        width = limit.x - origin.x
        height = limit.y - origin.y
        return cls(origin, height, width, name)

    def __str__(self):
        return (
            f"{self.name:<12} "
            f"{self.origin.x:>6.2f}, {self.origin.y:>6.2f}   "
            f"{self.limit.x:>6.2f}, {self.limit.y:>6.2f}   "
            f"area: {self.get_area():>6.2f}"
        )

    def get_area(self):
        return round(abs(self.height * self.width), DECIMAL_ACCURACY)

#####################################################################################

ORIGIN = np.array([0,0])
BORDER = np.array([10,30])
WALL = np.array([.15,.15])

# --------------------------------------- #

SQUARE_LEFT = 3.3
SQUARE_CENTER_X = 3.3
SQUARE_RIGHT = 3.1

# --------------------------------------- #

SQUARE_BOTTOM = 4.1
SQUARE_CENTER_Y = 4.8
SQUARE_TOP = 4.25

SQUARES_DELIMITER_HEIGHT = 13.3

#####################################################################################

LEFT_HALL_ORIGIN = Point(WALL[1], SQUARES_DELIMITER_HEIGHT)
LEFT_HALL_WIDTH = 1.26
LEFT_HALL_HEIGHT = BORDER[1] - WALL[1] - SQUARES_DELIMITER_HEIGHT
LEFT_HALL_STRUCTURE_NAME = "LEFT HALL"

LEFT_HALL = Structure(origin=LEFT_HALL_ORIGIN, height=LEFT_HALL_HEIGHT, width=LEFT_HALL_WIDTH, name=LEFT_HALL_STRUCTURE_NAME)

# --------------------------------------- #

PATIO_ORIGIN = Point(LEFT_HALL.limit.x, SQUARES_DELIMITER_HEIGHT)
PATIO_HEIGHT = 4.30
PATIO_WIDTH = 7.24
PATIO_STRUCTURE_NAME = "PATIO"

PATIO = Structure(origin=PATIO_ORIGIN, height=PATIO_HEIGHT, width=PATIO_WIDTH, name=PATIO_STRUCTURE_NAME)

# --------------------------------------- #

RIGHT_HALL_ORIGIN = Point(PATIO.limit.x, SQUARES_DELIMITER_HEIGHT)
RIGHT_HALL_WIDTH = 1.20
RIGHT_HALL_HEIGHT = BORDER[1] - WALL[1] - SQUARES_DELIMITER_HEIGHT
RIGHT_HALL_STRUCTURE_NAME = "RIGHT HALL"

RIGHT_HALL = Structure(origin=RIGHT_HALL_ORIGIN, height=RIGHT_HALL_HEIGHT, width=RIGHT_HALL_WIDTH, name=RIGHT_HALL_STRUCTURE_NAME)

#####################################################################################

PATIO_TO_DOOR = 2.45
DOOR = 1.05

LIVING_ROOM_ORIGIN = Point(PATIO.origin.x + PATIO_TO_DOOR + DOOR, PATIO.limit.y)
LIVING_ROOM_HEIGHT = 5
LIVING_ROOM_WIDTH = -3.25
LIVING_ROOM_STRUCTURE_NAME = "LIVING ROOM"

LIVING_ROOM = Structure(origin=LIVING_ROOM_ORIGIN, height=LIVING_ROOM_HEIGHT, width=LIVING_ROOM_WIDTH, name=LIVING_ROOM_STRUCTURE_NAME)

# --------------------------------------- $

LIVING_ROOM_TO_INTERSECTION = 3.5
INTERSECTION_ORIGIN = Point(LIVING_ROOM_ORIGIN.x, PATIO.limit.y+ LIVING_ROOM_TO_INTERSECTION)
INTERSECTION_HEIGHT = 1.2
INTERSECTION_WIDTH = 1.05
INTERSECTION_STRUCTURE_NAME = "INTERSECTION"

INTERSECTION = Structure(origin=INTERSECTION_ORIGIN, height=INTERSECTION_HEIGHT, width=INTERSECTION_WIDTH, name=INTERSECTION_STRUCTURE_NAME)

# --------------------------------------- $

HOUSE_CORNER_DELIMITER = round(LIVING_ROOM.origin.x - abs(LIVING_ROOM.width), DECIMAL_ACCURACY)
DINING_ROOM_ORIGIN = Point(HOUSE_CORNER_DELIMITER, LIVING_ROOM.limit.y)
DINING_ROOM_HEIGHT = 2.95
DINING_ROOM_WIDTH = 3.25
DINING_ROOM_STRUCTURE_NAME = "DINING_ROOM"

DINING_ROOM = Structure(origin=DINING_ROOM_ORIGIN, height=DINING_ROOM_HEIGHT, width=DINING_ROOM_WIDTH, name=DINING_ROOM_STRUCTURE_NAME)

# --------------------------------------- $

KITCHEN_ORIGIN = Point(HOUSE_CORNER_DELIMITER, DINING_ROOM.limit.y)
KITCHEN_HEIGHT = 3.00
KITCHEN_WIDTH = 2.50
KITCHEN_STRUCTURE_NAME = "KITCHEN"

KITCHEN = Structure(origin=KITCHEN_ORIGIN, height=KITCHEN_HEIGHT, width=KITCHEN_WIDTH, name=KITCHEN_STRUCTURE_NAME)

# --------------------------------------- $

BATHROOM_ORIGIN = Point(INTERSECTION.limit.x, INTERSECTION.origin.y)
BATHROOM_HEIGHT = 1.40
BATHROOM_WIDTH = 2.45
BATHROOM_STRUCTURE_NAME = "BATHROOM"

BATHROOM = Structure(origin=BATHROOM_ORIGIN, height=BATHROOM_HEIGHT, width=BATHROOM_WIDTH, name=BATHROOM_STRUCTURE_NAME)

# --------------------------------------- $

WALL_THICKNESS = .20
ROOM_ONE_ORIGIN = Point(LIVING_ROOM_ORIGIN.x + WALL_THICKNESS, LIVING_ROOM_ORIGIN.y + WALL_THICKNESS)
ROOM_ONE_HEIGHT = 3.20
ROOM_ONE_WIDTH = 3.25
ROOM_ONE_STRUCTURE_NAME = "ROOM_ONE"

ROOM_ONE = Structure(origin=ROOM_ONE_ORIGIN, height=ROOM_ONE_HEIGHT, width=ROOM_ONE_WIDTH, name=ROOM_ONE_STRUCTURE_NAME)

# --------------------------------------- $

ROOM_TWO_ORIGIN = Point(INTERSECTION.origin.x + WALL_THICKNESS, INTERSECTION.limit.y + WALL_THICKNESS)
ROOM_TWO_HEIGHT = 3.00
ROOM_TWO_WIDTH = 3.25
ROOM_TWO_STRUCTURE_NAME = "ROOM_TWO"

ROOM_TWO = Structure(origin=ROOM_TWO_ORIGIN, height=ROOM_TWO_HEIGHT, width=ROOM_TWO_WIDTH, name=ROOM_TWO_STRUCTURE_NAME)

# --------------------------------------- $

LAUNDRY_ORIGIN = Point(KITCHEN.limit.x + WALL_THICKNESS, KITCHEN.origin.y + WALL_THICKNESS)
LAUNDRY_HEIGHT = 3
LAUNDRY_WIDTH = 4
LAUNDRY_STRUCTURE_NAME = "LAUNDRY"

LAUNDRY = Structure(origin=LAUNDRY_ORIGIN, height=LAUNDRY_HEIGHT, width=LAUNDRY_WIDTH, name=LAUNDRY_STRUCTURE_NAME)

# --------------------------------------- $

BACK_HALL_ORIGIN = Point(KITCHEN.limit.x, KITCHEN.limit.y + WALL_THICKNESS)
BACK_HALL_HEIGHT = 1.3
BACK_HALL_WIDTH = 7
BACK_HALL_STRUCTURE_NAME = "BACK_HALL"

BACK_HALL = Structure(origin=BACK_HALL_ORIGIN, height=BACK_HALL_HEIGHT, width=BACK_HALL_WIDTH, name=BACK_HALL_STRUCTURE_NAME)

#####################################################################################

SQUARES = []

def create_squares(placas = []):
    x_positions = [SQUARE_LEFT, SQUARE_CENTER_X, SQUARE_RIGHT]
    y_positions = [SQUARE_BOTTOM, SQUARE_CENTER_Y, SQUARE_TOP]

    current_x = WALL[0]

    rectangles = []

    for x_size in x_positions:
        current_y = WALL[1]
    
        for y_size in y_positions:
            p1 = np.array([current_x, current_y])
            p2 = np.array([current_x + x_size, current_y + y_size])

            rectangles.append((p1, p2))

            current_y += y_size
        current_x += x_size

    for i, (p1, p2) in enumerate(rectangles, start=1):
        SQUARES.append(Structure.from_origin_limit(
                                                    origin=Point(p1[0], p1[1]),
                                                    limit=Point(p2[0], p2[1]),
                                                    name=f"Square {i}"
                                                 )
        )

    print()
    for placa in SQUARES:
        print(str(placa))
    print()

def get_total_area():
    kari_area = sum(s.get_area() for s in KARI)
    emilio_area = sum(s.get_area() for s in EMILIO)

    # ---- #
    outer_area = BORDER[0] * BORDER[1]
    inner_width  = BORDER[0] - 2 * WALL[0]
    inner_height = BORDER[1] - 2 * WALL[1]
    inner_area = inner_width * inner_height
    # ---- #

    border_area = outer_area - inner_area
    used_total =  round(
                        kari_area + 
                        emilio_area
    )
    
    unused_total = TOTAL_AREA - used_total
    error_area = TOTAL_AREA - (used_total+border_area)
    
    print("\n" + "="*50)
    print(f"{'TOTAL AREA':<20} : {TOTAL_AREA:>6.2f}")
    print(f"{'KARI TOTAL AREA':<20} : {kari_area:>6.0f}")
    print(f"{'EMILIO TOTAL AREA':<20} : {emilio_area:>6.0f}")
    print(f"{'USED TOTAL':<20} : {used_total:>6.2f}")
    print("-"*50)
    print(f"{'UNUSED TOTAL':<20} : {unused_total:>6.2f}")
    print(f"{'BORDER TOTAL AREA':<20} : {border_area:>6.2f}")
    print(f"{'MARGIN OF ERROR':<20} : {error_area:>6.2f}")
    print("="*50)

def print_coordinates():
    print(str(LEFT_HALL))
    print(str(PATIO))
    print(str(RIGHT_HALL))
    print(str(LIVING_ROOM))
    print(str(INTERSECTION))
    print(str(DINING_ROOM))
    print(str(KITCHEN))
    print(str(BATHROOM))
    print(str(ROOM_ONE))
    print(str(ROOM_TWO))
    print(str(BACK_HALL))
    print(str(LAUNDRY))

############################### MAIN ################################

print("\n"*1000)

print("HOUSE DIMENSIONS -------------- ALL MEASUREMENTS IN METERS")

create_squares()

KARI = [
        
        SQUARES[3],
        SQUARES[4],
        SQUARES[5],
        SQUARES[6],
        SQUARES[7],
        SQUARES[8],
        ROOM_TWO,
        KITCHEN,
        DINING_ROOM,
        RIGHT_HALL,
        LAUNDRY
    ]

EMILIO = [

        SQUARES[0],
        SQUARES[1],
        SQUARES[2],
        ROOM_ONE,
        LIVING_ROOM,
        BATHROOM,
        INTERSECTION,
        PATIO,
        LEFT_HALL,
        BACK_HALL
    ]

print_coordinates()
get_total_area()

print("\n"*3)