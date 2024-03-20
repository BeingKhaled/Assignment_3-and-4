from flask import Flask, render_template, request, redirect, url_for
from forms import DataCollectionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information')
def information():
    return render_template('information.html')

# Route for data collection form
@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()  # Creating an instance of the form
    if form.is_submitted():  # Checking if the form is submitted
        # Here you can handle form submission and data storage
        with open('../Assignment_3_and_4/input.txt', 'a') as file:  # Opening a file to store form data
            for field_name, field_value in form.data.items():  # Writing form data to the file
                file.write(f"{field_name.capitalize().replace('_', ' ')}: {field_value}\n")
            file.write('\n')  # Adding a new line for the next form submission
    return render_template('data_collection.html', form=form)  # Rendering the data collection form template

if __name__ == '__main__':
    app.run(debug=True)

