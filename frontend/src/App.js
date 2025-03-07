<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Threat Intelligence Graph</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Cyber Threat Intelligence Graph</h1>
    
    <div>
        <h2>Add Threat Data</h2>
        <input type="text" id="ip" placeholder="IP Address">
        <input type="text" id="domain" placeholder="Domain">
        <input type="text" id="threat" placeholder="Threat Indicator">
        <button onclick="addThreat()">Add Threat</button>
    </div>

    <div>
        <h2>Query Threat Intelligence</h2>
        <input type="text" id="queryIp" placeholder="Enter IP Address">
        <button onclick="queryThreat()">Query</button>
        <p id="queryResult"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
