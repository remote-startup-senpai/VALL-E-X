#!/bin/bash

echo "[01/03] 📂 Preparing folders..."
mkdir -p checkpoints
mkdir -p whisper
echo "[01/03] ✅ Folders created!"

echo "[02/03] 🎤 Downloading VALL-E-X checkpoint..."
curl \
    -o checkpoints/vallex-checkpoint.pt \
    -L https://huggingface.co/Plachta/VALL-E-X/resolve/main/vallex-checkpoint.pt
echo "[02/03] ✅ VALL-E-X checkpoint downloaded!"

echo "[03/03] 🤫 Downloading Whisper checkpoint..."
curl \
    -o whisper/medium.pt \
    -L https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt
echo "[03/03] ✅ VALL-E-X checkpoint downloaded!"
