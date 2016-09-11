from skimage import data, color, feature
from skimage.viewer import ImageViewer

camera = data.camera()
camera_gray = color.rgb2gray(camera)
harris = feature.corner_harris(camera_gray)
viewer = ImageViewer(harris)
viewer.show()
