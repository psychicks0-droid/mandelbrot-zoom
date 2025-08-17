#!/bin/bash

# Конвертация PNG в MP4 (H.264)
ffmpeg -framerate 30 -pattern_type glob -i "output/mandelbrot_*.png" \
  -c:v libx264 -pix_fmt yuv420p -crf 23 \
  -vf "scale=800:800:flags=lanczos" \
  examples/mandelbrot_zoom.mp4

# Создание GIF (опционально)
ffmpeg -i examples/mandelbrot_zoom.mp4 \
  -vf "fps=15,scale=400:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  -loop 0 examples/mandelbrot_zoom.gif

echo "Видео создано: examples/mandelbrot_zoom.mp4"
echo "GIF создан: examples/mandelbrot_zoom.gif"