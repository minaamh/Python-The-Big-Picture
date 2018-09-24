>>> bpy.data.objects
<bpy_collection[3], BlendDataObjects>

>>> list(bpy.data.objects)
[bpy.data.objects['Camera'], bpy.data.objects['Cube'], bpy.data.objects['Lamp']]

>>> cube = bpy.data.objects['Cube']
>>> cube.location
Vector((0.0, 0.0, 0.0))

>>> cube.location
Vector((2.3387231826782227, 1.6995861530303955, 1.3083970546722412))

>>> import mathutils
>>> cube.location += mathutils.Vector((1,1,1))