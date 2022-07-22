#disable telemetry
function Disable-Telemetry{
    function Disable-Telemetry {

        # Stop and Disable DiagTrack Service
        Get-Service -Name DiagTrack | Set-Service -Status Stopped -StartupType Disabled 
      
        # Stop and Disable dmwappushservice Service
        Get-Service -Name dmwappushservice | Set-Service -Status Stopped -StartupType Disabled 
      
        # Disable Perfmon DiagTrack entry
        Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\WMI\Autologger\Diagtrack-Listener\ -name Start -Value 0
      
        # Disable DataCollection entry
        Set-ItemProperty -Path HKLM:\SOFTWARE\Policies\Microsoft\Windows\DataCollection\ -name AllowTelemetry -Value 0
      
        # Disable Wifi Sense
        Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\features\ -name WiFiSenseCredShared -Value 0
        Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\features\ -name WiFiSenseOpen -Value 0
      
        # Disable Wifi Sense on newer Windows 10
        $path = "\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\features"
        Get-ChildItem HKLM:$path  | Where-Object { $_.Name.EndsWith("-1000") } | Set-ItemProperty -name FeatureStates -Value 0
      
        # https://www.pcwelt.de/a/bundesamt-fuer-it-sicherheit-bsi-untersucht-sicherheit-von-windows-10,3463082
      
      
        # „HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search” und ändern dort den Wert bei „AllowCortana“ auf 0. Sollte der Schlüssel oder der Eintrag nicht existieren, dann müssen Sie ihn jeweils manuell anlegen.
      
        # https://intermundien.de/windows-sicherheitseinschraenkung-feeback-und-diagnose-ueber-gpo/
      }
      
      # $trigger = New-JobTrigger -AtStartup -RandomDelay 00:00:30
      # Register-ScheduledJob -Trigger $trigger -FilePath C:\temp\Disable-Telemetry.ps1 -Name DisableTelemetry
      
}


Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$form = New-Object System.Windows.Forms.Form
$form.Text = 'Telemetry Disabler © S3R43o3'
$form.Size = New-Object System.Drawing.Size(350,200)
$form.StartPosition = 'CenterScreen'

$okButton = New-Object System.Windows.Forms.Button
$okButton.Location = New-Object System.Drawing.Point(100,130)
$okButton.Size = New-Object System.Drawing.Size(75,23)
$okButton.Text = 'OK'
$okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
$form.AcceptButton = $okButton
$form.Controls.Add($okButton)

$cancelButton = New-Object System.Windows.Forms.Button
$cancelButton.Location = New-Object System.Drawing.Point(175,130)
$cancelButton.Size = New-Object System.Drawing.Size(75,23)
$cancelButton.Text = 'Cancel'
$cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
$form.CancelButton = $cancelButton
$form.Controls.Add($cancelButton)

$label = New-Object System.Windows.Forms.Label
$label.Location = New-Object System.Drawing.Point(10,20)
$label.Size = New-Object System.Drawing.Size(320,20)
$label.Text = "Disable the telemetry data collector. Select a option"
$form.Controls.Add($label)

$listBox = New-Object System.Windows.Forms.ListBox
$listBox.Location = New-Object System.Drawing.Point(10,40)
$listBox.Size = New-Object System.Drawing.Size(300,20)
$listBox.Height = 80

[void] $listBox.Items.Add('Disable Telemetry')
[void] $listBox.Items.Add('Exit')

$form.Controls.Add($listBox)

$form.Topmost = $true

$result = $form.ShowDialog()


if ($result -eq [System.Windows.Forms.DialogResult]::OK)
{
    $x = $listBox.SelectedItem
    if($x -eq "Disable Telemetry"){
        Clear-Host
        Write-Host "-: Windows Telemetry Disabler :-" -ForegroundColor Blue -Separator "|"
        Write-Host " "
        Write-Host "[Telemetry Disabler] - deactivate telemetry..." -ForegroundColor Yellow
        Write-Host " "
        Disable-Telemetry
        Write-Host "[Telemetry Disabler] - Windows Telemetry successfully disabled!`r`n`r`nThanks for using my software!" -ForegroundColor Yellow
        Start-Sleep -Milliseconds 350
        Exit-PSSession
        Exit
    }
    elseif ($x -eq "Exit") {
        Exit-PSSession
        Exit
    }
}