const chat = document.getElementById("chat");
const cart = JSON.parse(localStorage.getItem("cart") || "[]");

function send() {
  const q = query.value.trim();
  if (!q) return;

  addMsg(q, "user");
  query.value = "";

  fetch("https://ai-price-compare-backend.onrender.com/search", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      query: q,
      mode: document.querySelector('input[name="mode"]:checked').value
    })
  })
  .then(r => r.json())
  .then(showResults)
  .catch(() => addMsg("Something went wrong. Try again.", "bot"));
}

function showResults(data) {
  data.results.forEach(p => {
    chat.innerHTML += `
      <div class="card">
        <b>${p.platform}</b><br>
        ₹${p.price}<br>
        <button onclick="openApp('${p.link}')">Open App</button>
        <button onclick="addToCart('${p.name}','${p.link}')">Add to Cart</button>
      </div>`;
  });
}

function addMsg(text, type) {
  chat.innerHTML += `<div class="msg ${type}">${text}</div>`;
}

function openApp(link) {
  window.location.href = link;
}

function addToCart(name, link) {
  cart.push({ name, link });
  localStorage.setItem("cart", JSON.stringify(cart));
  alert("Added to temporary cart");
}
