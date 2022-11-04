import bpy
import bmesh


def symmetrize_vertices(self, context):
    obj = context.object 
    
    mesh = obj.data
    bm = bmesh.from_edit_mesh(mesh)
    selected_verts = [v for v in bm.verts if v.select]

    active_vert = None
    for elem in reversed(bm.select_history):
        if isinstance(elem, bmesh.types.BMVert):
            active_vert = elem
            break

    for vert in selected_verts:
        if vert is not active_vert:
            vert.co = active_vert.co.copy()
            if self.x_symmetry:
                vert.co.x = -vert.co.x
            if self.y_symmetry:
                vert.co.y = -vert.co.y
            if self.z_symmetry:
                vert.co.z = -vert.co.z    
    bmesh.update_edit_mesh(obj.data)
    

class SYMMETRIZER_OT_symmetrize(bpy.types.Operator):
    bl_idname = "vertex_symmetrizer.symmetrize"
    bl_label = "Symmetrize"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'REGISTER', 'UNDO'}

    x_symmetry: bpy.props.BoolProperty(default=True)
    y_symmetry: bpy.props.BoolProperty(default=False)
    z_symmetry: bpy.props.BoolProperty(default=False)

    def invoke(self, context, event):
        return self.execute(context)

    def execute(self, context):
        symmetrize_vertices(self, context)
        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        row = layout.row(align=True)

        row.prop(self, 'x_symmetry', text='X', toggle=True)
        row.prop(self, 'y_symmetry', text='Y', toggle=True)
        row.prop(self, 'z_symmetry', text='Z', toggle=True)
