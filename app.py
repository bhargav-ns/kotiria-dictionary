from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

dictionary_data = {}

@app.route('/')
def index():
    return render_template('index.html', dictionary_data=dictionary_data)

@app.route('/add', methods=['POST'])
def add_word():
    if request.method == 'POST':
        word = request.form['word']
        definition = request.form['definition']
        
        if word and definition:
            dictionary_data[word] = definition
        
        print(word, definition)
        print(dictionary_data)
        
        flash('Word added successfully!')
        return redirect(url_for('index'))
    
@app.route('/delete/<string:word>')
def delete_word(word):
    if word in dictionary_data:
        del dictionary_data[word]
        flash('Word deleted successfully!')
        return redirect(url_for('index'))
    
@app.route('/edit/<string:word>')
def edit_word(word):
    if word in dictionary_data:
        return render_template('edit.html', word=word, definition=dictionary_data[word])
    
@app.route('/update/<string:word>', methods=['POST'])
def update_word(word):
    if request.method == 'POST':
        definition = request.form['definition']
        
        if word and definition:
            dictionary_data[word] = definition
            flash('Word updated successfully!')
            return redirect(url_for('index'))
        

@app.route('/search', methods=['GET'])
def search_word():
    query = request.args.get('query')
    definition = None
    print(query)
    # Search for the word in the dictionary_data
    if query in dictionary_data:
        definition = dictionary_data[query]

    # Return the search results as HTML
    search_results = f'<p><strong>Definition:</strong> {definition}</p>' if definition else '<p>No definition found for this word.</p>'
    print(search_results)
    return search_results
    
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000, use_debugger=True, use_reloader=True)
    
# Path: templates/index.html
