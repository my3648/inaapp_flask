from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('0a_homepage.html')

@app.route('/index')
def index():
    return render_template('0b_index.html')

@app.route('/analytics')
def analytics():
    return render_template('d00_00_analytics.html')

# @app.route('/d00_a01_gpsroute', methods=['POST'])
# def d00_a01_gpsroute():    
#     result = request.form['requestedFiles']
#     print(result)
#     fileoption = {
#         'requestedFiles': result
#     }
#     return render_template('d00_a01_gpsroute.html', fileoption=fileoption)

# @app.route('/d00_a02_fho')
# def d00_a02_fho():
#     return render_template('d00_a02_fho.html')

# @app.route('/d00_b01_epm')
# def d00_b01_epm():
#     return render_template('d00_b01_epm.html')

# @app.route('/d00_b02_lambdaadap')
# def d00_b02_lambdaadap():
#     return render_template('d00_b02_lambdaadap.html')

# @app.route('/d00_b03_vvladap')
# def d00_b03_vvladap():
#     return render_template('d00_b03_vvladap.html')

# @app.route('/d00_b07_iumpr')
# def d00_b07_iumpr():
#     return render_template('d00_b07_iumpr.html')

# for testing
# @app.route('/d00_b07_iumpr_data')
# def d00_b07_iumpr_data():
#     jsdata = {}
#     with open('d00_b07_iumpr.json', 'r') as f:
#         jsdata = json.load(f)
#         f.close()
#     return jsonify({'plotdata': jsdata})

if __name__=="__main__":
    app.run(debug=True)

