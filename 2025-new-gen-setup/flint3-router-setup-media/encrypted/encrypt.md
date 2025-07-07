# Hidden files

https://superuser.com/questions/370388/simple-built-in-way-to-encrypt-and-decrypt-a-file-on-a-mac-via-command-line

Passkey: 2....p

## Wifi pwd

```shell
cd 2025-new-gen-setup/flint3-router-setup-media/encrypted
# encrypt file.txt to file.enc using 256-bit AES in CBC mode
openssl enc -aes-256-cbc -salt -in wifi-pwd.txt -out wifi-pwd.txt.enc
```

```shell
cd 2025-new-gen-setup/flint3-router-setup-media/encrypted
# decrypt binary file.enc
openssl enc -d -aes-256-cbc -in wifi-pwd.txt.enc -out wifi-pwd.txt
```

## Box details

```shell
cd 2025-new-gen-setup/flint3-router-setup-media/encrypted
# encrypt file.txt to file.enc using 256-bit AES in CBC mode
openssl enc -aes-256-cbc -salt -in BE9300-Wi-Fi-7-Router.jpeg -out BE9300-Wi-Fi-7-Router.jpeg.enc
```

```shell
cd 2025-new-gen-setup/flint3-router-setup-media/encrypted
# decrypt binary file.enc
openssl enc -d -aes-256-cbc -in BE9300-Wi-Fi-7-Router.jpeg.enc -out BE9300-Wi-Fi-7-Router.jpeg
```

