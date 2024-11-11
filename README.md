# 실행방법

python main.py

# Swagger

http://localhost:8080/docs

# Environment Variable Registration

The following environment variables need to be registered. Note that the actual
installation path may vary depending on your setup, so please enter the correct path
where the programs are installed.

### Environment Variables to Register

- `FFMPEG_BINARY` - Example: `C:/ProgramData/chocolatey/bin/ffmpeg.exe`
- `IMAGEMAGICK_BINARY` - Example: `C:/Program Files/ImageMagick-7.1.1-Q16/magick.exe`

### macOS Installation (using Homebrew)

For macOS users, you can install the required programs using Homebrew:

```bash
brew install imagemagick
brew install ffmpeg
```

After installation, ensure the programs are accessible, and configure the environment
variables if necessary.
