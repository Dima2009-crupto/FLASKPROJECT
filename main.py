from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


survey_results = {"Маргарита": 0, "Пепероні": 0, "Гавайська": 0}


menu = [
    {"name": "Мисливска", "description": "Томатний соус," "Сир моцарелла," "Солоні огірочки," "Смажена цибуля," "Ковбаски мисливські копчені," "Соус Dijon", "price": 180},
    {"name": "Пепероні", "description": "Томатний соус, сир, пепероні", "price": 150},
    {"name": "Гавайська", "description": "Томатний соус, сир, ананас, шинка", "price": 140}
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer in survey_results:
            survey_results[answer] += 1
        return redirect(url_for("results"))
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html", results=survey_results)

@app.route("/menu")
def menu_page():
    return render_template("menu.html", menu=menu)

@app.route("/add_menu", methods=["GET", "POST"])
def add_menu():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")


        if name and description and price:
            menu.append({"name": name, "description": description, "price": float(price)})
            return redirect(url_for("menu_page"))
    return render_template("add_menu.html")

if __name__ == "__main__":
    app.run(debug=True)