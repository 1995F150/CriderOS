
function handleCredentialResponse(response) {
  const id_token = response.credential;
  fetch('https://your-backend-url.onrender.com/verify', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ token: id_token })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerText = `Signed in as: ${data.email}`;
  });
}
