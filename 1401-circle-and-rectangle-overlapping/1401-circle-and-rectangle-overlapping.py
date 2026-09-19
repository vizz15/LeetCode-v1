class Solution:

  def checkOverlap(
      self,
      radius: int,
      xCenter: int,
      yCenter: int,
      x1: int,
      y1: int,
      x2: int,
      y2: int,
  ) -> bool:
    # Find the closest x and y coordinates on the rectangle to the circle center
    closest_x = max(x1, min(x2, xCenter))
    closest_y = max(y1, min(y2, yCenter))

    # Calculate the distance squared from the circle center to this closest point
    dist_x = xCenter - closest_x
    dist_y = yCenter - closest_y

    # Compare squared distance with squared radius to avoid square root inaccuracy
    return (dist_x**2 + dist_y**2) <= (radius**2)
