# platonic
Determines parameters associated with platonic solids, along with a plotting option.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to Use](#how-to-use)

## General Info
If given the number of desired faces and edge length, will determine these parameters:
* name: (str) The name of the solid.
* schlafli_symbol: (tuple(int)) The Schlafli symbol for the solid (p, q).
* p: (int) The first Schlafli symbol (# of edges of each face).
* q: (int) The second Schlafli symbol (# of faces that meet at each vertex).
* coxeter_number: (int) The Coxeter number of the solid.
* dihedral_angle: (float) The interior angle between any two face planes.
* defect: (float) The angular defect at each vertex.
* solid_angle: (float) The solid angle at each vertex.
* circum_radius: (float) The radius of the sphere that passes through all the vertices.
* in_radius: (float) The radius of the sphere that is tangent to each face at the center of the face.
* mid_radius: (float) The radius of the sphere that is tangent to each edge at the midpoint of the edge.
* surface_area: (float) The surface area of the platonic solid.
* volume: (float) The volume of the platonic solid.
* vertices: (tuple(float)) The vertices associated with the platonic solid.

## Technologies
Project was created with:
* Python 3.6

## How to Use
Just import platonic and type platonic.PlatonicSolid(). This will determine all parameters. Add .plot() to generate a 3D scatter plot of the vertices.  
Here are the arguments to PlatonicSolid:
* faces: (int) The number of desired faces for the solid can only be 4, 6, 8, 12, or 20 (default is 4).
* edge_length: (float) The desired edge length for the solid (default is 1).
