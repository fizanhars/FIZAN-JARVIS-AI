from flask import Flask, request, jsonify, render_template_string
from jarvis.ai import JarvisAI

app = Flask(__name__)
assistant = JarvisAI()

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FIZAN JARVIS AI</title>
    <style>
        body {
            background: #0b0f14;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 30px 15px;
        }

        h1 {
            margin-top: 30px;
        }

        #status {
            margin: 20px;
            color: #aaa;
        }

        button {
            border: 0;
            border-radius: 50%;
            width: 90px;
            height: 90px;
            font-size: 36px;
            cursor: pointer;
        }

        #output {
            max-width: 600px;
            margin: 30px auto;
            padding: 20px;
            background: #151b23;
            border-radius: 15px;
            text-align: left;
            min-height: 80px;
        }
    </style>
</head>

<body>
    <h1>🤖 FIZAN JARVIS AI</h1>
    <p id="status">Ready</p>

    <button id="mic">🎤</button>

    <div id="output">
        <b>JARVIS:</b>
        <span id="answer">Waiting for your question...</span>
    </div>

<script>
const mic = document.getElementById("mic");
const status = document.getElementById("status");
const answer = document.getElementById("answer");

const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

if (!SpeechRecognition) {
    status.textContent =
        "Speech recognition is not supported in this browser.";
} else {

    const recognition = new SpeechRecognition();

    recognition.lang = "en-IN";
    recognition.continuous = false;
    recognition.interimResults = false;

    mic.onclick = () => {
        status.textContent = "🎤 Listening...";
        recognition.start();
    };

    recognition.onresult = async (event) => {
        const text = event.results[0][0].transcript;

        status.textContent = "Thinking...";
        answer.textContent = text;

        try {
            const response = await fetch("/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: text
                })
            });

            const data = await response.json();

            answer.textContent = data.reply;
            status.textContent = "JARVIS is ready";

            const speech = new SpeechSynthesisUtterance(data.reply);
            speech.lang = "en-IN";
            speechSynthesis.cancel();
            speechSynthesis.speak(speech);

        } catch (error) {
            status.textContent = "Connection error";
            answer.textContent = "JARVIS could not connect.";
        }
    };

    recognition.onerror = () => {
        status.textContent = "Microphone error. Please try again.";
    };

    recognition.onend = () => {
        if (status.textContent === "🎤 Listening...") {
            status.textContent = "Ready";
        }
    };
}
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()

    if not message:
        return jsonify({"reply": "Please say something."})

    reply = assistant.reply(message)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
