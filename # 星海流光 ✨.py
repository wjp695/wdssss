<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>玫瑰星箭 · 3D氛围感</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html, body {
            height: 100%;
            width: 100%;
            overflow: hidden;
            background: #000;
            perspective: 1500px; /* 3D 核心效果 */
        }

        /* 视频背景 */
        .video-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -2;
            opacity: 0.85;
            filter: brightness(0.9) contrast(1.1);
        }

        /* 3D 光晕氛围层 */
        .light-effect {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 50% 50%, rgba(255, 0, 140, 0.15), transparent 60%);
            z-index: -1;
            animation: lightMove 12s infinite alternate ease-in-out;
        }

        /* 3D 浮动文字 */
        .content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform-style: preserve-3d;
            transform: translate(-50%, -50%) rotateX(10deg) rotateY(-10deg);
            color: #ff2e96;
            font-size: 5rem;
            font-family: 华文彩云;
            text-shadow: 
                0 0 15px rgba(255, 46, 150, 0.8),
                0 0 30px rgba(255, 0, 130, 0.6),
                0 0 45px rgba(255, 0, 100, 0.4);
            text-align: center;
            animation: float3d 6s ease-in-out infinite;
            z-index: 10;
        }

        /* 星光粒子 */
        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background-image:
                radial-gradient(2px 2px at 20px 30px, #fff, transparent),
                radial-gradient(2px 2px at 60px 70px, #fff, transparent),
                radial-gradient(1px 1px at 50px 50px, #ffc0dd, transparent),
                radial-gradient(2px 2px at 120px 150px, #fff, transparent);
            background-size: 200px 200px;
            opacity: 0.5;
            animation: starMove 25s linear infinite;
        }

        /* 3D浮动动画 */
        @keyframes float3d {
            0% { transform: translate(-50%, -50%) rotateX(10deg) rotateY(-10deg) translateY(0px); }
            50% { transform: translate(-50%, -50%) rotateX(-5deg) rotateY(10deg) translateY(-25px); }
            100% { transform: translate(-50%, -50%) rotateX(10deg) rotateY(-10deg) translateY(0px); }
        }

        /* 光晕流动 */
        @keyframes lightMove {
            0% { transform: scale(1); opacity: 0.4; }
            50% { transform: scale(1.3); opacity: 0.7; }
            100% { transform: scale(1); opacity: 0.4; }
        }

        /* 星星移动 */
        @keyframes starMove {
            0% { background-position: 0 0; }
            100% { background-position: 200px 200px; }
        }
    </style>
</head>
<body>

    <!-- 3D星光层 -->
    <div class="stars"></div>

    <!-- 视频背景 -->
    <video class="video-background" autoplay muted loop>
        <source src="玫瑰星箭.mp4" type="video/mp4">
    </video>

    <!-- 光晕 -->
    <div class="light-effect"></div>

    <!-- 3D文字 -->
    <div class="content">
        玫瑰星箭
    </div>

    <!-- 音乐 -->
    <audio id="music1" loop preload="auto" hidden>
        <source src="http://music.163.com/song/media/outer/url?id=1963443271.mp3">
    </audio>

    <script>
        document.body.addEventListener('click', () => {
            const audio = document.getElementById('music1');
            audio.volume = 0.7;
            audio.play();
        });
    </script>

</body>
</html>