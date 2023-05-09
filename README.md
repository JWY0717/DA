# GC project
- ais 신호 수신하여 mysql에 저장
- [node](https://nodejs.org/ko/download)
- .env <<

## Project start
```
npm install
/VesselSignalProcessor/index.exe
/VesselSignalProcessor/VesselSignalProcessor.exe
npm run start
```

## Run server (.bat)
```
@echo off
:while
start "" /WAIT "C:\VesselSignalProcessor\index.exe"
start "" /WAIT "C:\VesselSignalProcessor\VesselSignalProcessor.exe"
start "" /WAIT "C:\Program Files\nodejs\node.exe" "C:\AisServer\ais.js"
echo "AIS server has stopped unexpectedly, restarting in 5 seconds..."
timeout /t 5 > nul
goto :while
```
