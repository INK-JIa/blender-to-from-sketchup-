toolbar = UI::Toolbar.new"b2s"
cmd = UI::Command.new('导出到blender'){
model = Sketchup.active_model
show_summary = true
status = model.export('blendsu/toblender.glb',show_summary)
}
 menu = UI.menu('extensions')
 menu.add_item(cmd)
 
 cmd.small_icon = "toblender.ico"
 cmd.large_icon = "toblender.ico"
 toolbar.add_item cmd
 toolbar.show