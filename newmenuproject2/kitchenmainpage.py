import json
from flask import Flask, redirect, request

with open("C:\\Users\\DELL\\Downloads\\Python 2\\restaurant_menu_project\\newmenuproject2\\data.json", "r") as f:
    data = json.load(f)

finishedMenuItems = {}

app = Flask(__name__)

@app.route("/")
def home():
    with open("C:\\Users\\DELL\\Downloads\\Python 2\\restaurant_menu_project\\newmenuproject2\\data.json", "r") as f:
        data = json.load(f)
        data = dict(reversed(list(data.items())))
    print("Data has been updated:", data)
    page = ""
    g = open("C:\\Users\\DELL\\Downloads\\Python 2\\restaurant_menu_project\\newmenuproject2\\havetocooklist.html","r")
    page = g.read()
    for key, vluae in finishedMenuItems.items():
        if key in data:
            del data[key]
    
    for ranNumber, value in data.items():
        

        page += f""""<div>{ranNumber}</div>
            <div>{value['time']}</div>
            <div>{value['tableNumber']}</div>
            """
        for item, qty in value['order'].items():
            if qty > 0:
                page += f""""<div>{item}: {qty}</div>"""
        page += f"""
                <form action="/finished" method="post">
                <button type="submit" value="{value}" name="{ranNumber}">Finished</button>
    </form>
                <div>--------------------</div>"""
    g.close()
    return page

@app.route("/finished", methods=["POST"])
def finished():
    form =  request.form
    finishedMenuItems.update(form)
    
    return redirect("/")
app.run(host="0.0.0.0",port=5001)
