PowerShell ile sanal ortamı etkinleştirme

- PowerShell (Windows):
  .\.venv\Scripts\Activate.ps1

- CMD (Windows):
  .\.venv\Scripts\activate.bat

- Git Bash / WSL:
  source .venv/Scripts/activate

Eğer PowerShell Execution Policy engel olursa, geçici olarak izin vermek için:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Kullanım örneği:

.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

Python yürütülebilir dosyası: `.venv\Scripts\python.exe`
