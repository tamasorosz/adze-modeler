import pygmsh.geo as gmsh


def node_gmsh_point_distance(node, point):
    dx = node.x - point.x[0]
    dy = node.y - point.x[1]

    return (dx ** 2.0 + dy ** 2.0) ** 0.5


def gmsh_writer(nodes, lines, arcs, cubic_beziers):
    lcar = 5.0
    epsilon = 1e-6
    with gmsh.Geometry() as geom:
        # add nodes
        points = []
        for node in nodes:
            temp = geom.add_point([node.x, node.y], lcar)
            # temp._id = node.id
            points.append(temp)

        # add lines
        glines = []
        for line in lines:
            for i in range(len(points)):
                if node_gmsh_point_distance(line.start_pt, points[i]) < epsilon:
                    start_pt = points[i]

                if node_gmsh_point_distance(line.end_pt, points[i]) < epsilon:
                    end_pt = points[i]

            temp = geom.add_line(p0=start_pt, p1=end_pt)
            glines.append(temp)

        # add cubic beziers
        gbeziers = []
        for cb in cubic_beziers:
            for i in range(len(points)):
                if node_gmsh_point_distance(cb.start_pt, points[i]) < epsilon:
                    start_pt = points[i]
                if node_gmsh_point_distance(cb.end_pt, points[i]) < epsilon:
                    end_pt = points[i]
                if node_gmsh_point_distance(cb.control1, points[i]) < epsilon:
                    control1 = points[i]
                if node_gmsh_point_distance(cb.control2, points[i]) < epsilon:
                    control2 = points[i]

            temp = geom.add_bspline([start_pt, control1, control2, end_pt])
            gbeziers.append(temp)
        # ll = geom.add_curve_loop(glines)
        # pl = geom.add_plane_surface(ll)

        geom.save_geometry("test.geo_unrolled")
        # mesh = geom.generate_mesh()
        # mesh.write("test.vtk")
