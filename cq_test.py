import cadquery as cq


def generate_stl(user_data_name, user_data_geolocation):

        # Step 1: Create a basic rectangular name tag using CadQuery
        width = max(len(user_data_name), len(user_data_geolocation))
        model = cq.Workplane("XY").box(width*6, 50, 2)
        text_name = cq.Workplane("XY", origin=(0, 10, 1)).text(user_data_name, 8, 0.2, font="Courier")
        text_geolocation = cq.Workplane("XY", origin=(0, -10, 1)).text(user_data_geolocation, 8, 0.2, font="Courier")
        
        model = model.union(text_name)
        model = model.union(text_geolocation)

        return model
    
geolocation = "Grimstad"
name = "Billy Bob Johansen"

result = generate_stl(name, geolocation)