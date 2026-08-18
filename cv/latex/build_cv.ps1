[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$toolDir = Join-Path $repoRoot '.tools\tectonic'
$tectonicExe = Join-Path $toolDir 'tectonic.exe'
$buildDir = Join-Path $PSScriptRoot 'build'
$sourceFile = Join-Path $PSScriptRoot 'Hung_Q_Nguyen_CV.tex'
$publishedPdf = Join-Path $repoRoot 'cv\Hung_Q_Nguyen_CV.pdf'

$tectonicVersion = '0.17.0'
$tectonicArchive = "tectonic-$tectonicVersion-x86_64-pc-windows-msvc.zip"
$tectonicUrl = "https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%40$tectonicVersion/$tectonicArchive"

if (-not (Test-Path -LiteralPath $tectonicExe)) {
    Write-Host "Tectonic is not installed. Downloading version $tectonicVersion..."
    New-Item -ItemType Directory -Force -Path $toolDir | Out-Null
    $archivePath = Join-Path $toolDir $tectonicArchive
    try {
        Invoke-WebRequest -Uri $tectonicUrl -OutFile $archivePath
        Expand-Archive -LiteralPath $archivePath -DestinationPath $toolDir -Force
    }
    finally {
        Remove-Item -LiteralPath $archivePath -Force -ErrorAction SilentlyContinue
    }
}

if (-not (Test-Path -LiteralPath $tectonicExe)) {
    throw "Tectonic could not be installed at $tectonicExe"
}

New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

Push-Location $PSScriptRoot
try {
    $previousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $compilerOutput = & $tectonicExe --chatter minimal --synctex --keep-logs --keep-intermediates --outdir $buildDir $sourceFile 2>&1
        $compilerExitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }
    if ($compilerExitCode -ne 0) {
        $compilerOutput | ForEach-Object { Write-Host $_ }
        throw "LaTeX compilation failed with exit code $compilerExitCode. See $buildDir for the log."
    }
}
finally {
    Pop-Location
}

$builtPdf = Join-Path $buildDir 'Hung_Q_Nguyen_CV.pdf'
if (-not (Test-Path -LiteralPath $builtPdf)) {
    throw "Compilation finished without producing $builtPdf"
}

Copy-Item -LiteralPath $builtPdf -Destination $publishedPdf -Force
Write-Host "CV compiled successfully: $publishedPdf"
