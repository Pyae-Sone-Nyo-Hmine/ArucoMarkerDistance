import numpy as np


class Marker:

    def __init__(self, corners, ids):
        self.corners = corners
        self.ids = ids

        if len(corners) != 0:

            # calculate the average length using distance formula
            l_1 = np.sqrt(pow(abs(self.corners[0][0][0][0] - self.corners[0][0][1][0]), 2) + pow(
                abs(self.corners[0][0][0][1] - self.corners[0][0][1][1]), 2))

            l_2 = np.sqrt(pow(abs(self.corners[0][0][1][0] - self.corners[0][0][2][0]), 2) + pow(
                abs(self.corners[0][0][1][1] - self.corners[0][0][2][1]), 2))

            l_3 = np.sqrt(pow(abs(self.corners[0][0][2][0] - self.corners[0][0][3][0]), 2) + pow(
                abs(self.corners[0][0][2][1] - self.corners[0][0][3][1]), 2))

            l_4 = np.sqrt(pow(abs(self.corners[0][0][3][0] - self.corners[0][0][0][0]), 2) + pow(
                abs(self.corners[0][0][3][1] - self.corners[0][0][0][1]), 2))

            average_length = (l_1 + l_2 + l_3 + l_4) * 0.25

            self.average_length = average_length

            # calculate the center of the aruco marker
            x_sum = self.corners[0][0][0][0] + self.corners[0][0][1][0] + self.corners[0][0][2][0] + \
                    self.corners[0][0][3][
                        0]

            y_sum = self.corners[0][0][0][1] + self.corners[0][0][1][1] + self.corners[0][0][2][1] + \
                    self.corners[0][0][3][
                        1]

            x_centroid = x_sum * 0.25
            y_centroid = y_sum * 0.25

            self.centroid = x_centroid, y_centroid

        else:
            self.average_length = 0
            self.centroid = 0,0
