import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB max limit
ALLOWED_EXTENSIONS = {'csv'}

# Ensure the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file has a valid CSV extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle CSV file uploads, process data, and return top sources and protocols."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
        
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only CSV files are supported.'}), 400

    try:
        # Secure the filename even if we read it in memory (good practice if saved later)
        _ = secure_filename(file.filename)
        
        # Performance optimization: read stream directly without TextIOWrapper 
        # and only pull the required columns to save memory
        df = pd.read_csv(file.stream, usecols=['Source', 'Protocol'])
        
        # Efficiently calculate value counts
        top_sources = df['Source'].value_counts().head(5)
        top_protocols = df['Protocol'].value_counts().head(5)
        
        return jsonify({
            'top_sources': {
                'labels': top_sources.index.tolist(),
                'counts': top_sources.values.tolist()
            },
            'top_protocols': {
                'labels': top_protocols.index.tolist(),
                'counts': top_protocols.values.tolist()
            }
        })

    except ValueError as ve:
        # Specifically catches missing columns from 'usecols' parameter
        return jsonify({'error': "CSV must contain both 'Source' and 'Protocol' columns."}), 400
    except Exception as e:
        return jsonify({'error': f"Error processing file: {str(e)}"}), 500

if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=5000, debug=True)
