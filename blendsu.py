bl_info = {
    "name": "SketchUp Export/Import",
    "blender": (4, 2, 0),
    "category": "Import-Export",
}

import bpy
from bpy.props import StringProperty, PointerProperty
import os

class SketchUpSettings(bpy.types.PropertyGroup):
    export_path: StringProperty(
        name="Export Path",
        default="//",
        subtype='DIR_PATH'
    )

class ExportToSketchUp(bpy.types.Operator):
    bl_idname = "export.send_to_sketchup"
    bl_label = "发送到 SketchUp"

    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        if not selected_objects:
            self.report({'WARNING'}, "请先选择对象.")
            return {'CANCELLED'}

        export_path = context.preferences.addons[__name__].preferences.export_path
        file_path = os.path.join(export_path, "fromblender.glb")

        # 使用新的 GLTF 导出选项
        bpy.ops.export_scene.gltf(
            filepath=file_path,
            use_selection=True,
            export_format='GLB',
            export_apply=True  # 应用修改器
        )
        
        self.report({'INFO'}, f"导出至 {file_path}")
        return {'FINISHED'}

class ImportFromSketchUp(bpy.types.Operator):
    bl_idname = "import.import_su_to_blender"
    bl_label = "导入 SU 到 Blender"

    def execute(self, context):
        export_path = context.preferences.addons[__name__].preferences.export_path
        file_path = os.path.join(export_path, "toblender.glb")

        if not os.path.exists(file_path):
            self.report({'WARNING'}, "文件不存在!")
            return {'CANCELLED'}

        bpy.ops.import_scene.gltf(filepath=file_path)
        self.report({'INFO'}, f"导入自 {file_path}")
        return {'FINISHED'}

class SketchUpPanel(bpy.types.Panel):
    bl_label = "SketchUp 导入导出"
    bl_idname = "PANEL_PT_sketchup"
    bl_space_type = 'VIEW_3D'  
    bl_region_type = 'UI'       
    bl_category = 'SketchUp'    

    def draw(self, context):
        layout = self.layout
        layout.operator("export.send_to_sketchup")
        layout.operator("import.import_su_to_blender")

class SketchUpSettingsPanel(bpy.types.AddonPreferences):
    bl_idname = __name__

    export_path: StringProperty(
        name="Export Path",
        default="//",
        subtype='DIR_PATH'
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "export_path", text="Export Path")

def register():
    bpy.utils.register_class(SketchUpSettings)
    bpy.types.Preferences.sketchup_settings = PointerProperty(type=SketchUpSettings)

    bpy.utils.register_class(ExportToSketchUp)
    bpy.utils.register_class(ImportFromSketchUp)
    bpy.utils.register_class(SketchUpPanel)
    bpy.utils.register_class(SketchUpSettingsPanel)

def unregister():
    bpy.utils.unregister_class(SketchUpSettingsPanel)
    bpy.utils.unregister_class(SketchUpPanel)
    bpy.utils.unregister_class(ImportFromSketchUp)
    bpy.utils.unregister_class(ExportToSketchUp)
    del bpy.types.Preferences.sketchup_settings
    bpy.utils.unregister_class(SketchUpSettings)

if __name__ == "__main__":
    register()
