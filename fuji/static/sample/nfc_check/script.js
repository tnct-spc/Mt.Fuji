/** 
 * @brief NFC検索用のAPIにアクセスする
 * @detail フォームから情報を受取り、そのデータをJSONにパースした後、APIにアクセスして登録されたNFCタグかを確認する
 */
function search(){
    // フォームの情報をJSONにする
    var json = {
        IDm: document.getElementById('idm').value
    };

    // JSONデータの文字列化
    json = JSON.stringify(json);

    // APIにデータ送信
    $.ajax({
        type : 'post',
        url : 'http://localhost:8000/nfc/check/',
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
