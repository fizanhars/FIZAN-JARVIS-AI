from flask import Flask, request, jsonify
from jarvis.ai import JarvisAI

app = Flask(__name__)
assistant = JarvisAI()


@app.get("/")
def home():
    return """
    <!doctype html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>FIZAN JARVIS AI</title>
    </head>
    <body>
        <h1>FIZAN JARVIS AI</h1>

        <input id="message" placeholder="Ask JARVIS..." />
        <button onclick="askJarvis()">Send</button>

        <p id="reply"></p>

        <script>
        async function askJarvis() {
            const message = document.getElementById("message").value;

            const response = await fetch("/ask", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({message})
            });

            const data = await response.json();
            document.getElementById("reply").innerText = data.reply;
        }
        </script>
    </body>
    </html>
    """


@app.post("/ask")
def ask():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()

    if not message:
        return jsonify({"reply": "Please enter a message."}), 400

    return jsonify({"reply": assistant.reply(message)})
if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


