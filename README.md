## Overview
Local VM (VirtualBox + Linux Mint) monitors CPU. When CPU > 75%, triggers auto-scale to GCP.

## Files
- monitor.py - CPU/RAM monitoring script
- autoscale.py - Auto-scale trigger script  
- app.py - Flask app deployed on GCP
- metrics.csv - Recorded CPU/RAM metrics
- autoscale_log.csv - Auto-scale trigger log
- scale_trigger.txt - Trigger event proof

## GCP Setup
- Project: vm-autoscale
- Cloud VM: cloud-scale-vm (34.28.200.21)
- MIG: autoscale-mig (CPU 75%, Min:1, Max:3)
