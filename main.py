import sys
import cadwork
import element_controller as ec


sys.path.append("C:\\Users\\MichaelBrunner\\cwapi3d-cutwithplane\\pythonProject\\.venv\\Lib\\site-packages")
from cwmath.cwplane3d import CwPlane3d
from cwmath.cwvector3d import CwVector3d

if __name__ == '__main__':
    element_ids = ec.get_user_element_ids()
    plane_normal = CwVector3d(0.000000, -0.500000, 0.866025)
    plane = CwPlane3d(CwVector3d(-42.500000, 1644.450845, 3432.000000),
                      plane_normal)
    distance = plane.distance_to_point(CwVector3d(0.0, 0.0, 0.0))
    for element_id in element_ids:
        print(ec.cut_element_with_plane(element_id,
                                        cadwork.point_3d(*plane_normal),
                                        distance))

