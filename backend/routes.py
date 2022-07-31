# API Routes
app = create_app()

@app.route("/api/customers" methods=["GET"])

def customers():
  return {"customers": ["Customer1", "Customer2", "Customer3"]}

if __name__ == "__main__":
    app.run(debug=True)