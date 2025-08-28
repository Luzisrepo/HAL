@echo off
:: Run the PowerShell script silently from the same folder
powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File "%~dp0curl.ps1"
