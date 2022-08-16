from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__)
Filename = 'modelroi.pkl'
with open(Filename, 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def index_page():
    print(model)
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict_logic():
    if request.method == 'POST':
        lenderyield = float(request.form.get('lenderyield'))
        borrowerapr = float(request.form.get('borrowerapr'))
        estimatedreturn = float(request.form.get('estimatedreturn'))
        loancurrentdaysdelinquent = float(request.form.get('loancurrentdaysdelinquent'))
        investors = float(request.form.get('investors'))

    pred_name = model.predict([[lenderyield, borrowerapr, estimatedreturn, loancurrentdaysdelinquent,
                                investors]]).tolist()[0]

    return render_template('index.html', pred_name=pred_name)


if __name__ == "__main__":
    app.run(debug=True)