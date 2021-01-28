from svgpathtools import svg2paths, wsvg
import os

if __name__ == "__main__":
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(ROOT_DIR)

    path = os.path.join(ROOT_DIR, "examples/owl", "owl-svgrepo-com.svg")
    paths, attributes = svg2paths(path)

    # Update: You can now also extract the svg-attributes by setting
    # return_svg_attributes=True, or with the convenience function svg2paths2
    #paths, attributes, svg_attributes = svg2paths2(path)

    # Let's print out the first path object and the color it was in the SVG
    # We'll see it is composed of two CubicBezier objects and, in the SVG file it
    # came from, it was red
    redpath = paths[0]
    redpath_attribs = attributes[0]
    print(redpath)
    print(redpath_attribs)
