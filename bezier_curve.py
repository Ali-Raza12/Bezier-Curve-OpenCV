import cv2
import numpy as np


class BezierCurve:
    @staticmethod
    def draw_curve(image_raw, control_points: list, interpolation: int, color: tuple = (0, 0, 255), thickness: int = 3):
        coeff_lst = BezierCurve.calculate_coefficients(interpolation)
        calc_points = BezierCurve.calculate_points(control_points, coeff_lst)
        cv2.polylines(image_raw, [calc_points], False, color, thickness)
        return image_raw

    @staticmethod
    def calculate_coefficients(n_points: int):
        t = np.linspace(0, 1, n_points)
        u = 1 - t
        coeff_0 = u**3
        coeff_1 = 3*t*u**2
        coeff_2 = 3*t**2*u
        coeff_3 = t**3
        return [coeff_0, coeff_1, coeff_2, coeff_3]

    @staticmethod
    def calculate_points(ctrl_pts: list, coeffs: list):
        x = coeffs[0]*ctrl_pts[0][0] + coeffs[1]*ctrl_pts[1][0] + \
            coeffs[2]*ctrl_pts[2][0] + coeffs[3]*ctrl_pts[3][0]
        y = coeffs[0]*ctrl_pts[0][1] + coeffs[1]*ctrl_pts[1][1] + \
            coeffs[2]*ctrl_pts[2][1] + coeffs[3]*ctrl_pts[3][1]
        x = x.reshape((-1, 1))
        y = y.reshape((-1, 1))
        points = np.hstack((x, y)).astype(np.int32)
        return points
