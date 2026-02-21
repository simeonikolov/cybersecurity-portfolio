# Splunk Queries

## Failed SSH logins
index=linux_logs "Failed password"

## Count by IP
index=linux_logs | stats count by src_ip

## Suspicious sudo usage
index=linux_logs "sudo"
