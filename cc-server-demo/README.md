## VSCode Extensions

- `C/C++`
- `CMake Tools`

## Set Environment

```powershell
$env:VCPKG_ROOT = "X:\\your\\vckpg\\path"
$env:PATH = "$env:PATH;$env:VCPKG_ROOT"
```

## Install dependencies

```powershell
# vcpkg add port drogon
vcpkg install
```

## Build & Run

#### Using command

```powershell
cmake --preset=Release
cd ./build/Release
cmake --build .
ninja .
cc-server-demo.exe
```

#### Using VSCode Extensions GUI

1. Select `Release` preset on the bottom status bar
2. Select ▶️ to build and run
