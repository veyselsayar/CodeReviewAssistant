document.getElementById('analyzeBtn').addEventListener('click', () => {
    const code = document.getElementById('codeInput').value;

    fetch('http://127.0.0.1:5000/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code })
    })
    .then(res => res.json())
    .then(data => {
        if(data.error) {
            document.getElementById('result').textContent = 'Hata: ' + data.error;
        } else {
            document.getElementById('result').textContent = JSON.stringify(data.result, null, 2);
        }
    })
    .catch(err => {
        document.getElementById('result').textContent = 'İstek hatası: ' + err;
    });
});
