from msg_class import UserData
import cadquery as cq
import os
os.environ['FONTCONFIG_PATH'] = '/etc/fonts/'



class STLGenerator:
    def generate_stl(self, user_data):
        print(f"Generating STL file for {user_data.name} based at {user_data.geolocation}")

        # Step 1: Create a basic rectangular name tag using CadQuery
        model = cq.Workplane("XY").box(30, 10, 2)

        # Step 2: Add text (User's name and location)
        # Create 3D text geometry for name
        name_text = cq.Workplane("XY").text(user_data.name, 2, -0.2)
        # Create 3D text geometry for location
        location_text = cq.Workplane("XY").transformed(offset=(0, 3)).text(user_data.geolocation, 1, -0.2)

        # Step 3: Combine text with name tag
        # This example cuts the text into the surface of the name tag
        model = model.cut(name_text)
        model = model.cut(location_text)

        # Step 4: Export to STL format
        #model.export(f"{user_data.name}_tag.stl")
        filename = f"{user_data.name}_tag.3mf"
        cq.exporters.export(model,filename, tolerance=0.01, angularTolerance=0.01)

        print(f"STL file generated: {user_data.name}_tag.stl")
