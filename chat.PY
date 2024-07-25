from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/traiter_formulaire', methods=['POST'])
def traiter_formulaire():
    ville = request.form.get('city', '')
    print("Voici ma ville:", ville)  # Ceci est la valeur entrée par l'utilisateur
    # Traitez les données du formulaire ici...
    return "Données du formulaire traitées avec succès."
if __name__ == '__main__':
    app.run(debug=True)
