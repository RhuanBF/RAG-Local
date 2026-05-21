//captura de elementos
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const fileInput = document.getElementById("file-input");
const uploadBtn = document.getElementById("upload-btn");
const barraLateralBox = document.getElementById("barra-lateral-box");

async function sendMessage() {
  const mensagem = userInput.value.trim();//trim para remover os espaços em branco (strip())
  if (!mensagem) //se mensage for vazio retorna
    return;
  addMessage("Você", mensagem); //balão de fala
  userInput.value = "";
  try { 
    //o '/chat' é para conectar com o route da API (irá esperar uma resposta)
    const response = await fetch("http://127.0.0.1:8000/chat", { 
      method: "POST",
      headers: { "Content-Type": "application/json" }, 
      body: JSON.stringify({ mensagem: mensagem })//tranforma em string para passar pela rede
    });
    const data = await response.json();//transforma o json em objeto novamente
    addMessage("ChatBot", data.resposta || "Sem resposta.");
  } catch (error) {
    addMessage("Erro", "Erro ao conectar com a API.");
  }
}

async function uploadFiles(files) {
  const formData = new FormData();
  
  // Adiciona todos os arquivos na mesma caixinha com o nome "files" (plural)
  for (const file of files) {
    formData.append("files", file);
  }

  try {
    addMessage("Sistema", `Enviando ${files.length} arquivo(s)...`);

    const response = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      throw new Error(`Erro no servidor: ${response.status}`);
    }

    const data = await response.json();

    // Adiciona cada um dos arquivos na barra lateral
    for (const file of files) {
      adicionarArquivoNaBarra(file.name);
    }

    addMessage("Sistema", "Todos os arquivos foram processados e salvos com sucesso!");

  } catch (error) {
    addMessage("Erro", "Erro ao enviar o lote de arquivos.");
    console.error(error);
  }
}

function addMessage(sender, text) {
  const msg = document.createElement("div");
  msg.classList.add("mensagem");
  const formattedText = text.replace(/\n/g, "<br>");
  msg.innerHTML = `<strong>${sender}:</strong><br>${formattedText}`;
  msg.style.marginBottom = "15px";
  msg.style.color = "#ffffff";
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function adicionarArquivoNaBarra(nomeArquivo) {
  const item = document.createElement("div");
  item.classList.add("arquivo-item");
  item.innerHTML = `<i class="fa-solid fa-file-upload"></i> ${nomeArquivo}`;
  barraLateralBox.appendChild(item);
}

uploadBtn.addEventListener("click", () => {
  fileInput.click();
});

fileInput.addEventListener("change", async () => {
  const files = fileInput.files;
  if (files.length === 0) return;
  
  // Envia a lista completa de uma vez so
  await uploadFiles(files);
  
  fileInput.value = "";
});

userInput.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    sendMessage();
  }
});

window.addEventListener("DOMContentLoaded", () => {
  addMessage("ChatBot", "Olá! Envie documentos e faça perguntas sobre eles.");
});