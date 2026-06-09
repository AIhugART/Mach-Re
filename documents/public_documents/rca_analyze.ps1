$filePath = "BanSacVanHoaVietNam_Phan_Ngoc.md"
$content = Get-Content $filePath -Encoding utf8

$issues = [System.Collections.Generic.List[PSObject]]::new()

for ($i = 0; $i -lt $content.Count; $i++) {
    $line = $content[$i]
    $lineNum = $i + 1

    # 1. Lines with corrupt separator (--- mixed with text)
    if ($line -match "---" -and $line -match "[a-zA-Z\w]" -and $line -notmatch "^## " -and $line.Length -gt 5) {
        $issues.Add([PSCustomObject]@{
            Line = $lineNum
            Type = "CORRUPT_SEPARATOR"
            Content = $line.Substring(0, [Math]::Min(120, $line.Length))
        })
    }

    # 2. Missing TRANG header (header merged with previous line)
    if ($line -match "## TRANG \d+" -and $i -gt 0) {
        $prev = $content[$i - 1]
        if ($prev -notmatch "^\s*$") {
            $issues.Add([PSCustomObject]@{
                Line = $lineNum
                Type = "NO_BLANK_BEFORE_HEADER"
                Content = "Prev: '$($prev.Substring(0, [Math]::Min(60,$prev.Length)))' | This: $($line)"
            })
        }
    }

    # 3. Content merged on same line as separator or header
    if ($line -match "^## TRANG \d+.+\w") {
        $issues.Add([PSCustomObject]@{
            Line = $lineNum
            Type = "TRANG_MERGED_WITH_CONTENT"
            Content = $line.Substring(0, [Math]::Min(120, $line.Length))
        })
    }

    # 4. Very long lines (possible merge of multiple lines)
    if ($line.Length -gt 800) {
        $issues.Add([PSCustomObject]@{
            Line = $lineNum
            Type = "VERY_LONG_LINE"
            Content = "Length=$($line.Length) | $($line.Substring(0, [Math]::Min(100, $line.Length)))"
        })
    }

    # 5. Lines ending mid-word before separator (truncated content)
    if ($line -match "\w$" -and $i + 1 -lt $content.Count -and $content[$i + 1] -match "^---") {
        if ($line.Length -lt 30 -and $line -notmatch "^(#|[-\*]|\d+\.)") {
            $issues.Add([PSCustomObject]@{
                Line = $lineNum
                Type = "POSSIBLE_TRUNCATED_LINE"
                Content = "Line: '$line' (followed by separator)"
            })
        }
    }
}

Write-Host "=== RCA ANALYSIS RESULTS ===" -ForegroundColor Cyan
Write-Host "Total lines: $($content.Count)"
Write-Host "Total issues found: $($issues.Count)"
Write-Host ""

$byType = $issues | Group-Object Type | Sort-Object Count -Descending
foreach ($g in $byType) {
    Write-Host "[$($g.Count)] $($g.Name)" -ForegroundColor Yellow
    $g.Group | Select-Object -First 3 | ForEach-Object {
        Write-Host "  Line $($_.Line): $($_.Content)"
    }
    if ($g.Count -gt 3) { Write-Host "  ... and $($g.Count - 3) more" }
    Write-Host ""
}

# Export to CSV
$issues | Export-Csv -Path "rca_issues.csv" -Encoding utf8 -NoTypeInformation
Write-Host "Full issue list saved to: rca_issues.csv" -ForegroundColor Green
