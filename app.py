import os

from flask import Flask, request, render_template, send_file
from nameTagLib.msg_class import UserData
from nameTagLib.model_generator import STLGenerator
from nameTagLib.user_input import UserInputDataClass
from nameTagLib.geo_location import GeoLocationAPI_Class

app = Flask(__name__)

# Initialize the classes
user_data = UserData()
user_input = UserInputDataClass()
geo_location = GeoLocationAPI_Class("https://ipgeolocation.abstractapi.com/v1/?api_key=6c96de49e97f467b8cc6a446e5c4bdf1")  # Replace with your actual API key
stl_generator = STLGenerator()


# Route for the form
@app.route('/')
def form():
    return render_template('form.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['user_name']
    isInputValid = user_input.validate_data(name)

    if isInputValid:
        user_data.name = name
        location = geo_location.get_data()  # This should be modified if you need to pass specific data to get_data()
        isLocationValid = geo_location.validate_data(location)

        if isLocationValid:
            user_data.geolocation = location
            stl_file_path = stl_generator.generate_stl(
                user_data)  # This should return the path to the generated STL file

            # Pass the user's name and location to the download template
            return render_template('download.html', user_name=name, user_location=location, stl_file_path=stl_file_path)

    # If input is not valid, you can redirect to the form again or show an error message
    return "Invalid input", 400


# Route to download the STL file
@app.route('/download')
def download():
    stl_file_path = "./name_tag.3mf"#request.args.get('name_tag.3mf')
    if stl_file_path and os.path.exists(stl_file_path):
        return send_file(stl_file_path, as_attachment=True, mimetype='application/octet-stream')
    else:
        return "File not found", 404



if __name__ == '__main__':
    app.run(debug=True)
