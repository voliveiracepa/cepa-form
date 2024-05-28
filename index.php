<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Eventos</title>
</head>
<body>
    <h1>Cadastro de Acidente/Incidente</h1>
    <form id="eventForm" action="/submit" method="post" enctype="multipart/form-data">
        <label for="driverName">Nome do Condutor:</label>
        <input type="text" id="driverName" name="driverName" required><br><br>
        
        <label for="eventDate">Data do Evento:</label>
        <input type="date" id="eventDate" name="eventDate" required><br><br>

        <label for="eventDescription">Descrição do Evento:</label>
        <textarea id="eventDescription" name="eventDescription" required></textarea><br><br>

        <label for="reportFile">Boletim de Ocorrência (PDF):</label>
        <input type="file" id="reportFile" name="reportFile" accept=".pdf" required><br><br>

        <label for="photos">Fotos do Acidente (JPEG, JPG, PNG):</label>
        <input type="file" id="photos" name="photos" accept=".jpeg,.jpg,.png" multiple required><br><br>

        <button type="submit">Enviar</button>
    </form>
</body>
</html>