@echo off
title �ļ����ַ��滻
mode con cols=60 lines=20
::�ļ�Ҫ������������ʾ����
setlocal EnableDelayedExpansion & color 0a
:1
set a=
set b=
set c=
cls&echo.
set /p a= ������Ҫ���滻���ַ�:
cls&echo.
set /p b= �������滻��!a!�����ַ�����Ҫȥ����!a!������ֱ�ӻس�:
for /f "delims=" %%a in ('dir /b /a /a-d') do (
if "%%~fa" neq "%~0" (
set xz=%%~na
ren "%%~fa" "!xz:%a%=%b%!%%~xa" ))
cls&echo.&set /p c= ������ɣ����� 0 ���أ��������������ַ��˳�
if "!c!"=="0" (goto 1) else (exit)
GOTO :EOF