import cadquery as cq

class modelGenerator:
    def generate_3mf(self, user_data):
        print(f"Generating .3mf file for {user_data.name} based at {user_data.geolocation}")

        # Defining width of the name tag based on the number of characters in the name/city
        width = max(len(user_data.name), len(user_data.geolocation))

        # Create model and text
        model = cq.Workplane("XY").box(width * 6, 50, 2)
        text_name = cq.Workplane("XY", origin=(0, 10, 1)).text(user_data.name, 12, 0.8, font="impact")
        text_geolocation = cq.Workplane("XY", origin=(0, -10, 1)).text(user_data.geolocation, 12, 0.8, font="impact")

        # Make the model and text union
        model = model.union(text_name)
        model = model.union(text_geolocation)

        # Export to file
        filename = "./name_tag.3mf"
        cq.exporters.export(model, filename)

        print(f"3mf file generated: name_tag.3mf")
