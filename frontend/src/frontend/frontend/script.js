const backendUrl = "http://localhost:5000";

function addThreat() {
    const ip = document.getElementById("ip").value;
    const domain = document.getElementById("domain").value;
    const threat = document.getElementById("threat").value;

    fetch(`${backendUrl}/add_threat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ip, domain, threat })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error("Error:", error));
}

function queryThreat() {
    const ip = document.getElementById("queryIp").value;

    fetch(`${backendUrl}/query_threat?ip=${ip}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("queryResult").innerText = data.threat_info || "No data found";
    })
    .catch(error => console.error("Error:", error));
}
