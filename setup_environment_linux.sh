#!/bin/bash

set -e  # Exit on error

# === CONFIGURATION ===
PYTHON_VERSION="3.9.22"
ENV_NAME="rps-env"
REQ_FILE="requirements_linux.txt"
MINICONDA_DIR="$HOME/miniconda3"
CONDA_BIN="$MINICONDA_DIR/bin/conda"
MAMBA_BIN="$MINICONDA_DIR/bin/mamba"

# === FUNCTIONS ===

install_miniconda() {
    echo "[INFO] Installing Miniconda..."
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O miniconda.sh
    bash miniconda.sh -b -p "$MINICONDA_DIR"
    rm miniconda.sh
    export PATH="$MINICONDA_DIR/bin:$PATH"
}

install_mamba() {
    echo "[INFO] Installing Mamba..."
    "$CONDA_BIN" install -y -n base -c conda-forge mamba
}

create_env() {
    echo "[INFO] Creating virtual environment: $ENV_NAME"
    "$MAMBA_BIN" create -y -n "$ENV_NAME" python="$PYTHON_VERSION"
}

activate_env() {
    # Conda environment activation requires sourcing the profile script
    echo "[INFO] Activating environment '$ENV_NAME'"
    source "$MINICONDA_DIR/etc/profile.d/conda.sh"
    conda activate "$ENV_NAME"
}

install_requirements() {
    echo "[INFO] Installing PyTorch 2.6.0 first..."
    
    "$MAMBA_BIN" install -y -n "$ENV_NAME" -c pytorch -c conda-forge \
        pytorch=2.6.0 \
        cpuonly \
        torchvision \
        torchaudio

    echo "[INFO] Activating environment for remaining installs..."
    source "$MINICONDA_DIR/etc/profile.d/conda.sh"
    conda activate "$ENV_NAME"

    echo "[INFO] Installing remaining dependencies from $REQ_FILE..."
    "$MAMBA_BIN" install -y --file "$REQ_FILE" || true

    echo "[INFO] Installing fallback packages via pip..."
    pip install --upgrade pip
    pip install -r "$REQ_FILE"
}

# === MAIN EXECUTION ===

echo "[INFO] Starting setup script..."

# Step 1: Install Miniconda if missing
if [ ! -f "$CONDA_BIN" ]; then
    install_miniconda
else
    echo "[INFO] Miniconda already installed."
    export PATH="$MINICONDA_DIR/bin:$PATH"
fi

# Step 2: Install Mamba if missing
if [ ! -f "$MAMBA_BIN" ]; then
    install_mamba
else
    echo "[INFO] Mamba already installed."
fi

# Step 3: Create environment if missing
if ! "$CONDA_BIN" env list | grep -q "$ENV_NAME"; then
    create_env
else
    echo "[INFO] Environment '$ENV_NAME' already exists."
fi

# Step 4: Install dependencies into the environment
install_requirements

echo "[INFO] Setup complete."
echo "To activate your environment, run:"
echo "source \"$MINICONDA_DIR/etc/profile.d/conda.sh\" && conda activate $ENV_NAME"