#!/bin/bash
git add .
git commit -m "Mise à jour automatique - $(date)"
git push origin main --force
echo "✅ Système Neuro-Insulin mis à jour sur GitHub !"
