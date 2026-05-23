@echo off
REM Wrapper script for running challenge tests
REM Usage: test.bat raindrops
REM        test.bat word-count
REM        test.bat -l  (list all challenges)

setlocal enabledelayedexpansion

if "%1"=="" (
    echo Usage: test.bat ^<challenge-name^>
    echo Example: test.bat raindrops
    echo.
    echo Run "test.bat -l" to list all challenges
    exit /b 1
)

if "%1"=="-l" (
    python challenges\test_runner.py --list
    exit /b 0
)

python challenges\test_runner.py %1
