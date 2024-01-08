#!/bin/bash


output=$(avahi-browse -d local  _spotify-connect._tcp --resolve --parsable --terminate)



echo "--------------- Avahi output ---------------------------------"
echo "$output"
 

echo "--------------- Avahi filtered output -------------------------"
# Use grep to filter lines with "="
filtered_output=$(echo "$output" | grep '=')
echo $filtered_output

echo "--------------- Avahi filtered output with ip, port, zc path ---"
echo "$filtered_output" | awk -F ';' '{print $8, $9, $10}' 


echo "--------------- Curl spotify zc api ----------------------------"

ARRAY=()
# Use awk to extract IP, port, and path, then perform curl requests
echo "$filtered_output" | awk -F ';' '{print $8, $9, $10}' | while read -r ip port path; do
    
    # Construct the URL
    url="http://${ip}:${port}/zc"

    # Make a curl request to the service
    curl_result=$(curl -s "$url?action=getInfo") 

    # Print the result for each iteration
    echo "Curl Result for $url"
    echo $curl_result | jq -C
    echo $curl_result | jq -C -r '.remoteName, .modelDisplayName, .aliases[0].name, .groupStatus'
    echo "---------------------------------"
done
