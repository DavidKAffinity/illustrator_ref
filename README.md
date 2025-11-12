illustrator_ref Generation Guide

**Requires Python 3.11 or newer.**

---

## Installation (PowerShell)

### Navigate to the Project Directory

```powershell
cd "path\to\your\projects"
```

### Clone repository from GitHub, allows local development (Remember to push changes)

```powershell
git clone https://github.com/DavidKAffinity/illustrator_ref.git
```

### Navigate to project that is importing illustrator_ref

```powershell
cd "path\to\your\project"
```

### Activate Virtual Environment

```powershell
.venv\Scripts\Activate.ps1
```

### Install illustrator_ref
-e means the illustrator_ref is in editable mode and changes to code will be updated automatically on local, rather than making a copy and putting it inside the .venv

```powershell
pip install -e ../illustrator_ref
```

## Generation (PowerShell)
If illustrator is updated and a new generation is needed

## Delete old illustrator_ref
Located in your Project Directory, inside sku_reader/src
If there is no sku_reader folder, follow Installation above

## Virtual Environment
If there is no venv, create one by navigating to your illustrator_ref folder

```powershell
cd "path/to/your/projects/illustrator_ref"
python -m venv .venv
```

## Navigate to your illustrator_ref folder and activate .venv

```powershell
cd "path/to/your/projects/illustrator_ref"
./.venv/Scripts/Activate.ps1
```

## Generate Library

```powershell
python
```

```python
from win32com.client import makepy
makepy.main()
```

Select Adobe Illustrator 20** Type Library *.*

## Copy Library to Local illustrator_ref and rename as illustrator_ref
The file will be placed inside \AppData\Local\Temp\gen_py\

## Git Add, Push, and Commit

```powershell
git add src/illustrator_ref/illustrator_ref.py
git commit -m "Generated new Illustrator COM Wrapper"
git push
```