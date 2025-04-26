#!/bin/bash
PROJECT_DIR="tarnsparent_screan"
OUTPUT="transparent_display.tar.gz"

echo "📦 打包專案為 $OUTPUT ..."
tar --exclude="$PROJECT_DIR/venv" \
    --exclude="$PROJECT_DIR/__pycache__" \
    -czf $OUTPUT $PROJECT_DIR

echo "✅ 打包完成！"