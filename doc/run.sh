# pip install sphinx
# pip install furo
#sphinx-build . _build 

#!/usr/bin/env bash

WATCH_DIR="."
BUILD_CMD="sphinx-build . _build"

echo "Watching .md files under $(pwd)..."

inotifywait -m -r \
  -e modify,create,delete,move \
  --format '%f' \
  "$WATCH_DIR" | while read file
do
  if [[ "$file" == *.md ]]; then
    echo "Detected change in $file"
    echo "Running sphinx-build..."
    $BUILD_CMD
    echo "Build finished."
  fi
done
