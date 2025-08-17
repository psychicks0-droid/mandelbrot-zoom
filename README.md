# Mandelbrot Fractal Zoom Explorer

<img src="examples/zoom_demo.gif" alt="Zoom Demo" width="100%" style="max-width: 600px;">

## Features
- 60-level smooth zoom (30,000x magnification)
- Customizable center points & color maps
- 800×800px resolution @ 300 iterations
- Automatic video/GIF generation

## Quick Start
```bash
git clone https://github.com/psychicks0-droid/mandelbrot-zoom.git
cd mandelbrot-zoom
pip install -r requirements.txt
python mandelbrot.py
```

## Customization
Edit parameters in mandelbrot.py:

```python
generate_mandelbrot(
    center=(-0.16, 1.04),  # Dragon Valley coordinates
    zoom_levels=100,       # Increase for smoother zoom
    max_iterations=500,    # Higher = more detail
    cmap='twilight',       # Color map
    output_dir="renders"   # Custom output folder
)
```

## Requirements
- Python 3.9+

- Packages:

```bash
text
numpy>=1.20
matplotlib>=3.4
tqdm>=4.60
FFmpeg (for video conversion)
```

## Video Creation

```bash
./make_video.sh  # Converts PNGs to MP4/GIF
```

## License
MIT © 2025 Psychicks
