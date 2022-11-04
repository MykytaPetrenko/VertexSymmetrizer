import bpy
from .panel import VIEW3D_PT_Symmetrize
from .operator import SYMMETRIZER_OT_symmetrize


bl_info = {
    "name" : "Vertex Symmetrizer",
    "author" : "Mykyta Petrenko (FSeal)",
    "description" : "Simple addon that copies the position of the active vertex to the selected with invertion of the chosen axis.",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 0),
    "location" : "View3D -> Mesh Edit Mode -> N-Panel -> FSeaL -> Vertex Symmetrizer",
    "warning" : "",
    "category" : "Mesh"
}

CLASSES = [
    SYMMETRIZER_OT_symmetrize,
    VIEW3D_PT_Symmetrize
]

def register():
    for c in CLASSES:
        bpy.utils.register_class(c)  


def unregister():
    for c in CLASSES:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
