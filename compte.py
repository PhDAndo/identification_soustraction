import cv2
import numpy as np
import common

color_infos = (0, 0, 255)
xmin = 90
xmax = 510
ymin = 315
ymax = 360
video = 'autoroute.mp4'

nbr_old = 0
vehicule = 0
seuil = 10

fond = common.moyenne_image(video, 500)
fond = fond[ymin:ymax]