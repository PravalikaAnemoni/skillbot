# PowerShell setup script for SkillBot project
# Usage: Open PowerShell, run: .\scripts\setup_env.ps1

param(
    [string]$venvPath = ".venv"
)

Write-Host "Setting up virtual environment in $venvPath"

# Create venv if it doesn't exist
if (-not (Test-Path $venvPath)) {
    python -m venv $venvPath
}

# Activate venv for the current session
$activate = Join-Path $venvPath "Scripts\Activate.ps1"
if (Test-Path $activate) {
    Write-Host "Activating virtual environment..."
    & $activate
} else {
    Write-Error "Activation script not found at $activate"
    exit 1
}

# Upgrade pip and install requirements
Write-Host "Upgrading pip and installing requirements.txt"
python -m pip install --upgrade pip
pip install -r .\requirements.txt

# Install spaCy English model if not present
Write-Host "Checking for spaCy model en_core_web_sm"
try {
    python -c "import spacy; spacy.load('en_core_web_sm')" 2>$null
    Write-Host "spaCy model en_core_web_sm already installed."
} catch {
    Write-Host "Downloading spaCy model en_core_web_sm..."
    python -m spacy download en_core_web_sm
}

# Download TextBlob corpora (safe to run even if already present)
Write-Host "Downloading TextBlob corpora (may take a minute)"
python -m textblob.download_corpora

Write-Host "Setup complete. To start the API: python .\api\main.py"
Write-Host "To run the demo UI: streamlit run .\demo\app.py"
