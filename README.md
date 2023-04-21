# Bezier-Curve_OpenCV
Draw cubic bezier curves on images using OpenCV in Python

#Usage
Here's the basic code to create a bezier curve on a black background image
`
import numpy as np
import cv2
from bezier_curve import BezierCurve

img = np.zeros((512, 512, 3), np.uint8)

img = BezierCurve.draw_curve(image_raw=img,
                             control_points=[[100, 100], [200, 400], [400, 400], [500, 100]],
                             interpolation=100,
                             color=(0, 255, 0))

cv2.imshow("Bezier Curve", img)
cv2.waitKey(0)
`
