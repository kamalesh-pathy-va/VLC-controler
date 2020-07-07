#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

SetTitleMatchMode, 2
^#!v::WinActivate, VLC
^#!p::send {SPACE}
^#!f::send {Right Down}
^#!r::send {Left Down}
^#!u::send {Up Down}
^#!d::send {Down Down}
^#!m::send m
^#!b::send f