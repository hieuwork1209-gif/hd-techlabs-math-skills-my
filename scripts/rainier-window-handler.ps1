param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Uri
)

$ErrorActionPreference = 'Stop'

function Show-RainierError([string]$Message) {
    try {
        Add-Type -AssemblyName PresentationFramework -ErrorAction Stop
        [System.Windows.MessageBox]::Show(
            $Message,
            'Rainier window routing',
            [System.Windows.MessageBoxButton]::OK,
            [System.Windows.MessageBoxImage]::Warning
        ) | Out-Null
    } catch {
        # The protocol handler is normally hidden. If UI cannot be shown,
        # there is intentionally no browser fallback because that could route
        # the chat into the wrong signed-in Chrome window.
    }
}

try {
    $parsed = [Uri]$Uri
    if ($parsed.Scheme -ne 'rainier-chat') {
        throw 'invalid Rainier protocol scheme'
    }

    $problem = $parsed.Host
    if ($problem -notmatch '^problem[0-9]+$') {
        throw 'invalid problem identifier in Rainier protocol URL'
    }

    $encoded = $parsed.AbsolutePath.Trim('/')
    if (-not $encoded) {
        throw 'missing encoded ChatGPT URL'
    }
    $encoded = $encoded.Replace('-', '+').Replace('_', '/')
    $padding = (4 - ($encoded.Length % 4)) % 4
    if ($padding -gt 0) {
        $encoded += ('=' * $padding)
    }
    $chatUrl = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($encoded))

    $chat = [Uri]$chatUrl
    if ($chat.Scheme -ne 'https' -or
        $chat.Host -notin @('chatgpt.com', 'chat.openai.com') -or
        $chat.AbsolutePath -notmatch '/c/') {
        throw 'protocol payload is not a valid ChatGPT conversation URL'
    }

    $bindingPath = Join-Path $env:LOCALAPPDATA ("Rainier\window-bindings\{0}.json" -f $problem)
    if (-not (Test-Path -LiteralPath $bindingPath)) {
        throw "no local window binding for $problem; run rainier-bind-window.py first"
    }
    $binding = Get-Content -LiteralPath $bindingPath -Raw | ConvertFrom-Json

    Add-Type @"
using System;
using System.Runtime.InteropServices;
public static class RainierWindow {
    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool IsWindow(IntPtr hWnd);

    [DllImport("user32.dll")]
    public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint processId);

    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool BringWindowToTop(IntPtr hWnd);

    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool SetForegroundWindow(IntPtr hWnd);
}
"@

    $hwnd = [IntPtr]([Int64]$binding.hwnd)
    $expectedProcessId = [uint32]$binding.pid
    if (-not [RainierWindow]::IsWindow($hwnd)) {
        throw "$problem window binding is stale because the HWND no longer exists"
    }

    [uint32]$actualProcessId = 0
    [RainierWindow]::GetWindowThreadProcessId($hwnd, [ref]$actualProcessId) | Out-Null
    if ($actualProcessId -eq 0 -or $actualProcessId -ne $expectedProcessId) {
        throw "$problem window binding is stale because the HWND now belongs to another process"
    }

    try {
        $proc = Get-Process -Id ([int]$actualProcessId) -ErrorAction Stop
    } catch {
        throw "$problem Chrome process is no longer running"
    }
    if ($proc.ProcessName -ne 'chrome') {
        throw "$problem window binding no longer points to Chrome"
    }

    [RainierWindow]::BringWindowToTop($hwnd) | Out-Null
    Start-Sleep -Milliseconds 80
    $focused = [RainierWindow]::SetForegroundWindow($hwnd)
    if (-not $focused) {
        Start-Sleep -Milliseconds 120
        [RainierWindow]::BringWindowToTop($hwnd) | Out-Null
        $focused = [RainierWindow]::SetForegroundWindow($hwnd)
    }
    if (-not $focused) {
        throw "Windows refused to focus the bound Chrome window for $problem"
    }

    # Do not call ShowWindowAsync/SW_RESTORE here. The user may have the
    # target Chrome window snapped or positioned on a specific monitor.
    Start-Sleep -Milliseconds 350
    $shell = New-Object -ComObject WScript.Shell
    Set-Clipboard -Value $chatUrl
    $shell.SendKeys('^l')
    Start-Sleep -Milliseconds 120
    $shell.SendKeys('^v')
    Start-Sleep -Milliseconds 80
    $shell.SendKeys('{ENTER}')
    Start-Sleep -Milliseconds 250
    Set-Clipboard -Value 'next'
} catch {
    Show-RainierError $_.Exception.Message
    exit 2
}

exit 0
