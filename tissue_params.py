import math


class Params:
    SLIDE_CLIP_OFFSET = 22
    SLIDE_LENGTH = 75
    TOTAL_LENGTH = 105
    OFFSET_ANGLE = 30
    phi_angle_radian = None
    theta_angle_radian = None
    phi_angle_with_offset = None
    theta_angle_with_offset = None
    final_position_y = None
    final_position_x = None
    position_after_pivot_y = None
    position_after_pivot_x = None
    THETA_ANGLE = None
    PHI_ANGLE = None
    PICKUP_POSITION_X = None
    PICKUP_POSITION_Y = None

    def __init__(self):
        self.set_defaults()
        self.update_positions()

    def get_theta_angle(self):
        print("Theta: " + str(self.THETA_ANGLE) + "\n")
        return self.THETA_ANGLE

    def set_theta_angle(self, theta):
        self.THETA_ANGLE = theta
        print("Theta set to: " + str(self.THETA_ANGLE) + "\n")

    def get_phi_angle(self):
        print("Phi: " + str(self.PHI_ANGLE) + "\n")
        return self.PHI_ANGLE

    def set_phi_angle(self, phi):
        self.PHI_ANGLE = phi
        print("Phi set to: " + str(self.PHI_ANGLE) + "\n")

    def get_slide_pickup_position(self):
        print("PICKUP_POSITION_X: " + str(self.PICKUP_POSITION_X) + "\n")
        print("PICKUP_POSITION_Y: " + str(self.PICKUP_POSITION_Y) + "\n")

    def set_slide_pickup_position(self, x_abs, y_abs):
        self.PICKUP_POSITION_X = x_abs
        self.PICKUP_POSITION_Y = y_abs

    def update_positions(self):
        self.theta_angle_with_offset = self.THETA_ANGLE #+ self.OFFSET_ANGLE
        self.phi_angle_with_offset = self.PHI_ANGLE  #+ self.OFFSET_ANGLE
        self.theta_angle_radian = math.radians(self.theta_angle_with_offset)
        self.phi_angle_radian = math.radians(self.phi_angle_with_offset)
        self.position_after_pivot_x = self.PICKUP_POSITION_X + (self.TOTAL_LENGTH * (math.cos(self.theta_angle_radian) - math.cos(self.phi_angle_radian)))
        self.position_after_pivot_y = self.PICKUP_POSITION_Y - (self.TOTAL_LENGTH * (math.sin(self.phi_angle_radian) - math.sin(self.theta_angle_radian)))
        self.final_position_x = self.position_after_pivot_x - 20 * math.cos(self.phi_angle_radian)
        self.final_position_y = self.position_after_pivot_y - 20 * math.sin(self.phi_angle_radian)

    def current_default_positions(self):
        self.update_positions()
        print("Slide_theta: " + str(self.THETA_ANGLE) + "\n")
        print("Slide_phi: " + str(self.PHI_ANGLE) + "\n")
        print("Slide_pickup_position_x: " + str(self.PICKUP_POSITION_X) + "\n")
        print("Slide_pickup_position_y: " + str(self.PICKUP_POSITION_Y) + "\n")
        print("position_after_pivot_x: " + str(self.position_after_pivot_x) + "\n")
        print("slide_position_after_pivot_Y: " + str(self.position_after_pivot_y) + "\n")
        print("final_position_x: " + str(self.final_position_x) + "\n")
        print("final_position_y: " + str(self.final_position_y) + "\n")

    def set_defaults(self):
        self.THETA_ANGLE = 30
        self.PHI_ANGLE = 40
        self.PICKUP_POSITION_X = 30
        self.PICKUP_POSITION_Y = 40
        self.update_positions()
