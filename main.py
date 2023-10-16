from flask import Flask, render_template, request, jsonify
import datetime, os

app = Flask(__name__)
print("Working!")

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No image part in the request"
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    
    #---- START SAMPLE CODE ----#
        #-----Description---------
        # the code below has to be changed
        # take the 'file' which is an image and pass in into the trained model
        # the result will be a string i.e. the name of the flower
        # assign the name of the flower to the variable image_name
        #-----Description End-----

    # Saves the file with the current date as the file name
    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.jpg'
    file.save(os.path.join('uploads', filename))
    text = f"Image {filename}.jpg has been saved."
    print(text)
    #---- END SAMPLE CODE ----#

    return render_template('success.html', image_name = filename)
