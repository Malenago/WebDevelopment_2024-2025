
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Карта изображений</title>
    <style>
        body {
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }
        #image-map {
            max-width: 100%;
            height: auto;
            position: relative;
            margin-bottom: 20px;
        }
        .message {
            display: none;
            margin-top: 20px;
            padding: 10px;
            background-color: rgba(255, 228, 225, 0.8);
            border: 1px solid rgb(246, 160, 203);
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Интерактивная карта изображений</h1>
    <img src="image.png" id="image-map" usemap="#imageMap" alt="Карта" />

    <map name="imageMap">
        <area shape="rect" coords="55,60,400,300" href="order.php" alt="ЗАКАЗ" title="Заказ">
        <area shape="circle" coords="700,200,200" href="https://ru.wikipedia.org" alt="ВИКИ" title="Вики">
        <area shape="rect" coords="1000,60,1400,300" href="https://www.youtube.com" alt="ВИДЕО" title="Видео">
        <area shape="rect" coords="1300,60,1900,300" onclick="showMessage();" alt="УВЕДОМЛЕНИЕ" title="Уведомление">
        <area shape="rect" coords="2000,60,2600,300" onclick="changeColor();" alt="ИЗМЕНИТЬ ЦВЕТ" title="Изменить цвет">
    </map>

    <div class="message" id="popupMessage">Вы нажали на область!</div>

    <script>
        function showMessage() {
            const message = document.getElementById('popupMessage');
            message.style.display = 'block';
            setTimeout(() => {
                message.style.display = 'none';
            }, 3000);
        }

        function changeColor() {
            const colors = [
                'rgba(255, 99, 71, 0.7)', 
                'rgba(240, 248, 255, 0.7)', 
                'rgba(135, 206, 250, 0.7)', 
                'rgba(255, 215, 0, 0.7)' 
            ];
            
            // Получаем текущий цвет фона
            const currentBodyColor = document.body.style.backgroundColor;
            const colorIndex = colors.indexOf(currentBodyColor);
            const newColor = colors[(colorIndex + 1) % colors.length]; 
            document.body.style.backgroundColor = newColor; 
        }
    </script>
</body>
</html>
