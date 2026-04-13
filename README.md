<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neuro-Insulin VPN | 2026 Matrix Interface</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Cairo:wght@300;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-green: #39FF14;
            --dark-bg: #050505;
            --glow-shadow: 0 0 15px rgba(57, 255, 20, 0.5);
        }

        body, html {
            margin: 0;
            padding: 0;
            background-color: var(--dark-bg);
            color: var(--neon-green);
            font-family: 'Orbitron', 'Cairo', sans-serif;
            overflow-x: hidden;
            min-height: 100vh;
        }

        /* حاوية مطر الماتريكس */
        #matrix-canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
            opacity: 0.8; /* شفافية المطر لعدم تشتيت القراءة */
        }

        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            z-index: 1;
            position: relative;
            background: rgba(5, 5, 5, 0.6); /* طبقة شفافة لتسهيل الرؤية */
            min-height: 100vh;
            border: 1px solid var(--neon-green);
        }

        header {
            text-align: center;
            padding: 40px 20px;
            text-shadow: var(--glow-shadow);
        }

        h1 {
            font-size: 2.2rem;
            letter-spacing: 4px;
            margin-bottom: 5px;
            animation: glitch 3s infinite;
        }

        .status-bar {
            border: 1px solid var(--neon-green);
            padding: 8px 15px;
            font-size: 0.85rem;
            margin-bottom: 25px;
            box-shadow: var(--glow-shadow);
            background: rgba(0, 0, 0, 0.8);
        }

        .search-container {
            width: 85%;
            max-width: 500px;
            position: relative;
        }

        input[type="text"] {
            width: 100%;
            background: rgba(0, 0, 0, 0.9);
            border: 2px solid var(--neon-green);
            padding: 12px 15px;
            color: var(--neon-green);
            font-family: 'monospace';
            outline: none;
            box-shadow: var(--glow-shadow);
        }

        .search-btn {
            position: absolute;
            left: 5px;
            top: 50%;
            transform: translateY(-50%);
            background: var(--neon-green);
            color: black;
            border: none;
            padding: 5px 12px;
            cursor: pointer;
            font-weight: bold;
        }

        .content-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            width: 90%;
            margin-top: 30px;
            padding-bottom: 40px;
        }

        .card {
            border: 1px solid var(--neon-green);
            padding: 15px;
            background: rgba(0, 0, 0, 0.8);
            transition: 0.3s;
            cursor: pointer;
            backdrop-filter: blur(5px);
        }

        .card:hover {
            background: var(--neon-green);
            color: black;
            box-shadow: var(--glow-shadow);
        }

        @keyframes glitch {
            0% { transform: skew(0deg); }
            20% { transform: skew(3deg); }
            24% { transform: skew(-3deg); }
            28% { transform: skew(0deg); }
            100% { transform: skew(0deg); }
        }

        footer {
            margin-top: auto;
            padding: 15px;
            font-size: 0.75rem;
            text-align: center;
            width: 100%;
            background: rgba(0, 0, 0, 0.9);
        }
    </style>
</head>
<body>

    <canvas id="matrix-canvas"></canvas>

    <div class="main-container">
        <header>
            <h1>NEURO-INSULIN VPN</h1>
            <p>تكنولوجيا 2026: خوارزمية التحرر من الإدمان</p>
        </header>

        <div class="status-bar">
            SYSTEM STATUS: <span id="typing">CONNECTING...</span>
        </div>

        <div class="search-container">
            <form action="https://www.google.com/search" method="GET">
                <input type="text" name="q" placeholder="ابحث في أعماق النظام..." required>
                <button type="submit" class="search-btn">SCAN</button>
            </form>
        </div>

        <div class="content-grid">
            <div class="card">
                <h3>تصفية النواقل</h3>
                <p>تنظيم استقبال التنبيهات الرقمية لتحسين التركيز الفائق.</p>
            </div>
            <div class="card">
                <h3>جدار حماية الدوبامين</h3>
                <p>منع التطبيقات من استنزاف طاقتك العصبية دون إذنك.</p>
            </div>
            <div class="card">
                <h3>بروتوكول 2026</h3>
                <p>تشفير تام للهوية مع حماية من تتبع الذكاء الاصطناعي.</p>
            </div>
        </div>

        <footer>
            © 2026 Kabbach Systems | Casablanca Interface v4.0
        </footer>
    </div>

    <script>
        // --- 1. تأثير مطر الماتريكس ---
        const canvas = document.getElementById('matrix-canvas');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$+-*/=%'\"#&_()[]{}<>^|!?.";
        const fontSize = 16;
        const columns = canvas.width / fontSize;
        const drops = Array(Math.floor(columns)).fill(1);

        function drawMatrix() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = "#39FF14";
            ctx.font = fontSize + "px monospace";

            for (let i = 0; i < drops.length; i++) {
                const text = letters.charAt(Math.floor(Math.random() * letters.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }

        setInterval(drawMatrix, 35);

        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });

        // --- 2. تأثير الكتابة الآلية ---
        const statusText = "MATRIX LINK ESTABLISHED | NEURO-FILTER ACTIVE | ENCRYPTED";
        let j = 0;
        function typeWriter() {
            if (j < statusText.length) {
                document.getElementById("typing").innerHTML += statusText.charAt(j);
                j++;
                setTimeout(typeWriter, 80);
            }
        }
        document.getElementById("typing").innerHTML = "";
        typeWriter();
    </script>
</body>
</html>
