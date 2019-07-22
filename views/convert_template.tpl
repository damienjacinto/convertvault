<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Service de chiffrement/déchiffrement</title>
    <link rel="stylesheet" href="/static/css/mystyle.css" type="text/css"/> 
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        document.querySelector('#copy-button').addEventListener('click', function() {
            try {
                var copyText = document.querySelector("#result");
                copyText.select();
                document.execCommand("copy");
                window.getSelection().removeAllRanges();
            } catch(e) {}
        });
    });    
    </script>
</head>
<body>
    <nav class="navbar">
        <div class="titleNavbar">Service de chiffrement/déchiffrement ansible-vault à la volée</div>
    </nav>

    <form method="POST">
        <div class="input">
            <div class="flex-col1">
                <label for="vaultpassword">Clé de chiffrement :</label>
                <input type="password" class="form-control password" name="vaultpassword" placeholder="Enter encryption key" value="{{password}}" pattern=".{,30}" required title="max 30 characters">
                <small class="error">{{error}}</small>
            </div>
            <div class="flex-col2">
                <button class="btn" type="submit" id="send">Encrypt or Decrypt</button>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <textarea class="form-control" name="source" rows="25">{{source}}</textarea>
            </div>

            <div class="col">
                <textarea class="form-control" name="result" id="result" readonly rows="25">{{result}}</textarea>
                <span title="Copy to clipboard" class="icon-copy" id="copy-button" />
            </div>
        </div>
    </form>

</body>
</html>