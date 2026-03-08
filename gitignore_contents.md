# Build outputs
dist/
build/
*.egg-info/

# Model weights (handled by git-lfs, not regular git)
model/weights/checkpoints/*
!model/weights/checkpoints/.gitkeep

# OS metadata
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
Thumbs.db
desktop.ini

# Python
__pycache__/
*.py[cod]
*.pyo
.env
.venv
venv/
*.egg

# Editor artifacts
.vscode/
.idea/
*.swp
*.swo
*~

# Temporary and cache
*.tmp
*.cache
.cache/
*.log

# Node (if any JS tooling added later)
node_modules/

# Training artifacts not yet committed
*.safetensors.tmp
*.bin.tmp

# Obsidian
.obsidian/