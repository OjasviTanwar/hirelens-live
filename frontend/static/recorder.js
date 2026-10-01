let mediaRecorder = null;
let audioChunks = [];
let hasRecorded = false;

async function startRecording() {
  // ✅ NEW: block recording during coding questions
  if (document.getElementById("codeBox")?.style.display === "block") {
    alert("Voice answer not required for coding questions");
    return;
  }

  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);

  audioChunks = [];
  hasRecorded = false;
  mediaRecorder.start();

  mediaRecorder.ondataavailable = e => {
    if (e.data.size > 0) audioChunks.push(e.data);
  };
}

function stopRecording() {
  if (!mediaRecorder) return;

  mediaRecorder.stop();

  mediaRecorder.onstop = async () => {
    const blob = new Blob(audioChunks, { type: "audio/wav" });
    const formData = new FormData();
    formData.append("audio", blob, "answer.wav");

    await fetch("/upload_audio", {
      method: "POST",
      body: formData
    });

    hasRecorded = true;
  };
}

async function analyze() {
  // ✅ NEW: block analysis during coding questions
  if (document.getElementById("codeBox")?.style.display === "block") {
    alert("Analysis is not required for coding questions");
    return;
  }

  if (!hasRecorded) {
    alert("Record answer first");
    return;
  }

  document.getElementById("loader").style.display = "block";

  const res = await fetch("/analyze", { method: "POST" });
  const data = await res.json();

  document.getElementById("loader").style.display = "none";
  document.getElementById("report").innerText = data.report || "No feedback";
}
