class MapGenerator:
    def __init__(self, level, sx: int, sy: int) -> None:
        self.level = level
        self.sx = sx
        self.sy = sy

    def get_pixel_at(self, x: int, y: int):
        print(x, y)
        if 0 <= x < self.sx and 0 <= y < self.sy:
            return self.level[x + y * self.sy]
        return 0

    def parse(self):
        actors = {"floors": [], "walls": []}
        for x in range(self.sx):
            for y in range(self.sy):
                pixel_value = self.get_pixel_at(x, y)

                if pixel_value == 1:
                    actors["floors"].append((x, y))

                    # Left
                    if self.get_pixel_at(x - 1, y) == 0:
                        actors["walls"].append((x - 0.5, y, 90))

                    # Right
                    if self.get_pixel_at(x + 1, y) == 0:
                        actors["walls"].append((x + 0.5, y, -90))

                    # Up
                    if self.get_pixel_at(x, y - 1) == 0:
                        actors["walls"].append((x, y - 0.5, 180))

                    # Down
                    if self.get_pixel_at(x, y + 1) == 0:
                        actors["walls"].append((x, y + 0.5, 0))

        return actors