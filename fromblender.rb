toolbar = UI::Toolbar.new"b2s"
cmd = UI::Command.new('从blender导入'){
model = Sketchup.active_model

options = { :units => "model",
            :merge_coplanar_faces => true,
            :show_summary => true }
status = model.import("blendsu/fromblender.glb", options)
}
menu = UI.menu('extensions')
menu.add_item(cmd)

 cmd.small_icon = "fromblender.ico"
 cmd.large_icon = "fromblender.ico"
 toolbar.add_item cmd
 toolbar.show