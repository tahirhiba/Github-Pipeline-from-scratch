from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory database
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

# Point de terminaison pour les webhooks de test
@app.route('/webhook/testing', methods=['POST'])
def testing_webhook():
    data = request.json
    # Traitement spécifique pour les événements de test ici
    # Par exemple : valider le payload et déclencher une action
    return jsonify({'status': 'Webhook de test reçu!'}), 200

# Point de terminaison pour les webhooks de déploiement
@app.route('/webhook/deployment', methods=['POST'])
def deployment_webhook():
    data = request.json
    # Traitement spécifique pour les événements de déploiement ici
    # Par exemple : déployer une mise à jour de l'application
    return jsonify({'status': 'Webhook de déploiement reçu!'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
