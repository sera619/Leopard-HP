<# Title: Poweshell Menu #>

$List = "1) Flask Development", "2) Flask Production", "0) Exit"

$ymin = 3
$xmin = 3
Clear-Host
Write-Host ""
Write-Host -ForegroundColor Blue "-: Python Flask-Development Helper :-" 
Write-Host ""

[Console]::SetCursorPosition(0, $ymin)
foreach ($name in $list) {
    for ($i = 0; $i -lt $xmin; $i++){
        Write-Host "" -NoNewline

    }
    Write-Host "" + $name
}

#Highlight selected item
function Write-Highlighted{
    [Console]::SetCursorPosition(1 + $xmin, $cursorY + $ymin)
    Write-Host ">" -BackgroundColor Yellow -ForegroundColor Black -NoNewline
    Write-Host "" + $List[$cursorY] -BackgroundColor Yellow -ForegroundColor Black
    [Console]::SetCursorPosition(0, $cursorY + $ymin)
}   


#remove higlighted text
function Write-Normal{
    [Console]::SetCursorPosition(1 + $xmin, $cursorY + $ymin)
    Write-Host "" + $List[$cursorY]
}


# default highlight first item
$cursorY = 0
Write-Highlighted
$selection = ""
$menu_active = $true
while ($menu_active){
    if([Console]::KeyAvailable){
        $x = $Host.UI.RawUI.ReadKey()
        [Console]::SetCursorPosition(1, $cursorY)
        Write-Normal
        switch ($x.VirtualKeyCode){
            38 {
                # arrowdown key
                if($cursorY -gt 0){
                    $cursorY = $cursorY - 1
                }
            }
            40{
                # arrowup key
                if($cursorY -lt $List.Length - 1){
                    $cursorY = $cursorY + 1
                }
            }
            13{
                # enter key
                $selection = $List[$cursorY]
                $menu_active = $false
            }
        }
        Write-Highlighted
    }
    # prevent CPU usage spikes
    Start-Sleep -Milliseconds 5 
}
Clear-Host
if($selection -eq "1) Flask Development"){
    Write-Host "Development mode used."
    c:/1Coding/Python/Leopard-HP/h2-env/Scripts/Activate.ps1
    $env:FLASK_ENV="development"
    flask run
}elseif ($selection -eq "2) Flask Production") {
    Write-Host "Production mode used."
    c:/1Coding/Python/Leopard-HP/h2-env/Scripts/Activate.ps1
    $env:FLASK_ENV="production"
    flask run
}