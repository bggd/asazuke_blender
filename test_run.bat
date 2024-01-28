setlocal
set PYTHONPATH=%PYTHONPATH%;.venv\\Lib\\site-packages;.

blender blend\\default_scene.blend --background -noaudio --factory-startup --python tests\\test_default_scene.py

endlocal
