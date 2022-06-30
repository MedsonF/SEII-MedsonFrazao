from flask import Flask, render_template, redirect, url_for

app = Flask(__name__,
            static_url_path ='',
            static_folder = 'web/static',
            template_folder =  'web/templates')

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/<dir>")
def subDir(dir):
    print(dir)
    info = f"Variável recebida: {dir}!!!"
    return render_template ("index.html", content=info)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = 8080)