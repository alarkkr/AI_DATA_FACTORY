Write-Host "Restoring AI_DATA_FACTORY to Phase 6 checkpoint..."

Copy-Item CHECKPOINT_PHASE6\core . -Recurse -Force
Copy-Item CHECKPOINT_PHASE6\crawler . -Recurse -Force
Copy-Item CHECKPOINT_PHASE6\processing . -Recurse -Force
Copy-Item CHECKPOINT_PHASE6\ai_processing . -Recurse -Force
Copy-Item CHECKPOINT_PHASE6\database . -Recurse -Force
Copy-Item CHECKPOINT_PHASE6\knowledge_graph . -Recurse -Force
Copy-Item CHECKPOINT_PHASE6\dataset_builder . -Recurse -Force
Copy-Item CHECKPOINT_PHASE6\control_panel . -Recurse -Force

Copy-Item CHECKPOINT_PHASE6\*.py . -Force

Write-Host "Restore complete."
