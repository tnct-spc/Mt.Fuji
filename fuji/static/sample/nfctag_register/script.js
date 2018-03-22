/** 
 * @brief NFCTagのAPIにアクセスして登録する
 * @detail APIにログインした後、NFCTagのAPIにアクセスして登録する
 */
async function nfctag_register(){
    await new Promise((resolve) => {
        /* まずログインする */
        // 登録に必要な情報をJSONにする
        var json = {
            email: document.getElementById('email').value,
            password: document.getElementById('password').value
        };

        // JSONデータの文字列化
        json = JSON.stringify(json);

        // APIにデータ送信
        $.ajax({
            type : 'post',
            url : 'http://localhost:8000/account/register/',
            data : json,
            contentType: 'application/JSON',
            dataType : 'JSON',
            scriptCharset: 'utf-8',
            success : function(data) {
                // レスポンスを表示
                alert(1);
                alert(JSON.stringify(data));
                resolve();
            },
            error : function(data) {
                // レスポンスを表示
                alert(1);
                alert(JSON.stringify(data));
                resolve();
            }
        });
    });

    /* NFCTagを登録する */
    // 登録に必要な情報をJSONにする
    var json = {
        IDm: document.getElementById('idm').value
    }
    
    // JSONデータの文字列化
    json = JSON.stringify(json);

    // APIにデータ送信
    $.ajax({
        type : 'post',
        url : 'http://localhost:8000/nfc/register/',
        data : json,
        contentType: 'application/JSON',
        dataType : 'JSON',
        scriptCharset: 'utf-8',
        success : function(data) {
            // レスポンスを表示
            alert(2);
            alert(JSON.stringify(data));
        },
        error : function(data) {
            // レスポンスを表示
            alert(2);
            alert(JSON.stringify(data));
        }
    });
}


