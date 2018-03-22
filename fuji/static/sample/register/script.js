/** 
 * @brief ログイン用のAPIにアクセスする
 * @detail フォームから情報を受取り、そのデータをJSONにパースした後、APIにアクセスしてログインする。
 */
function register(){    
    // フォームの情報をJSONにする
    var json = {
        email: document.getElementById('email').value,
        name: document.getElementById('name').value,
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
            alert(JSON.stringify(data));
        },
        error : function(data) {
            // レスポンスを表示
            alert(JSON.stringify(data));
        }
    });
};
