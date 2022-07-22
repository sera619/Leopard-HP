<# PowerShell simple GUI Helper for Python libary "Flask"#>


Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$form = New-Object System.Windows.Forms.Form
$form.Text = 'Flask Runner © S3R43o3'
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
$label.Text = "Flask Webserver, wähle einen modus"
$form.Controls.Add($label)

$listBox = New-Object System.Windows.Forms.ListBox
$listBox.Location = New-Object System.Drawing.Point(10,40)
$listBox.Size = New-Object System.Drawing.Size(300,20)
$listBox.Height = 80

[void] $listBox.Items.Add('Development mode')
[void] $listBox.Items.Add('Production mode')
[void] $listBox.Items.Add('Exit')

$form.Controls.Add($listBox)

$form.Topmost = $true

$result = $form.ShowDialog()


if ($result -eq [System.Windows.Forms.DialogResult]::OK)
{
    $x = $listBox.SelectedItem
    if($x -eq "Development mode"){
        Clear-Host
        Write-Host "-: Flask Runner 1.0 :-" -ForegroundColor Blue -Separator "|"
        Write-Host " "
        Write-Host "[Flask Runner] - Starting in development mode..." -ForegroundColor Yellow
        Write-Host " "
        C:\1Coding\Python\Leopard-HP\env-leos\Scripts\activate.ps1
        $env:FLASK_ENV="development"
        flask run
    }
    elseif ($x -eq "Production mode") {
        Clear-Host
        Write-Host "-: Flask Runner 1.0 :-" -ForegroundColor Blue
        Write-Host " "
        Write-Host "[Flask Runner] - Starting in production mode..." -ForegroundColor Yellow
        Write-Host " "
        C:\1Coding\Python\Leopard-HP\env-leos\Scripts\activate.ps1
        $env:FLASK_ENV="production"
        flask run
        
    }
    elseif ($x -eq "Exit") {
        Exit-PSSession
    }
}