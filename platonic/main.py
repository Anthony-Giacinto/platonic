"""
Contains the PlatonicSolids class.

Classes:
    PlatonicSolids: Finds many parameters associated with the given platonic solid, with the option of plotting it.
"""


import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


class PlatonicSolid:
    """ Finds many parameters associated with the given platonic solid, with the option of plotting it.

    Class Attributes:
        name_dict: (dict) Dictionary of platonic solid names based off of the number of faces.
        schlafli_dict: (dict) Dictionary of Schlafli Symbols based off of the number of faces.
        coxeter_dict: (dict) Dictionary of Coxeter numbers based off of the number of faces.

    Instance Attributes:
        faces: (int) The number of desired faces for the solid can only be 4, 6, 8, 12, or 20 (default is 4).
        edge_length: (float) The desired edge length for the solid (default is 1).
        plot: (bool) If True, will automatically plot the solid (default is True).
        name: (str) The name of the solid.
        schlafli_symbol: (tuple(int)) The Schlafli symbol for the solid (p, q).
        p: (int) The first Schlafli symbol (# of edges of each face).
        q: (int) The second Schlafli symbol (# of faces that meet at each vertex).
        coxeter_number: (int) The Coxeter number of the solid.
        dihedral_angle: (float) The interior angle between any two face planes.
        defect: (float) The angular defect at each vertex.
        solid_angle: (float) The solid angle at each vertex.
        circum_radius: (float) The radius of the sphere that passes through all the vertices.
        in_radius: (float) The radius of the sphere that is tangent to each face at the center of the face.
        mid_radius: (float) The radius of the sphere that is tangent to each edge at the midpoint of the edge.
        surface_area: (float) The surface area of the platonic solid.
        volume: (float) The volume of the platonic solid.
        vertices: (tuple(float)) The vertices associated with the platonic solid.

    Functions:
        plot: Creates a 3D scatter plot of the platonic solid.
    """

    name_dict = {4: 'Tetrahedron', 6: 'Cube', 8: 'Octahedron', 12: 'Dodecahedron', 20: 'Icosahedron'}
    schlafli_dict = {4: (3, 3), 6: (4, 3), 8: (3, 4), 12: (5, 3), 20: (3, 5)}
    coxeter_dict = {4: 4, 6: 6, 8: 6, 12: 10, 20: 10}

    def __init__(self, faces=4, edge_length=1, plot=True):
        """
        :param faces: (int) The number of desired faces for the solid can only be 4, 6, 8, 12, or 20 (default is 4).
        :param edge_length: (float) The desired edge length for the solid (default is 1).
        :param plot: (bool) If True, will automatically plot the solid (default is True).
        """

        self._faces = faces
        self.edge_length = edge_length
        if plot: self.plot()

    @property
    def faces(self):
        if self._faces not in list(self.name_dict.keys()):
            raise Exception('faces must be 4, 6, 8, 12, or 20')
        else:
            return self._faces

    @property
    def name(self):
        return self.name_dict[self.faces]

    @property
    def schlafli_symbol(self):
        return self.schlafli_dict[self.faces]

    @property
    def p(self):
        return self.schlafli_symbol[0]

    @property
    def q(self):
        return self.schlafli_symbol[1]

    @property
    def coxeter_number(self):
        return self.coxeter_dict[self.faces]

    @property
    def dihedral_angle(self):
        return 2*math.asin((math.cos(math.pi/self.q)/math.sin(math.pi/self.p)))

    @property
    def defect(self):
        return 2*math.pi - math.pi*self.q*(1 - 2/self.p)

    @property
    def solid_angle(self):
        return self.q*self.dihedral_angle - math.pi*(self.q - 2)

    @property
    def circum_radius(self):
        return (self.edge_length/2)*math.tan(self.dihedral_angle/2)*math.tan(math.pi/self.q)

    @property
    def in_radius(self):
        return (self.edge_length/2)*(math.tan(self.dihedral_angle/2)/math.tan(math.pi/self.p))

    @property
    def mid_radius(self):
        return (self.edge_length/2)*(math.cos(math.pi/self.p)/math.sin(math.pi/self.coxeter_number))

    @property
    def surface_area(self):
        return ((self.edge_length/2)**2)*self.faces*self.p/math.tan(math.pi/self.p)

    @property
    def volume(self):
        return self.in_radius*self.surface_area/3

    @property
    def vertices(self):
        if self.name is 'Tetrahedron':
            return (1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)
        elif self.name is 'Cube':
            return (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1), (-1, -1, -1)
        elif self.name is 'Octahedron':
            return (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)
        elif self.name is 'Dodecahedron':
            phi = (1 + 5**0.5)/2
            return (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1), (-1, -1, -1), \
                   (0, 1/phi, phi), (0, -1/phi, -phi), (1/phi, phi, 0), (-1/phi, -phi, 0), (phi, 0, 1/phi), \
                   (-phi, 0, -1/phi), (0, -1/phi, phi), (0, 1/phi, -phi), (-1/phi, phi, 0), (1/phi, -phi, 0), \
                   (-phi, 0, 1/phi), (phi, 0, -1/phi)
        else:
            phi = (1 + 5**0.5)/2
            return (0, 1, phi), (0, -1, -phi), (1, phi, 0), (-1, -phi, 0), (phi, 0, 1), (-phi, 0, -1), \
                   (0, -1, phi), (0, 1, -phi), (-1, phi, 0), (1, -phi, 0), (-phi, 0, 1), (phi, 0, -1)

    def plot(self):
        """ Creates a 3D scatter plot of the platonic solid. """

        x_array = [arr[0] for arr in self.vertices]
        y_array = [arr[1] for arr in self.vertices]
        z_array = [arr[2] for arr in self.vertices]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x_array, y_array, z_array)
        ax.set_title('Platonic Solid:\n' + self.name)
        return plt.show()
