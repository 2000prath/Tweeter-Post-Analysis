from flask import Flask , request , render_template
import tweeter
app= Flask("__name__")

@app.route("/",methods=["POST","GET"])
def main():
    if request.method == "GET" :
        return render_template("index.html")
    if request.method == "POST":
        text=request.form.get("text")
        
        return render_template("index.html",text=text,data=tweeter.predict(text))

if __name__ == "__main__":
    app.run(debug=True)