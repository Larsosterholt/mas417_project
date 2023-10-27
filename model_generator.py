from msg_class import UserData
import cadquery as cq
import os
os.environ['FONTCONFIG_PATH'] = '/etc/fonts/'



class STLGenerator:
    def generate_stl(self, user_data):
        print(f"Generating STL file for {user_data.name} based at {user_data.geolocation}")
        width = max(len(user_data.name), len(user_data.geolocation))
        model = cq.Workplane("XY").box(width * 6, 50, 5)
        text_name = cq.Workplane("XY", origin=(0, 10, 2.5)).text(user_data.name, 8, 0.2, font="Courier")
        text_geolocation = cq.Workplane("XY", origin=(0, -10, 2.5)).text(user_data.geolocation, 8, 0.2, font="Courier")

        model = model.union(text_name)
        model = model.union(text_geolocation)

        filename = f"{user_data.name}_tag.3mf"
        cq.exporters.export(model,filename, tolerance=0.01, angularTolerance=0.01)

        print(f"STL file generated: {user_data.name}_tag.stl")
