-- Full description
#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Database name
DB_NAME="$1"

# MySQL command to fetch table information
mysql -e "SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE FROM information_schema.columns WHERE table_schema='$DB_NAME' AND table_name='first_table';"
