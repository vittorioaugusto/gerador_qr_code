from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form["link"]
        nome = request.form["nome"] or "qr_code"  # Se o nome não for fornecido, use "qr_code"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_io = BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)

        response = send_file(img_io, mimetype="image/png")
        response.headers["Content-Disposition"] = f"inline; filename={nome}.png"
        return response

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
