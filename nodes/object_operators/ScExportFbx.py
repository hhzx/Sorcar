import bpy
import os

from bpy.props import StringProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScObjectOperatorNode

class ScExportFbx(Node, ScObjectOperatorNode):
    bl_idname = "ScExportFbx"
    bl_label = "Export FBX"

    in_file: StringProperty(subtype='DIR_PATH', update=ScNode.update_value)
    in_filename: StringProperty(default="untitled")

    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketString", "File").init("in_file", True)
        self.inputs.new("ScNodeSocketString", "File Name").init("in_filename", True)
    
    def error_condition(self):
        return (
            super().error_condition()
            or self.inputs["File"].default_value == ""
            or self.inputs["File Name"].default_value == ""
        )
    
    def functionality(self):
        bpy.ops.export_scene.fbx(
            filepath = os.path.join(
                bpy.path.abspath(self.inputs["File"].default_value),
                self.inputs["File Name"].default_value+".fbx"
            ),
            use_selection = True,
            use_tspace = True
        )