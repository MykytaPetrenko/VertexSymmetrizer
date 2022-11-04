import bpy
from .operator import SYMMETRIZER_OT_symmetrize


class VIEW3D_PT_Symmetrize(bpy.types.Panel):
    """
    Addon main menu (N-Panel)
    """
    bl_label = "Vertex Symmetrizer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FSeaL'
    bl_context = 'mesh_edit'       

    def draw(self, context):                 
        layout = self.layout
        row = layout.row()
        props = row.operator(SYMMETRIZER_OT_symmetrize.bl_idname, text='X')
        props.x_symmetry, props.y_symmetry, props.z_symmetry = True, False, False
        props = row.operator(SYMMETRIZER_OT_symmetrize.bl_idname, text='Y')
        props.x_symmetry, props.y_symmetry, props.z_symmetry = False, True, False
        props = row.operator(SYMMETRIZER_OT_symmetrize.bl_idname, text='Z')
        props.x_symmetry, props.y_symmetry, props.z_symmetry = False, False, True

        row = layout.row()
        props = row.operator(SYMMETRIZER_OT_symmetrize.bl_idname, text='XY')
        props.x_symmetry, props.y_symmetry, props.z_symmetry = True, True, False
        props = row.operator(SYMMETRIZER_OT_symmetrize.bl_idname, text='XZ')
        props.x_symmetry, props.y_symmetry, props.z_symmetry = True, False, True
        props = row.operator(SYMMETRIZER_OT_symmetrize.bl_idname, text='YZ')
        props.x_symmetry, props.y_symmetry, props.z_symmetry = False, True, True

        row = layout.row()
        props = row.operator(SYMMETRIZER_OT_symmetrize.bl_idname, text='O')
        props.x_symmetry, props.y_symmetry, props.z_symmetry = True, True, True
