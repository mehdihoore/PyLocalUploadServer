# Define the function to convert Gregorian date to Persian date
function Convert-ToPersianDate {
    param (
        [DateTime]$gregorianDate
    )
    
    # Create a Persian calendar instance
    $persianCalendar = New-Object System.Globalization.PersianCalendar

    # Extract the Persian date components
    $year = $persianCalendar.GetYear($gregorianDate)
    $month = $persianCalendar.GetMonth($gregorianDate)
    $day = $persianCalendar.GetDayOfMonth($gregorianDate)

    # Format the Persian date as yyyy-MM-dd
    return "{0:D4}-{1:D2}-{2:D2}" -f $year, $month, $day
}

# Define the function to check if the file name already contains a Persian date
function Contains-PersianDate {
    param (
        [string]$fileName
    )
    
    # Regular expression pattern for Persian date in parentheses (yyyy-MM-dd)
    $pattern = '\(\d{4}-\d{2}-\d{2}\)$'
    
    return $fileName -match $pattern
}

# Prompt the user to enter the directory path
$directoryPath = Read-Host "Please enter the directory path"

# Check if the directory exists
if (-Not (Test-Path -Path $directoryPath -PathType Container)) {
    Write-Host "The directory path does not exist. Please enter a valid path."
    exit
}

# Get all files in the directory and its subfolders
Get-ChildItem -Path $directoryPath -File -Recurse | ForEach-Object {
    $file = $_
    $modifiedDate = $file.LastWriteTime

    # Convert the modified date to Persian date
    $persianDate = Convert-ToPersianDate -gregorianDate $modifiedDate

    # Check if the file name already contains a Persian date
    if (-Not (Contains-PersianDate -fileName $file.BaseName)) {
        # Create the new filename with Persian date in parentheses
        $newFileName = "{0} ({1}){2}" -f $file.BaseName, $persianDate, $file.Extension

        # Rename the file
        Rename-Item -Path $file.FullName -NewName $newFileName
    }
}